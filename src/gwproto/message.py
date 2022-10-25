from typing import Any
from typing import Callable
from typing import Generic
from typing import Mapping
from typing import Optional
from typing import TypeVar
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic.generics import GenericModel

from gwproto.topic import MQTTTopic


EnumType = TypeVar("EnumType")


def as_enum(
    value: Any, enum_type: Callable[[Any], EnumType], default: Optional[EnumType] = None
) -> Optional[EnumType]:
    try:
        return enum_type(value)
    except ValueError:
        return default


class Header(BaseModel):
    src: str
    dst: str = ""
    message_type: str
    message_id: str = ""
    type_name: str = Field("gridworks.header.000", const=True)


PayloadT = TypeVar("PayloadT")

PAYLOAD_TYPE_FIELDS = ["type_name", "type_alias", "TypeAlias"]

GRIDWORKS_ENVELOPE_TYPE = "gw"


class Message(GenericModel, Generic[PayloadT]):
    header: Header
    payload: PayloadT
    type_name: str = Field(GRIDWORKS_ENVELOPE_TYPE, const=True)

    def __init__(self, **kwargs: Any):
        kwargs["header"] = self._header_from_kwargs(kwargs)
        super().__init__(**kwargs)

    def message_type(self) -> str:
        return self.header.message_type

    def src(self) -> str:
        return self.header.src

    # TODO: Rename as "type_name" after renaming field to TypeName
    @classmethod
    def get_type_name(cls) -> str:
        return Message.__fields__["type_name"].default

    def mqtt_topic(self) -> str:
        return MQTTTopic.encode(self.src(), self.get_type_name(), self.message_type())

    @classmethod
    def _header_from_kwargs(cls, kwargs: dict[str, Any]) -> Header:
        header_kwargs = dict()
        payload = kwargs["payload"]
        for header_field, payload_fields in [
            ("src", ["src"]),
            ("dst", ["dst"]),
            ("message_id", ["message_id"]),
            ("message_type", PAYLOAD_TYPE_FIELDS),
        ]:
            val = kwargs.get(header_field, None)
            if val is None:
                for payload_field in payload_fields:
                    if hasattr(payload, payload_field):
                        val = getattr(payload, payload_field)
                    elif isinstance(payload, Mapping) and payload_field in payload:
                        val = payload[payload_field]
            if val is not None:
                header_kwargs[header_field] = val
        header: Optional[Union[Header, dict[str, Any]]] = kwargs.get("header", None)
        if isinstance(header, Header):
            header = header.copy(update=header_kwargs, deep=True)
        else:
            if header is not None:
                header_kwargs = dict(header, **header_kwargs)
            header = Header(**header_kwargs)
        return header
