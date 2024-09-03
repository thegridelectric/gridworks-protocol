# ruff: noqa: ANN401

import abc
import inspect
import json
import re
import sys
import typing
from abc import abstractmethod
from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Literal,
    NamedTuple,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
    get_origin,
)

import pydantic
from pydantic import BaseModel, Field, ValidationError, create_model

from gwproto.message import Header, Message
from gwproto.messages import AnyEvent
from gwproto.topic import MQTTTopic


class Decoder(abc.ABC):
    def decode_str(self, content: str | bytes, encoding: str = "utf-8") -> Any:
        if isinstance(content, bytes):
            content = content.decode(encoding)
        return self.decode_obj(json.loads(content))

    @abstractmethod
    def decode_obj(self, o: Any) -> Any: ...


class CallableDecoder(Decoder):
    _decode_obj: Callable[[Any], Any]

    def __init__(self, decode_obj: Callable[[Any], Any]) -> None:
        if not callable(decode_obj):
            raise TypeError(
                f"ERROR. decode_obj {decode_obj}/{type(decode_obj)} attribute is not Callable"
            )
        self._decode_obj = decode_obj

    def decode_obj(self, o: Any) -> Any:
        return self._decode_obj(o)


class PydanticDecoder(CallableDecoder):
    def __init__(self, model: Type["BaseModel"]) -> None:
        super().__init__(model.model_validate)


class MakerDecoder(CallableDecoder):
    DECODER_FUNCTION_NAME: str = "dict_to_tuple"

    def __init__(self, model: Any) -> None:
        decoder_function = getattr(model, self.DECODER_FUNCTION_NAME, None)
        if decoder_function is None:
            raise ValueError(
                f"ERROR. {model} has no function {self.DECODER_FUNCTION_NAME}"
            )
        super().__init__(decoder_function)


MessageDiscriminator = TypeVar("MessageDiscriminator", bound=Message[Any])


class MessageDecoder(Decoder):
    decoders: "Decoders"
    message_payload_discriminator: Optional[MessageDiscriminator]

    def __init__(
        self,
        decoders: "Decoders",
        message_payload_discriminator: Optional[Type[MessageDiscriminator]] = None,
    ) -> None:
        self.decoders = decoders
        self.message_payload_discriminator = message_payload_discriminator

    @classmethod
    def _try_message_as_event(cls, message_dict: dict, e: ValidationError) -> Message:
        special_typename_handling_message: Optional[Message[Any]] = None
        for error in e.errors():
            if error.get("type", "") == "union_tag_invalid":
                ctx = error.get("ctx", {})
                if ctx.get("discriminator", "") == "'TypeName'" and ctx.get(
                    "tag", ""
                ).startswith("gridworks.event"):
                    try:
                        message_dict["Payload"] = AnyEvent(**message_dict["Payload"])
                        special_typename_handling_message = Message(**message_dict)
                    except Exception as e2:  # noqa: BLE001
                        raise e2 from e
        if special_typename_handling_message is None:
            raise e
        return special_typename_handling_message

    def decode_obj(self, o: Any) -> Message[Any]:
        message_dict: dict = dict(o)
        message_dict["Header"] = Header.model_validate(message_dict.get("Header", {}))
        message: Message[Any]
        if message_dict["Header"].MessageType in self.decoders:
            message_dict["Payload"] = self.decoders.decode_obj(
                message_dict["Header"].MessageType,
                message_dict.get("Payload", {}),
            )
            message = Message(**message_dict)
        else:
            try:
                message = self.message_payload_discriminator.model_validate(
                    message_dict
                )
            except pydantic.ValidationError as e:
                # This can result because we receive a TypeName we don't recognize, either because the sender is
                # newer or older than our code. In some cases we can still meaningfully interpret the message,
                # for example if we can recognize that it is an event messasge, as is done here.
                message = self._try_message_as_event(message_dict, e)
        return message


class DecoderItem(NamedTuple):
    type_name: str
    decoder: Decoder


DEFAULT_TYPE_NAME_FIELD: str = "TypeName"
DEFAULT_PAYLOAD_FIELD: str = "Payload"
DEFAULT_EXCLUDED_TYPE_NAMES: set[str] = {Message.type_name()}


@dataclass
class OneDecoderExtractor:
    type_name_field: str = DEFAULT_TYPE_NAME_FIELD
    decoder_function_name: str = "parse_obj"

    def get_type_name(self, obj: Any) -> str:
        if not (type_name := getattr(obj, self.type_name_field, "")):  # noqa: SIM102
            if (decoder_fields := getattr(obj, "model_fields", None)) is not None:  # noqa: SIM102
                if (
                    model_field := decoder_fields.get(self.type_name_field, None)
                ) is not None:
                    type_name = getattr(model_field, "default", "")
        return type_name

    def get_decoder(self, obj: Any) -> Optional[Decoder]:
        decoder_function = getattr(obj, self.decoder_function_name, None)
        if callable(decoder_function):
            decoder = CallableDecoder(decoder_function)
        else:
            decoder = None
        return decoder

    def extract(self, obj: Any) -> Optional[DecoderItem]:
        item = None
        if type_name := self.get_type_name(obj):  # noqa: SIM102
            if (decoder := self.get_decoder(obj)) is not None:
                item = DecoderItem(type_name, decoder)
        return item


