from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any, Optional, Type

from result import Err, Ok, Result

from gwproto import Message, MQTTCodec


@dataclass
class MessageCase:
    tag: str
    src_message: Message[Any]
    exp_message: Optional[Message[Any]] = None
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
    exception: Exception | None

    def __str__(self) -> str:
        return f"{super().__str__()}\n\t\t{type(self.exception)}\n\t\t{self.exception}"


@dataclass
class MessageMatchError(CaseError):
    exp_message: Message[Any]
    decoded_message: Message[Any] | None

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


class NoExceptionError(ValueError):
    expected_types: Sequence[Type[Exception]]

    def __init__(self, expected_types: Sequence[Type[Exception]]) -> None:
        self.expected_types = expected_types


class UnexpectedExceptionTypeError(ValueError):
    got: Exception
    expected_types: Sequence[Type[Exception]]

    def __init__(
        self, got: Exception, expected_types: Sequence[Type[Exception]]
    ) -> None:
        self.got = got
        self.expected_types = expected_types


# class MessageCase:
#     tag: str
#     src_message: Message[Any]
#     exp_message: Optional[Message[Any]] = None
#     exp_payload: Any = None
#     exp_exceptions: list[Type[Exception]] = field(default_factory=list)


def _decode(
    src_codec: MQTTCodec,
    dst_codec: MQTTCodec,
    case: MessageCase,
) -> Result[Message[Any] | Exception, Exception]:
    try:
        decoded = dst_codec.decode(
            case.src_message.mqtt_topic(),
            src_codec.encode(case.src_message),
        )
        if case.exp_exceptions:
            return Err(NoExceptionError(case.exp_exceptions))
        return Ok(decoded)
    except Exception as e:  # noqa: BLE001
        if case.exp_exceptions and type(e) in case.exp_exceptions:
            return Ok(e)
        return Err(
            UnexpectedExceptionTypeError(got=e, expected_types=case.exp_exceptions)
        )


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
        match decode_result:
            case Err():
                errors.append(DecodeError(case_idx, case, decode_result.err()))
            case _:
                match decode_result.ok_value:
                    case Message() as decoded:
                        if case.exp_message is not None:
                            if decoded != case.exp_message:
                                errors.append(
                                    MessageMatchError(
                                        case_idx,
                                        case,
                                        exp_message=case.exp_message,
                                        decoded_message=decoded,
                                    )
                                )
                        else:
                            if case.exp_payload is None:
                                exp_payload = case.src_message.Payload
                            else:
                                exp_payload = case.exp_payload
                            if decoded.Payload != exp_payload:
                                errors.append(
                                    PayloadMatchError(
                                        case_idx,
                                        case,
                                        exp_payload=exp_payload,
                                        decoded_payload=decoded.Payload,
                                    )
                                )
    if errors:
        err_str = "ERROR. Got codec matching errors:"
        for error in errors:
            err_str += f"\n\t{error}"
        raise ValueError(err_str)
