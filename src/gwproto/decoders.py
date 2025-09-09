# ruff: noqa: ANN401
import abc
import inspect
import json
import re
import sys
from abc import abstractmethod
from collections.abc import Sequence
from types import ModuleType  # noqa
from typing import (
    Any,
    Literal,
    Optional,
    get_origin,
)

from gw.named_types import GwBase
from pydantic_core import PydanticUndefined

from gwproto.enums import MessageCategory, MessageCategorySymbol
from gwproto.messages import AnyEvent, Message
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
                try:
                    type_name = obj.type_name_value()
                except (AttributeError, TypeError, ValueError):
                    # Skip classes where type_name_value() is not properly implemented
                    continue
            elif TYPE_NAME_FIELD in obj.model_fields:
                field = obj.model_fields[TYPE_NAME_FIELD]
                if get_origin(field.annotation) == Literal:
                    default = field.default
                    # Skip if default is undefined or None
                    if default is not PydanticUndefined and default is not None:
                        type_name = str(default)
            if (
                type_name
                and type_name not in EXCLUDED_TYPE_NAMES
                and type_name != PydanticUndefined
            ):
                candidates.append((type_name, obj))

    return candidates


def named_types(
    module_names: str | Sequence[str] = "",
    modules: Optional[Sequence[Any]] = None,
    type_name_regex: Optional[re.Pattern[str]] = None,
) -> list[type[GwBase]]:
    r"""Find all GwBase types with type_name fields.

    Args:
        module_names: Names of modules to search for GwBase types
        modules: Module objects to search (in addition to module_names)
        type_name_regex: Optional regex pattern to filter type names.
            Only types whose type_name matches this pattern will be included.

    Examples of type_name_regex usage:
        - re.compile(r".*\.component\.gt") - only types ending w component.gt
        - re.compile(r"gridworks\.event\..*") - only event types

    Returns:
        List of GwBase classes found that match the criteria
    """
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
        module_names: str | Sequence[str] = "",
        modules: Optional[Sequence[Any]] = None,
        explicit_types: Optional[Sequence[Any]] = None,
        type_name_regex: Optional[re.Pattern[str]] = None,
    ) -> None:
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


class MQTTCodec(abc.ABC):
    ENCODING = "utf-8"
    message_decoder: MessageDecoder

    def __init__(
        self, message_decoder: Optional[MessageDecoder] = None, **decoder_kwargs: Any
    ) -> None:
        if message_decoder is None:
            # Create a default decoder with provided kwargs
            message_decoder = MessageDecoder(**decoder_kwargs)
        self.message_decoder = message_decoder

    def encode(
        self,
        content: bytes | GwBase | Message,
        message_category: MessageCategory = MessageCategory.ScadaWrapped,
    ) -> bytes:
        if isinstance(content, bytes):
            return content

        if message_category == MessageCategory.ScadaWrapped:
            # For ScadaWrapped, we need the full Message envelope
            if isinstance(content, Message):
                return content.to_type()
            message = Message(payload=content)
            return message.to_type()

        # for JsonDirect and JsonBroadcast, just send the payload
        if isinstance(content, Message):
            return content.payload.to_type()
        return content.to_type()

    def decode(self, topic: str, payload: bytes) -> Message[Any]:
        decoded_topic = MQTTTopic.decode(topic)
        envelope_type = decoded_topic.envelope_type

        if envelope_type == MessageCategorySymbol.gw.value:
            # ScadaWrapped - parse the JSON to get header and payload
            payload_str = (
                payload.decode(MQTTCodec.ENCODING)
                if isinstance(payload, bytes)
                else payload
            )
            message_dict = json.loads(payload_str)

            # Check it's actually a wrapped message
            if message_dict.get("TypeName") != Message.type_name_value():  # (gw)
                raise ValueError(
                    f"Expected TypeName='gw', got {message_dict.get('TypeName')}"
                )

            # Extract and decode the inner payload
            inner_payload_dict = message_dict.get("Payload")
            if not inner_payload_dict:
                raise ValueError("ScadaWrapped message missing Payload field")

            try:
                decoded_payload = self.message_decoder.decode_payload(
                    inner_payload_dict
                )
            except ValueError:
                # Check if its an unrecognized event type
                type_name = inner_payload_dict.get(
                    "TypeName", inner_payload_dict.get("type_name", "")
                )
                if type_name.startswith("gridworks.event"):
                    decoded_payload = AnyEvent.from_dict(inner_payload_dict)
                else:
                    raise  # Re-raise if not an event

            header_dict = message_dict.get("Header")
            message = Message(payload=decoded_payload, header=header_dict)

        elif envelope_type in [MessageCategorySymbol.rj, MessageCategorySymbol.rjb]:
            # Need to parse and wrap in Message
            payload_str = (
                payload.decode(self.ENCODING) if isinstance(payload, bytes) else payload
            )
            payload_dict = json.loads(payload_str)
            decoded_payload = self.message_decoder.decode_payload(payload_dict)
            message = Message(
                payload=decoded_payload, src=decoded_topic.src, dst=decoded_topic.dst
            )
        else:
            raise ValueError(f"Un-parsed envelope type: {envelope_type}")
        return message

    def _is_unrecognized_event(self, message_dict: dict[str, Any]) -> bool:
        """Check if this might be an unrecognized event type"""
        payload_dict = message_dict.get("Payload", message_dict.get("payload", {}))
        type_name = payload_dict.get("TypeName", payload_dict.get("type_name", ""))
        return type_name.startswith("gridworks.event")

    def validate_topic(self, topic: str) -> None:
        """Validate topic structure based on message category"""

        try:
            decoded_topic = MQTTTopic.decode(topic)
        except ValueError as e:
            raise ValueError(f"Invalid topic: {e}")

        self.validate_source_and_destination(decoded_topic.src, decoded_topic.dst)

    @abstractmethod
    def validate_source_and_destination(self, src: str, dst: str) -> None: ...