@dataclass
class MakerExtractor(OneDecoderExtractor):
    type_name_field: str = "type_name"
    decoder_function_name: str = MakerDecoder.DECODER_FUNCTION_NAME


class Decoders:
    _decoders: dict[str, Decoder]

    def __init__(self, decoders: Optional[dict[str, Decoder]] = None) -> None:
        self._decoders = {}
        if decoders is not None:
            self.add_decoders(decoders)

    def decoder(self, type_name: str) -> Decoder:
        return self._decoders[type_name]

    def decode_str(
        self, type_name: str, content: str | bytes, encoding: str = "utf-8"
    ) -> Any:
        return self.decoder(type_name).decode_str(content, encoding=encoding)

    def decode_obj(self, type_name: str, o: Any) -> Any:
        return self.decoder(type_name).decode_obj(o)

    def add_decoder(self, type_name: str, decoder: Decoder) -> "Decoders":
        self._validate(type_name, decoder)
        self._decoders[type_name] = decoder
        return self

    def add_decoders(self, decoders: dict[str, Decoder]) -> "Decoders":
        for type_name, decoder in decoders.items():
            self._validate(type_name, decoder)
        self._decoders.update(decoders)
        return self

    def merge(self, other: "Decoders") -> "Decoders":
        self.add_decoders(other._decoders)  # noqa: SLF001
        return self

    def __contains__(self, type_name: str) -> bool:
        return type_name in self._decoders

    def types(self) -> list[str]:
        return list(self._decoders.keys())

    def _validate(self, type_name: str, decoder: Decoder) -> None:
        if type_name in self._decoders and self._decoders[type_name] is not decoder:
            raise ValueError(
                f"ERROR. decoder for [{type_name}] is already present as [{self._decoders[type_name]}]"
            )

    @classmethod
    def from_objects(
        cls,
        objs: Optional[list[Any]] = None,
        message_payload_discriminator: Optional[Type[MessageDiscriminator]] = None,
        extractors: Optional[Sequence[OneDecoderExtractor]] = None,
    ) -> "Decoders":
        items = {}
        if objs is not None:
            if extractors is None:
                extractors = [OneDecoderExtractor(), MakerExtractor()]
            for obj in objs:
                for extractor in extractors:
                    item = extractor.extract(obj)
                    if item is not None:
                        items[item.type_name] = item.decoder
                        break
        d = Decoders(items)
        d.add_decoder(
            Message.type_name(), MessageDecoder(d, message_payload_discriminator)
        )
        return d


class MQTTCodec(abc.ABC):
    ENCODING = "utf-8"
    decoders: Decoders

    def __init__(self, decoders: Decoders) -> None:
        self.decoders = Decoders().merge(decoders)
        super().__init__()

    def encode(self, content: bytes | BaseModel) -> bytes:
        if isinstance(content, bytes):
            encoded = content
        else:
            encoded = content.model_dump_json()
            if not isinstance(encoded, bytes):
                encoded = encoded.encode(self.ENCODING)
        return encoded

    def decode(self, topic: str, payload: bytes) -> Any:
        decoded_topic = MQTTTopic.decode(topic)
        if decoded_topic.envelope_type not in self.decoders:
            raise ValueError(
                f"Type {decoded_topic.envelope_type} not recognized. Available decoders: {self.decoders.types()}"
            )
        self.validate_source_alias(decoded_topic.src)
        return self.decoders.decode_str(
            decoded_topic.envelope_type, payload, encoding=self.ENCODING
        )

    @abstractmethod
    def validate_source_alias(self, source_alias: str) -> None: ...


def get_pydantic_literal_type_name(
    o: Any, type_name_field: str = DEFAULT_TYPE_NAME_FIELD
) -> str:
    if (
        hasattr(o, "model_fields")
        and type_name_field in o.model_fields
        and get_origin(o.model_fields[type_name_field].annotation) == Literal
    ):
        return str(o.model_fields[type_name_field].default)
    return ""


