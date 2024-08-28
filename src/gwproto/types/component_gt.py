"""Type component.gt, version 001"""

import json
import logging
import os
from typing import Any, Dict, List, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, ConfigDict, Field, field_validator

from gwproto.data_classes.component import Component
from gwproto.types.channel_config import ChannelConfig, ChannelConfigMaker

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class ComponentGt(BaseModel):
    """
    Component Gt.

    Authority for the attributes of the component.gt.000 (ComponentId, ComponentAttributeClassId,
    DisplayName, HwUid) belongs to the WorldRegistry. The WorldRegistry is part of the GridWorks
    'BackOffice' structure for managing relational device data . Notably, ComponentId and ComponentAttributeClass
    are both required and immutable. HwUid is optional but once it is set to a non-null value
    that is also immutable - it is meant to be an immutable identifier associated to a specific
    physical device, ideally one that can be read remotely by the SCADA and also by the naked
    eye. The DisplayName is mutable, with its current value in time governed by the WorldRegistry.
    Reference updated cac 001, which has optional MakeModel and min poll period. Also allow
    extra.

    [More info](https://g-node-registry.readthedocs.io/en/latest/component.html)
    """

    component_id: str = Field(
        title="ComponentId",
        description="Immutable unique identifier for this specific device.",
    )
    component_attribute_class_id: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class. Authority for these, as well as the relationship "
            "between Components and ComponentAttributeClasses (Cacs) is maintained by the World "
            "Registry."
        ),
    )
    config_list: List[ChannelConfig] = Field(
        title="ConfigList",
        description=(
            "This list is expected to have length 0, except for nodes that do some kind of sensing "
            "- in which case it includes the information re timing of data polling and capture "
            "for the channels read by the node."
        ),
    )
    display_name: Optional[str] = Field(
        title="Display Name",
        description=(
            "This is an optional, mutable field whose use is strongly encouraged. It may include "
            "information about HOW the component is used in a hardware layout. It may also include "
            "the HwUid for the component."
        ),
        default=None,
    )
    hw_uid: Optional[str] = Field(
        title="Hardware Unique Id",
        description="Usually this is determined by the inheriting class.",
        default=None,
    )
    type_name: Literal["component.gt"] = "component.gt"
    version: Literal["001"] = "001"
    model_config = ConfigDict(
        extra="allow", populate_by_name=True, alias_generator=snake_to_pascal
    )

    @field_validator("component_id")
    @classmethod
    def _check_component_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentId failed UuidCanonicalTextual format validation: {e}",
            ) from e
        return v

    @field_validator("component_attribute_class_id")
    @classmethod
    def _check_component_attribute_class_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentAttributeClassId failed UuidCanonicalTextual format validation: {e}",
            ) from e
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Main step in serializing the object. Encodes enums as their 8-digit random hex symbol if
        settings.encode_enums = 1.
        """
        if ENCODE_ENUMS:
            return self.enum_encoded_dict()
        else:
            return self.plain_enum_dict()

    def plain_enum_dict(self) -> Dict[str, Any]:
        """
        Returns enums as their values.
        """
        d = {
            snake_to_pascal(key): value
            for key, value in self.model_dump().items()
            if value is not None
        }
        # Recursively calling as_dict()
        config_list = []
        for elt in self.config_list:
            config_list.append(elt.as_dict())
        d["ConfigList"] = config_list
        return d

    def enum_encoded_dict(self) -> Dict[str, Any]:
        """
        Encodes enums as their 8-digit random hex symbol
        """
        d = {
            snake_to_pascal(key): value
            for key, value in self.model_dump().items()
            if value is not None
        }
        # Recursively calling as_dict()
        config_list = []
        for elt in self.config_list:
            config_list.append(elt.as_dict())
        d["ConfigList"] = config_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the component.gt.001 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ComponentGtMaker:
    type_name = "component.gt"
    version = "001"

    @classmethod
    def tuple_to_type(cls, tuple: ComponentGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> ComponentGt:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a component.gt.001 type

        Returns:
            ComponentGt instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ComponentGt:
        """
        Translates a dict representation of a component.gt.001 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "ComponentId" not in d2.keys():
            raise GwTypeError(f"dict missing ComponentId: <{d2}>")
        if "ComponentAttributeClassId" not in d2.keys():
            raise GwTypeError(f"dict missing ComponentAttributeClass: <{d2}>")
        if "ConfigList" not in d2.keys():
            raise GwTypeError(f"dict missing ConfigList: <{d2}>")
        if not isinstance(d2["ConfigList"], List):
            raise GwTypeError(f"ConfigList <{d2['ConfigList']}> must be a List!")
        config_list = []
        for elt in d2["ConfigList"]:
            if not isinstance(elt, dict):
                raise GwTypeError(
                    f"ConfigList <{d2['ConfigList']}> must be a List of ChannelConfig types"
                )
            t = ChannelConfigMaker.dict_to_tuple(elt)
            config_list.append(t)
        d2["ConfigList"] = config_list
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret component.gt version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return ComponentGt(**d3)

    @classmethod
    def tuple_to_dc(cls, t: ComponentGt) -> Component:
        if t.component_id in Component.by_id.keys():
            dc = Component.by_id[t.component_id]
        else:
            dc = Component(
                component_id=t.component_id,
                component_attribute_class_id=t.component_attribute_class_id,
                config_list=t.config_list,
                display_name=t.display_name,
                hw_uid=t.hw_uid,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: Component) -> ComponentGt:
        return ComponentGt(
            component_id=dc.component_id,
            component_attribute_class_id=dc.component_attribute_class_id,
            config_list=dc.config_list,
            display_name=dc.display_name,
            hw_uid=dc.hw_uid,
        )

    @classmethod
    def type_to_dc(cls, t: str) -> Component:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: Component) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> Component:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))


def check_is_uuid_canonical_textual(v: str) -> None:
    """Checks UuidCanonicalTextual format

    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not UuidCanonicalTextual format
    """
    phi_fun_check_it_out = 5
    two_cubed_too_cute = 8
    bachets_fun_four = 4
    the_sublime_twelve = 12
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}") from e
    if len(x) != phi_fun_check_it_out:
        raise ValueError(f"<{v}> split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError as e:
            raise ValueError(f"Words of <{v}> are not all hex") from e
    if len(x[0]) != two_cubed_too_cute:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[1]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[2]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[3]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[4]) != the_sublime_twelve:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
