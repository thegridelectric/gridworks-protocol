# ruff: noqa: ANN401

import abc
import inspect
import re
import sys
from abc import abstractmethod
from collections.abc import Sequence
from types import ModuleType  # noqa
from typing import (
    Any,
    Generic,
    Literal,
    Optional,
    TypeVar,
    Union,
    get_origin,
)

from gw.errors import GwTypeError
from gw.named_types import GwBase
from pydantic import BaseModel, Field, ValidationError, create_model

from gwproto.message import Message
from gwproto.messages import AnyEvent
from gwproto.named_types import ComponentAttributeClassGt, ComponentGt
from gwproto.topic import MQTTTopic

TYPE_NAME_FIELD: str = "type_name"
EXCLUDED_TYPE_NAMES: set[str] = {Message.type_name_value()}  # gw


def get_candidate_modules(
    module_names: str | Sequence[str],
    modules: Optional[Sequence[Any]] = None,
) -> Sequence[ModuleType]:
    if isinstance(module_names, str):
        module_names = [module_names] if module_names else []
    if unimported := [
        module_name for module_name in module_names if module_name not in sys.modules
    ]:
        raise ValueError(f"ERROR. modules {unimported} have not been imported.")
    if modules is None:
        modules = []
    return [sys.modules[module_name] for module_name in module_names] + list(modules)


def get_candidate_gwbase_classes(
    module: ModuleType,
) -> Sequence[tuple[str, type[GwBase]]]:
    """From a given module, return list of (type_name, class) tuples for each
    object in the module that:
        * Is a class
        * Inherits from GwBase
        * Has a type_name field or type_name_value() method
        * type_name is not in EXCLUDED_TYPE_NAMES
    """
    candidates = []
    for _, obj in inspect.getmembers(module, inspect.isclass):
        if issubclass(obj, GwBase) and obj is not GwBase:
            # Try to get type_name
            type_name = None
            if hasattr(obj, "type_name_value"):
                type_name = obj.type_name_value()
            elif TYPE_NAME_FIELD in obj.model_fields:
                field = obj.model_fields[TYPE_NAME_FIELD]
                if get_origin(field.annotation) == Literal:
                    type_name = str(field.default)

            if type_name and type_name not in EXCLUDED_TYPE_NAMES:
                candidates.append((type_name, obj))

    return candidates


def named_types(
    module_names: str | Sequence[str] = "",
    modules: Optional[Sequence[Any]] = None,
    type_name_regex: Optional[re.Pattern[str]] = None,
) -> list[type[GwBase]]:
    """Find all GwBase types with type_name fields."""
    found_types = []
    accumulated_types: dict[str, type[GwBase]] = {}

    for module in get_candidate_modules(module_names, modules):
        for type_name, candidate_class in get_candidate_gwbase_classes(module):
            if (
                type_name in accumulated_types
                and accumulated_types[type_name] is not candidate_class
            ):
                raise ValueError(
                    f"ERROR type_name ({type_name}) "
                    f"for {candidate_class} already seen for "
                    f"class {accumulated_types[type_name]}"
                )
            if type_name_regex is None or type_name_regex.match(type_name):
                accumulated_types[type_name] = candidate_class
                found_types.append(candidate_class)

    return found_types


