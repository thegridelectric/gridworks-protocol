from dataclasses import dataclass, field
from typing import Any, Optional, Type

from gwproto import Message, MQTTCodec


@dataclass
class MessageCase:
    tag: str
    src_message: Message
    exp_message: Optional[Message] = None
    exp_payload: Any = None
    exp_exceptions: list[Type[Exception]] = field(default_factory=list)


@dataclass
class CaseError:
    case_idx: int
    case: MessageCase

    def __str__(self) -> str:
        return f"{self.case.tag:30s}  {self.case_idx:2d}  {type(self)}"


@dataclass
class DecodeError(CaseError):
    exception: Exception

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\t\t{type(self.exception)}"
            f"\n\t\t{self.exception}"
        )


@dataclass
class MessageMatchError(CaseError):
    exp_message: Message
    decoded_message: Message

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\t\texp: {type(self.exp_message)}"
            f"\n\t\tgot: {type(self.decoded_message)}"
        )


@dataclass
class PayloadMatchError(CaseError):
    exp_payload: Any
    decoded_payload: Any

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\t\texp: {type(self.exp_payload)}"
            f"\n\t\tgot: {type(self.decoded_payload)}"
        )


@dataclass
class DecodeResult:
    ok: bool
    decoded: Message | None
    exception: Exception | None


def _decode(
    src_codec: MQTTCodec,
    dst_codec: MQTTCodec,
    case: MessageCase,
) -> DecodeResult:
    decoded: Message | None
    exception: Exception | None
    ok: bool
    try:
        decoded = dst_codec.decode(
            case.src_message.mqtt_topic(),
            src_codec.encode(case.src_message),
        )
        exception = None
    except Exception as e:  # noqa: BLE001
        decoded = None
        exception = e
    if decoded is None:
        ok = type(exception) in case.exp_exceptions
    else:
        ok = not case.exp_exceptions
    return DecodeResult(ok, decoded, exception)


def assert_encode_decode(
    src_codec: MQTTCodec,
    dst_codec: MQTTCodec,
    messages: list[MessageCase],
) -> None:
    errors: list[CaseError] = []
    for case_idx, case in enumerate(messages):
        decode_result = _decode(
            src_codec,
            dst_codec,
            case,
        )
        if not decode_result.ok:
            errors.append(DecodeError(case_idx, case, decode_result.exception))
        elif not case.exp_exceptions:
            if case.exp_message is not None:
                if decode_result.decoded != case.exp_message:
                    errors.append(
                        MessageMatchError(
                            case_idx,
                            case,
                            exp_message=case.exp_message,
                            decoded_message=decode_result.decoded,
                        )
                    )
            else:
                if case.exp_payload is None:
                    exp_payload = case.src_message.Payload
                else:
                    exp_payload = case.exp_payload
                if decode_result.decoded.Payload != exp_payload:
                    errors.append(
                        PayloadMatchError(
                            case_idx,
                            case,
                            exp_payload=exp_payload,
                            decoded_payload=decode_result.decoded.Payload,
                        )
                    )
    if errors:
        err_str = "ERROR. Got codec matching errors:"
        for error in errors:
            err_str += f"\n\t{error}"
        raise ValueError(err_str)
