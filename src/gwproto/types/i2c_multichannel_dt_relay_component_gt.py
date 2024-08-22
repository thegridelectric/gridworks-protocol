"""Type i2c.multichannel.dt.relay.component.gt, version 000"""

import json
import logging
import os
from typing import Any, Dict, List, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import ConfigDict, Field, field_validator

from gwproto.data_classes.components.i2c_multichannel_dt_relay_component import (
    I2cMultichannelDtRelayComponent,
)
from gwproto.types import ComponentGt
from gwproto.types.channel_config import ChannelConfig, ChannelConfigMaker
from gwproto.types.relay_actor_config import RelayActorConfig, RelayActorConfigMaker

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class I2cMultichannelDtRelayComponentGt(ComponentGt):
    """
    I2c Multichannel Double Throw Relay Component.

    A specific instance of a board with multiple double-throw electromechanical relays. The
    board is expected to be addressable over i2c, with that address being configurable to a
    finite number of choices via dipswitches.
    """

    component_id: str = Field(
        title="Component Id",
        description=(
            "Primary GridWorks identifier for a specific physical instance of a Relay, and also "
            "as a more generic Component."
        ),
    )
    component_attribute_class_id: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class. Authority for these, as well as the relationship "
            "between Components and ComponentAttributeClasses (Cacs) is maintained by the World "
            "Registry."
        ),
    )
    i2c_address_list: List[int] = Field(
        title="I2c Address List",
        description="An ordered list of the I2c Addresses for the boards.",
    )
    config_list: List[ChannelConfig] = Field(
        title="Channel Config List",
        description=(
            "A list of the ChannelConfigs for the data channels reported by the actors associated "
            "to this component's relays (actors specified in the RelayConfigLlist)"
        ),
    )
    relay_config_list: List[RelayActorConfig] = Field(
        title="Relay Config List",
        description=(
            "Information about which actors control each relay, and the relay wiring state: (normally "
            "open, normally closed, double throw)."
        ),
    )
    display_name: Optional[str] = Field(
        title="DisplayName",
        default=None,
    )
    hw_uid: Optional[str] = Field(
        title="Hardware Unique Id",
        default=None,
    )
    type_name: Literal["i2c.multichannel.dt.relay.component.gt"] = (
        "i2c.multichannel.dt.relay.component.gt"
    )
    version: Literal["000"] = "000"
    model_config = ConfigDict(populate_by_name=True, alias_generator=snake_to_pascal)

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

    @field_validator("config_list")
    @classmethod
    def check_config_list(cls, v: List[ChannelConfig]) -> List[ChannelConfig]:
        """
        Axiom 1: Channel Consistency.
        There are no duplicates of ChannelName in the ConfigList
        """
        ...
        # TODO: Implement Axiom(s)
        return v

    @field_validator("relay_config_list")
    @classmethod
    def check_relay_config_list(
        cls, v: List[RelayActorConfig]
    ) -> List[RelayActorConfig]:
        """
        Axiom 2: Actor and Idx Consistency.
        There are no duplicates of ActorName or RelayIdx in the RelayConfigList
        """
        ...
        # TODO: Implement Axiom(s)
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
        # Recursively calling as_dict()
        relay_config_list = []
        for elt in self.relay_config_list:
            relay_config_list.append(elt.as_dict())
        d["RelayConfigList"] = relay_config_list
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
        # Recursively calling as_dict()
        relay_config_list = []
        for elt in self.relay_config_list:
            relay_config_list.append(elt.as_dict())
        d["RelayConfigList"] = relay_config_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the i2c.multichannel.dt.relay.component.gt.000 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class I2cMultichannelDtRelayComponentGtMaker:
    type_name = "i2c.multichannel.dt.relay.component.gt"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: I2cMultichannelDtRelayComponentGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> I2cMultichannelDtRelayComponentGt:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a i2c.multichannel.dt.relay.component.gt.000 type

        Returns:
            I2cMultichannelDtRelayComponentGt instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> I2cMultichannelDtRelayComponentGt:
        """
        Translates a dict representation of a i2c.multichannel.dt.relay.component.gt.000 message object
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
        if "I2cAddressList" not in d2.keys():
            raise GwTypeError(f"dict missing I2cAddressList: <{d2}>")
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
        if "RelayConfigList" not in d2.keys():
            raise GwTypeError(f"dict missing RelayConfigList: <{d2}>")
        if not isinstance(d2["RelayConfigList"], List):
            raise GwTypeError(
                f"RelayConfigList <{d2['RelayConfigList']}> must be a List!"
            )
        relay_config_list = []
        for elt in d2["RelayConfigList"]:
            if not isinstance(elt, dict):
                raise GwTypeError(
                    f"RelayConfigList <{d2['RelayConfigList']}> must be a List of RelayActorConfig types"
                )
            t = RelayActorConfigMaker.dict_to_tuple(elt)
            relay_config_list.append(t)
        d2["RelayConfigList"] = relay_config_list
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret i2c.multichannel.dt.relay.component.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return I2cMultichannelDtRelayComponentGt(**d3)

    @classmethod
    def tuple_to_dc(
        cls, t: I2cMultichannelDtRelayComponentGt
    ) -> I2cMultichannelDtRelayComponent:
        if t.component_id in I2cMultichannelDtRelayComponent.by_id.keys():
            dc = I2cMultichannelDtRelayComponent.by_id[t.component_id]
        else:
            dc = I2cMultichannelDtRelayComponent(
                component_id=t.component_id,
                component_attribute_class_id=t.component_attribute_class_id,
                i2c_address_list=t.i2c_address_list,
                config_list=t.config_list,
                relay_config_list=t.relay_config_list,
                display_name=t.display_name,
                hw_uid=t.hw_uid,
            )
        return dc

    @classmethod
    def dc_to_tuple(
        cls, dc: I2cMultichannelDtRelayComponent
    ) -> I2cMultichannelDtRelayComponentGt:
        return I2cMultichannelDtRelayComponentGt(
            component_id=dc.component_id,
            component_attribute_class_id=dc.component_attribute_class_id,
            i2c_address_list=dc.i2c_address_list,
            config_list=dc.config_list,
            relay_config_list=dc.relay_config_list,
            display_name=dc.display_name,
            hw_uid=dc.hw_uid,
        )

    @classmethod
    def type_to_dc(cls, t: str) -> I2cMultichannelDtRelayComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: I2cMultichannelDtRelayComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> I2cMultichannelDtRelayComponent:
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