class MessageDecoder:
    """Decoder for Message types that handles payload discrimination"""

    def __init__(
        self,
        model_name: str,
        module_names: str | Sequence[str] = "",
        modules: Optional[Sequence[Any]] = None,
        explicit_types: Optional[Sequence[Any]] = None,
        type_name_regex: Optional[re.Pattern[str]] = None,
    ) -> None:
        self.model_name = model_name
        self.payload_types = self._get_payload_types(
            module_names, modules, explicit_types, type_name_regex
        )
        # Create a mapping from type_name to class for fast lookup
        self.type_name_to_class = self._build_type_name_mapping(self.payload_types)

    def _build_type_name_mapping(
        self, payload_types: list[type[GwBase]]
    ) -> dict[str, type[GwBase]]:
        """Build mapping from type_name to class, checking for duplicates"""
        type_name_to_class = {}
        for cls in payload_types:
            # Get the type_name for this class
            type_name = None
            if hasattr(cls, "type_name_value"):
                type_name = cls.type_name_value()
            elif TYPE_NAME_FIELD in cls.model_fields:
                field = cls.model_fields[TYPE_NAME_FIELD]
                if get_origin(field.annotation) == Literal:
                    type_name = str(field.default)

            if type_name:
                # Check for duplicates
                if (
                    type_name in type_name_to_class
                    and type_name_to_class[type_name] is not cls
                ):
                    raise ValueError(
                        f"ERROR: type_name '{type_name}' used by multiple classes: "
                        f"{type_name_to_class[type_name]} and {cls}"
                    )
                type_name_to_class[type_name] = cls

        return type_name_to_class

    def _get_payload_types(
        self,
        module_names: str | Sequence[str],
        modules: Optional[Sequence[Any]],
        explicit_types: Optional[Sequence[Any]],
        type_name_regex: Optional[re.Pattern[str]],
    ) -> list[type[GwBase]]:
        """Get all GwBase types that can be used as payloads"""
        types = named_types(
            module_names=module_names,
            modules=modules,
            type_name_regex=type_name_regex,
        )
        if explicit_types:
            types.extend(explicit_types)
        return types

    def decode_payload(self, payload_dict: dict[str, Any]) -> GwBase:
        """Decode a payload dict to the appropriate GwBase type"""
        type_name = payload_dict.get("TypeName", payload_dict.get("type_name"))
        if not type_name:
            raise ValueError("Payload missing TypeName/type_name field")

        payload_class = self.type_name_to_class.get(type_name)
        if not payload_class:
            # Handle unrecognized event types
            if type_name.startswith("gridworks.event"):
                return AnyEvent.from_dict(payload_dict)
            raise ValueError(f"Unknown payload type: {type_name}")

        return payload_class.from_dict(payload_dict)

    def decode_message(self, message_dict: dict[str, Any]) -> Message[Any]:
        """Decode a full message dict"""
        # Extract payload dict
        payload_dict = message_dict.get("Payload", message_dict.get("payload"))
        if not payload_dict:
            raise ValueError("Message missing Payload/payload field")

        # Decode the payload
        payload = self.decode_payload(payload_dict)

        # Extract header if present
        header_dict = message_dict.get("Header", message_dict.get("header"))

        # Create the Message with the decoded payload
        return Message(payload=payload, header=header_dict)


class MQTTCodec(abc.ABC):
    ENCODING = "utf-8"
    message_decoder: MessageDecoder

    def __init__(
        self, message_decoder: Optional[MessageDecoder] = None, **decoder_kwargs: Any
    ) -> None:
        if message_decoder is None:
            # Create a default decoder with provided kwargs
            message_decoder = MessageDecoder(
                model_name=f"{self.__class__.__name__}Decoder", **decoder_kwargs
            )
        self.message_decoder = message_decoder

    def encode(self, content: bytes | GwBase) -> bytes:
        return content if isinstance(content, bytes) else content.to_type()

    def decode(self, topic: str, payload: bytes) -> Message[Any]:
        self.validate_topic(topic)

        # Parse the JSON payload
        import json

        payload_str = (
            payload.decode(self.ENCODING) if isinstance(payload, bytes) else payload
        )
        message_dict = json.loads(payload_str)

        try:
            # Use our custom decoder
            message = self.message_decoder.decode_message(message_dict)
        except (ValueError, ValidationError, GwTypeError) as e:
            # Try to handle as an unrecognized event
            if self._is_unrecognized_event(message_dict):
                payload_dict = message_dict.get(
                    "Payload", message_dict.get("payload", {})
                )
                event_payload = AnyEvent.from_dict(payload_dict)
                message = Message(payload=event_payload)
            else:
                raise ValueError(f"Trouble decoding! {e}")

        return message

    def _is_unrecognized_event(self, message_dict: dict[str, Any]) -> bool:
        """Check if this might be an unrecognized event type"""
        payload_dict = message_dict.get("Payload", message_dict.get("payload", {}))
        type_name = payload_dict.get("TypeName", payload_dict.get("type_name", ""))
        return type_name.startswith("gridworks.event")

    def validate_topic(self, topic: str) -> None:
        decoded_topic = MQTTTopic.decode(topic)
        if decoded_topic.envelope_type != Message.type_name_value():
            raise ValueError(
                f"Type {decoded_topic.envelope_type} not recognized. "
                f"Expected: {Message.type_name_value()}"
            )
        self.validate_source_and_destination(decoded_topic.src, decoded_topic.dst)

    @abstractmethod
    def validate_source_and_destination(self, src: str, dst: str) -> None: ...


