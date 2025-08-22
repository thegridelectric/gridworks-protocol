# ruff: noqa: ANN401

from collections.abc import Mapping
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
        payload = kwargs_dict.get("Payload")
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
            # Extract header fields from payload and kwargs
            header_kwargs = {}

            # Get from kwargs first
            for field in ["src", "dst", "message_id", "ack_required"]:
                if field in kwargs:
                    header_kwargs[field] = kwargs[field]

            # Extract from payload (these override kwargs)
            if hasattr(payload, "src"):
                header_kwargs["src"] = payload.src
            if hasattr(payload, "dst"):
                header_kwargs["dst"] = payload.dst
            if hasattr(payload, "message_id"):
                header_kwargs["message_id"] = payload.message_id
            if hasattr(payload, "ack_required"):
                header_kwargs["ack_required"] = payload.ack_required

            # MessageType always comes from payload.type_name
            header_kwargs["message_type"] = payload.type_name_value()

            header = Header(**header_kwargs)

        super().__init__(header=header, payload=payload)

    @model_validator(mode="after")
    def validate_message_type_consistency(self) -> Self:
        """Axiom 1: payload.type_name must equal header.message_type"""
        if self.header.message_type != self.payload.type_name:
            raise ValueError(
                f"Header message_type '{self.headers.message_type}' "
                f"doesn't match payload type_name '{self.payload.type_name}'"
            )
        return self

    @model_validator(mode="after")
    def validate_message_id_consistency(self) -> Self:
        """Axiom 2: if payload.message_id exists, it must equal header.message_id"""
        if hasattr(self.payload, "message_id") and self.payload.message_id:
            if (
                self.header.message_id
                and self.header.message_id != self.payload.message_id
            ):
                raise ValueError(
                    f"Header message_id '{self.header.message_id}' "
                    f"doesn't match payload message_id '{self.payload.message_id}'"
                )
            # If header.message_id is empty, set it from payload
            if not self.header.message_id:
                self.header.message_id = self.payload.message_id
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

    @classmethod
    def _header_from_kwargs(cls, kwargs: dict[str, Any]) -> Header:
        header_kwargs = {}
        if "payload" in kwargs:
            payload = kwargs["payload"]

            # Map header fields to possible payload sources
            # Header field -> (snake_case attr, PascalCase dict key)
            field_mappings = [
                ("Src", "src", "Src"),
                ("Dst", "dst", "Dst"),
                ("MessageId", "message_id", "MessageId"),
                ("MessageType", "type_name", "TypeName"),
                ("AckRequired", "ack_required", "AckRequired"),
            ]
            for header_field, attr_name, dict_key in field_mappings:
                val = kwargs.get(header_field)
                if val is None:
                    if hasattr(payload, attr_name):
                        # Payload is an object with snake_case attributes
                        val = getattr(payload, attr_name)
                    elif isinstance(payload, Mapping) and dict_key in payload:
                        # Payload is a dict with PascalCase keys
                        val = payload[dict_key]
                if val is not None:
                    header_kwargs[header_field] = val

        header = kwargs.pop("Header", None)
        d = dict(header) if header is not None else {}
        d.update(header_kwargs)
        return Header.from_dict(d)


GRIDWORKS_ENVELOPE_TYPE = Message.type_name_value()