def pydantic_named_types(  # noqa: C901
    module_names: str | Sequence[str],
    modules: Optional[Sequence[Any]] = None,
    type_name_field: str = DEFAULT_TYPE_NAME_FIELD,
    type_name_regex: Optional[re.Pattern] = None,
    excluded_type_names: Optional[set[str]] = None,
) -> list[Any]:
    if excluded_type_names is None:
        excluded_type_names = DEFAULT_EXCLUDED_TYPE_NAMES
    if isinstance(module_names, str):
        module_names = [module_names] if module_names else []
    if unimported := [
        module_name for module_name in module_names if module_name not in sys.modules
    ]:
        raise ValueError(f"ERROR. modules {unimported} have not been imported.")
    named_types = []
    accumulated_types: dict[str, Any] = {}
    if modules is None:
        modules = []
    for module in [sys.modules[module_name] for module_name in module_names] + list(
        modules
    ):
        module_classes = [
            entry[1] for entry in inspect.getmembers(module, inspect.isclass)
        ]
        for module_class in module_classes:
            if type_name := get_pydantic_literal_type_name(
                module_class, type_name_field=type_name_field
            ):
                if type_name in excluded_type_names:
                    continue
                if type_name in accumulated_types:
                    if accumulated_types[type_name] is module_class:
                        continue
                    raise ValueError(
                        f"ERROR {type_name_field} ({type_name}) "
                        f"for {module_class} already seen for "
                        f"class {accumulated_types[type_name]}"
                    )
                if type_name_regex is not None and not type_name_regex.match(type_name):
                    continue
                accumulated_types[type_name] = module_class
                named_types.append(module_class)
    return named_types


def create_message_payload_discriminator(  # noqa: PLR0913, PLR0917, RUF100
    model_name: str,
    module_names: str | Sequence[str] = "",
    modules: Optional[Sequence[Any]] = None,
    explicit_types: Optional[Sequence[Any]] = None,
    type_name_field: str = DEFAULT_TYPE_NAME_FIELD,
    type_name_regex: Optional[re.Pattern] = None,
    excluded_type_names: Optional[set[str]] = None,
) -> Type[MessageDiscriminator]:
    used_types = pydantic_named_types(
        module_names=module_names,
        modules=modules,
        type_name_field=type_name_field,
        type_name_regex=type_name_regex,
        excluded_type_names=excluded_type_names,
    )
    if explicit_types is not None:
        used_types.extend(explicit_types)
    return create_model(
        model_name,
        __base__=Message,
        Payload=(
            Union[tuple(used_types)],
            Field(..., discriminator=type_name_field),
        ),
    )


def create_discriminator(  # noqa: PLR0913, PLR0917, RUF100
    model_name: str,
    module_names: str | Sequence[str] = "",
    modules: Optional[Sequence[Any]] = None,
    explicit_types: Optional[Sequence[Any]] = None,
    type_name_field: str = DEFAULT_TYPE_NAME_FIELD,
    type_name_regex: Optional[re.Pattern] = None,
    payload_field_name: str = DEFAULT_PAYLOAD_FIELD,
    excluded_type_names: Optional[set[str]] = None,
) -> BaseModel:
    used_types = pydantic_named_types(
        module_names=module_names,
        modules=modules,
        type_name_field=type_name_field,
        type_name_regex=type_name_regex,
        excluded_type_names=excluded_type_names,
    )
    if explicit_types is not None:
        used_types.extend(explicit_types)
    if len(used_types) == 1:
        payload_field_type = (
            used_types[0],
            Field(...),
        )
    else:
        payload_field_type = (
            Union[tuple(used_types)],
            Field(..., discriminator=type_name_field),
        )
    return create_model(model_name, **{payload_field_name: payload_field_type})


class PydanticTypeNameDecoder(Decoder):
    loader: BaseModel
    payload_field_name: str
    contains: set[str]

    def __init__(  # noqa: PLR0913
        self,
        model_name: str,
        *,
        module_names: str | Sequence[str] = "",
        modules: Optional[Sequence[Any]] = None,
        explicit_types: Optional[Sequence[Any]] = None,
        type_name_field: str = DEFAULT_TYPE_NAME_FIELD,
        type_name_regex: Optional[re.Pattern] = None,
        payload_field_name: str = "Payload",
    ) -> None:
        self.payload_field_name = payload_field_name
        self.loader = create_discriminator(
            model_name=model_name,
            module_names=module_names,
            modules=modules,
            explicit_types=explicit_types,
            type_name_field=type_name_field,
            type_name_regex=type_name_regex,
            payload_field_name=payload_field_name,
        )
        payload_field_annotation = self.loader.model_fields[
            self.payload_field_name
        ].annotation
        if payload_field_annotation is None:
            raise ValueError(
                f"ERROR. Payload field <{payload_field_name}> has no annotation"
            )
        self.contains = {
            payload_type.model_fields["TypeName"].default
            for payload_type in typing.get_args(payload_field_annotation)
        }

    def __contains__(self, type_name: str) -> bool:
        return type_name in self.contains

    def decode_obj(self, data: dict) -> BaseModel:
        return getattr(
            self.loader.model_validate({self.payload_field_name: data}),
            self.payload_field_name,
        )