def get_model_type_name(cls: Any) -> str:
    """Return cls.TypeName, if cls inherits from BaseModel, has a TypeName field,
    and that field is a Literal, else returns an empty string.
    """
    if (
        issubclass(cls, BaseModel)
        and TYPE_NAME_FIELD in cls.model_fields
        and get_origin(cls.model_fields[TYPE_NAME_FIELD].annotation) == Literal
    ):
        return str(cls.model_fields[TYPE_NAME_FIELD].default)
    return ""


def get_candidate_payload_classes(
    module: ModuleType,
) -> Sequence[tuple[str, type[BaseModel]]]:
    """From a given module, return list of (TypeName, class) tuples for each
    object in the module that:
        * Is a class
        * Is or inherits from BaseModel
        * Has a TypeName which is a Literal with a value.
        * TypeName is not in EXCLUDED_TYPE_NAMES, which can happen if the class
          is a refinement of Message (e.g. PingMessage).
    """
    return [
        (str(module_class.model_fields[TYPE_NAME_FIELD].default), module_class)
        for _, module_class in inspect.getmembers(module, inspect.isclass)
        if (
            issubclass(module_class, BaseModel)
            and TYPE_NAME_FIELD in module_class.model_fields
            and get_origin(module_class.model_fields[TYPE_NAME_FIELD].annotation)
            == Literal
            and len(str(module_class.model_fields[TYPE_NAME_FIELD].default)) > 0
            and str(module_class.model_fields[TYPE_NAME_FIELD].default)
            not in EXCLUDED_TYPE_NAMES
        )
    ]


def include_candidate_class(
    type_name: str,
    candidate_class: type[BaseModel],
    accumulated_types: dict[str, type[BaseModel]],
    type_name_regex: Optional[re.Pattern[str]],
) -> bool:
    if (
        type_name not in EXCLUDED_TYPE_NAMES
        and type_name in accumulated_types
        and accumulated_types[type_name] is not candidate_class
    ):
        raise ValueError(
            f"ERROR {TYPE_NAME_FIELD} ({type_name}) "
            f"for {candidate_class} already seen for "
            f"class {accumulated_types[type_name]}"
        )
    return not (type_name_regex is not None and not type_name_regex.match(type_name))


def pydantic_named_types(
    module_names: str | Sequence[str],
    modules: Optional[Sequence[Any]] = None,
    type_name_regex: Optional[re.Pattern[str]] = None,
) -> list[Any]:
    """Find Pyantic BaseModels with Literal 'TypeName' fields."""
    named_types = []
    accumulated_types: dict[str, Any] = {}
    for module in get_candidate_modules(module_names, modules):
        for type_name, candidate_class in get_candidate_payload_classes(module):
            if (
                type_name in accumulated_types
                and accumulated_types[type_name] is not candidate_class
            ):
                raise ValueError(
                    f"ERROR {TYPE_NAME_FIELD} ({type_name}) "
                    f"for {candidate_class} already seen for "
                    f"class {accumulated_types[type_name]}"
                )
            if type_name_regex is None or type_name_regex.match(type_name):
                accumulated_types[type_name] = candidate_class
                named_types.append(candidate_class)
    return named_types


def create_message_model(
    model_name: str,
    module_names: str | Sequence[str] = "",
    modules: Optional[Sequence[Any]] = None,
    explicit_types: Optional[Sequence[Any]] = None,
    type_name_regex: Optional[re.Pattern[str]] = None,
) -> type[Message[Any]]:
    used_types = pydantic_named_types(
        module_names=module_names,
        modules=modules,
        type_name_regex=type_name_regex,
    )
    if explicit_types is not None:
        used_types.extend(explicit_types)
    return create_model(
        model_name,
        __base__=Message,
        Payload=(
            Union[tuple(used_types)],
            Field(..., discriminator=TYPE_NAME_FIELD),
        ),
    )