def create_message_model(
    module_names: str | Sequence[str] = "",
    modules: Optional[Sequence[Any]] = None,
    explicit_types: Optional[Sequence[Any]] = None,
    type_name_regex: Optional[re.Pattern[str]] = None,
) -> MessageDecoder:
    """Create a MessageDecoder instead of a pydantic model"""
    return MessageDecoder(
        module_names=module_names,
        modules=modules,
        explicit_types=explicit_types,
        type_name_regex=type_name_regex,
    )


# Union decoder for GwBase types
class UnionDecoder:
    """A Utility base class for decoding from a union of GwBase types."""

    def __init__(
        self,
        *,
        module_names: str | Sequence[str] = "",
        modules: Optional[Sequence[Any]] = None,
        explicit_types: Optional[Sequence[Any]] = None,
        type_name_regex: Optional[re.Pattern[str]] = None,
    ) -> None:
        self.types = named_types(
            module_names=module_names,
            modules=modules,
            type_name_regex=type_name_regex,
        )
        if explicit_types:
            self.types.extend(explicit_types)

        # Create a mapping from type_name to class for fast lookup
        self.type_name_to_class = {}
        for cls in self.types:
            if hasattr(cls, "type_name_value"):
                type_name = cls.type_name_value()
            elif TYPE_NAME_FIELD in cls.model_fields:
                field = cls.model_fields[TYPE_NAME_FIELD]
                if get_origin(field.annotation) == Literal:
                    type_name = str(field.default)
                else:
                    continue
            else:
                continue
            self.type_name_to_class[type_name] = cls

    def decode(self, data_dict: dict[str, Any]) -> GwBase:
        """Decode a dict to the appropriate GwBase type"""
        type_name = data_dict.get("TypeName", data_dict.get("type_name"))
        if not type_name:
            raise ValueError(f"Missing TypeName/type_name field in {data_dict}")

        cls = self.type_name_to_class.get(type_name)
        if not cls:
            raise ValueError(
                f"Unknown type: {type_name}. Available types: {list(self.type_name_to_class.keys())}"
            )

        return cls.from_dict(data_dict)


class CacDecoder(UnionDecoder):
    TYPE_NAME_REGEX = re.compile(r".*\.cac\.gt")

    def __init__(
        self,
        type_name_regex: Optional[re.Pattern[str]] = TYPE_NAME_REGEX,
        **kwargs: Any,
    ) -> None:
        super().__init__(type_name_regex=type_name_regex, **kwargs)

    def decode(
        self, cac_dict: dict[str, Any], *, allow_missing: bool = True
    ) -> ComponentAttributeClassGt:
        try:
            decoded = super().decode(cac_dict)
            if not isinstance(decoded, ComponentAttributeClassGt):
                raise TypeError(
                    f"ERROR. CacDecoder decoded type {type(decoded)}, "
                    "not ComponentAttributeClassGt"
                )
        except ValueError as e:
            if allow_missing and "Unknown type" in str(e):
                # Fall back to base ComponentAttributeClassGt for unknown types
                fallback_dict = dict(cac_dict)
                fallback_dict["TypeName"] = "component.attribute.class.gt"
                return ComponentAttributeClassGt.from_dict(cac_dict)
            raise
        else:
            return decoded


class ComponentDecoder(UnionDecoder):
    TYPE_NAME_REGEX = re.compile(r".*\.?component\.gt")

    def __init__(
        self,
        type_name_regex: Optional[re.Pattern[str]] = TYPE_NAME_REGEX,
        **kwargs: Any,
    ) -> None:
        super().__init__(type_name_regex=type_name_regex, **kwargs)

    def decode(
        self, component_dict: dict[str, Any], *, allow_missing: bool = True
    ) -> ComponentGt:
        try:
            decoded = super().decode(component_dict)
            if not isinstance(decoded, ComponentGt):
                raise TypeError(
                    f"ERROR. ComponentDecoder decoded type {type(decoded)}, "
                    "not ComponentGt"
                )
        except ValueError as e:
            if allow_missing and "Unknown type" in str(e):
                # Fall back to base ComponentGt for unknown types
                # Need to override TypeName to match ComponentGt's expectation
                fallback_dict = dict(component_dict)
                fallback_dict["TypeName"] = "component.gt"
                return ComponentGt.from_dict(fallback_dict)
            raise
        else:
            return decoded
