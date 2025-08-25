# ruff: noqa: ANN401

from typing import (
    Any,
    Callable,
    Generic,
    Literal,
    Optional,
    Self,
    TypeVar,
)

from gw.named_types import GwBase
from pydantic import model_validator

from gwproto.topic import MQTTTopic

EnumType = TypeVar("EnumType")


def as_enum(
    value: Any, enum_type: Callable[[Any], EnumType], default: Optional[EnumType] = None
) -> Optional[EnumType]:
    try:
        return enum_type(value)
    except ValueError:
        return default


class Header(GwBase):
    src: str
    dst: str = ""
    message_type: str
    message_id: str = ""
    ack_required: bool = False
    type_name: Literal["gridworks.header"] = "gridworks.header"
    version: str = "001"


def ensure_arg(arg_name: str, default_value: Any, kwargs_dict: dict[str, Any]) -> None:
    if arg_name not in kwargs_dict:
        payload = kwargs_dict.get("payload")
        if payload is None or not hasattr(payload, arg_name):
            kwargs_dict[arg_name] = default_value


PayloadT = TypeVar("PayloadT", bound=GwBase)


class Message(GwBase, Generic[PayloadT]):
    header: Header
    payload: PayloadT
    type_name: Literal["gw"] = "gw"

    def __init__(
        self, *, payload: PayloadT, header: Optional[Header] = None, **kwargs: Any
    ) -> None:
        if header is None:
            header_kwargs = {}

            # Get from kwargs first (lowest priority)
            for field in ["src", "dst", "message_id", "ack_required"]:
                if field in kwargs and kwargs[field] is not None:
                    header_kwargs[field] = kwargs[field]

            # Overwrite from payload (these override kwargs)
            if hasattr(payload, "src"):
                header_kwargs["src"] = payload.src
            if hasattr(payload, "dst"):
                header_kwargs["dst"] = payload.dst
            if hasattr(payload, "message_id"):
                header_kwargs["message_id"] = payload.message_id
            if hasattr(payload, "ack_required"):
                header_kwargs["ack_required"] = payload.ack_required

            # MessageType always comes from payload.type_name
            header_kwargs["message_type"] = payload.type_name

            header = Header.from_dict(header_kwargs)

        super().__init__(header=header, payload=payload)

    @model_validator(mode="after")
    def validate_message_type_consistency(self) -> Self:
        """Axiom 1: payload.type_name must equal header.message_type"""
        if self.header.message_type != self.payload.type_name:
            raise ValueError(
                f"Header message_type '{self.header.message_type}' "
                f"doesn't match payload type_name '{self.payload.type_name}'"
            )
        return self

    @model_validator(mode="after")
    def validate_message_id_consistency(self) -> Self:
        """Axiom 2: if payload.message_id exists, it must equal header.message_id"""
        pid = getattr(self.payload, "message_id", None)
        if pid:
            hid = self.header.message_id
            if not hid:
                raise ValueError(
                    f"Payload has message_id '{pid}' but header.message_id is missing"
                )
            if hid != pid:
                raise ValueError(
                    f"Header message_id '{hid}' doesn't match payload message_id '{pid}'"
                )
        return self

    @model_validator(mode="after")
    def validate_src_consistency(self) -> Self:
        """Axiom 2: if payload.src exists, it must equal header.src"""
        p_src = getattr(self.payload, "src", None)
        if p_src:
            h_src = self.header.src
            if not h_src:
                raise ValueError(f"Payload has src '{p_src}' but header.src is missing")
            if h_src != p_src:
                raise ValueError(
                    f"Header src '{h_src}' doesn't match payload src '{p_src}'"
                )
        return self

    def message_type(self) -> str:
        return self.header.message_type

    def src(self) -> str:
        return self.header.src

    def dst(self) -> str:
        return self.header.dst

    def mqtt_topic(self) -> str:
        return MQTTTopic.encode(
            envelope_type="gw",
            src=self.src(),
            dst=self.dst(),
            message_type=self.message_type(),
        )

    def __repr__(self) -> str:
        return (
            f"Message("
            f"src='{self.header.src}', "
            f"dst='{self.header.dst}', "
            f"type='{self.header.message_type}', "
            f"payload={self.payload.__class__.__name__}"
            f")"
        )

    def __str__(self) -> str:
        return f"{self.header.src} -> {self.header.dst}: {self.header.message_type}"


GRIDWORKS_ENVELOPE_TYPE = Message.type_name_value()