WrappedT = TypeVar("WrappedT")


class UnionWrapper(BaseModel, Generic[WrappedT]):
    """A utility class suitable for decoding a from union of types. In order
    to treat input as a union of types, Pydantic requires that our union be in
    named field, which by convention we call "Wrapped".
    """

    Wrapped: WrappedT

    @classmethod
    def create(
        cls,
        model_name: str,
        *,
        module_names: str | Sequence[str] = "",
        modules: Optional[Sequence[Any]] = None,
        explicit_types: Optional[Sequence[Any]] = None,
        type_name_regex: Optional[re.Pattern[str]] = None,
    ) -> type["UnionWrapper[WrappedT]"]:
        """Create pydantic model that is a union of all appropriate types found via
        module_names, modules and explicit_types"""
        used_types = pydantic_named_types(
            module_names=module_names,
            modules=modules,
            type_name_regex=type_name_regex,
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
                Field(..., discriminator=TYPE_NAME_FIELD),
            )
        # Pydantic requires us to put our discriminated union in a named field.
        # We use the name 'Wrapped'.
        return create_model(
            model_name, __base__=UnionWrapper, Wrapped=payload_field_type
        )


class UnionDecoder:
    """A Utility base class for decoding from a union of types."""

    loader: type[UnionWrapper[Any]]

    def __init__(
        self,
        model_name: str,
        *,
        module_names: str | Sequence[str] = "",
        modules: Optional[Sequence[Any]] = None,
        explicit_types: Optional[Sequence[Any]] = None,
        type_name_regex: Optional[re.Pattern[str]] = None,
    ) -> None:
        self.loader = UnionWrapper.create(
            model_name=model_name,
            module_names=module_names,
            modules=modules,
            explicit_types=explicit_types,
            type_name_regex=type_name_regex,
        )


class CacDecoder(UnionDecoder):
    TYPE_NAME_REGEX = re.compile(r".*\.cac\.gt")
    loader: type[UnionWrapper[Any]]

    def __init__(
        self,
        model_name: str,
        type_name_regex: Optional[re.Pattern[str]] = TYPE_NAME_REGEX,
        **kwargs: Any,
    ) -> None:
        super().__init__(model_name, type_name_regex=type_name_regex, **kwargs)

    def decode(
        self, cac_dict: dict[str, Any], *, allow_missing: bool = True
    ) -> ComponentAttributeClassGt:
        decoded: ComponentAttributeClassGt
        try:
            decoded = self.loader.model_validate({"Wrapped": cac_dict}).Wrapped
            if not isinstance(decoded, ComponentAttributeClassGt):
                raise TypeError(
                    f"ERROR. CacDecoder decoded type {type(decoded)}, "
                    "not ComponentAttributeClassGt"
                )
        except ValidationError as e:
            if allow_missing and any(
                error.get("type") == "union_tag_invalid" for error in e.errors()
            ):
                decoded = ComponentAttributeClassGt(**cac_dict)
            else:
                raise
        return decoded


class ComponentDecoder(UnionDecoder):
    TYPE_NAME_REGEX = re.compile(r".*\.?component\.gt")

    def __init__(
        self,
        model_name: str,
        type_name_regex: Optional[re.Pattern[str]] = TYPE_NAME_REGEX,
        **kwargs: Any,
    ) -> None:
        super().__init__(model_name, type_name_regex=type_name_regex, **kwargs)

    def decode(
        self, component_dict: dict[str, Any], *, allow_missing: bool = True
    ) -> ComponentGt:
        decoded: ComponentGt
        try:
            # Pydantic requires that our union of types (components here) be in
            # a named field, which by convention we call "Wrapped".
            decoded = self.loader.model_validate({"Wrapped": component_dict}).Wrapped
            if not isinstance(decoded, ComponentGt):
                raise TypeError(
                    f"ERROR. ComponentDecoder decoded type {type(decoded)}, "
                    "not ComponentGt"
                )
        except ValidationError as e:
            if allow_missing and any(
                error.get("type") == "union_tag_invalid" for error in e.errors()
            ):
                decoded = ComponentGt(**component_dict)
            else:
                raise
        return decoded
