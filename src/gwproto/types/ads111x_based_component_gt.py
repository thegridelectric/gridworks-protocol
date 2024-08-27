"""Type ads111x.based.component.gt, version 000"""

import json
import logging
import os
from typing import Any, Dict, List, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import ConfigDict, Field, field_validator, model_validator
from typing_extensions import Self

from gwproto.data_classes.components.ads111x_based_component import (
    Ads111xBasedComponent,
)
from gwproto.types.channel_config import ChannelConfig, ChannelConfigMaker
from gwproto.types.component_gt import ComponentGt
from gwproto.types.thermistor_data_processing_config import (
    ThermistorDataProcessingConfig,
    ThermistorDataProcessingConfigMaker,
)

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class Ads111xBasedComponentGt(ComponentGt):
    """
    TI ADS111x Based Temp Sensing Component.

    Designed for specific instances of a temp sensor based on the Texas Instrument ADS111X series
    of chips used w 10K thermistors for reading temperature.

    [More info](https://drive.google.com/drive/u/0/folders/1oFvs4-kvwyzt220eYlFnwdzEgVCIbbt6)
    """

    component_id: str = Field(
        title="Component Id",
        description=(
            "Primary GridWorks identifier for a specific physical instance of a MultipurposeSensor "
            "(perhaps only the 12-channel analog temp sensor), and also as a more generic Component."
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
    display_name: Optional[str] = Field(
        title="Display Name",
        description="Sample: Oak 16-channel AdsTemp Sensor <100>",
        default=None,
    )
    open_voltage_by_ads: List[float] = Field(
        title="Open Voltage By Ads",
        description=(
            "The voltage reading with no thermistor attached is called the 'open voltage.' It "
            "is close to the power supply voltage (e.g. 5V) , but we have found that there is "
            "non-trivial variation (~0.2 V), and there can even be variation in the average open "
            "voltage in the same installation across different ADS chips (~0.01 or 0.02V). This "
            "list follows the same order as the self.cac.AdsI2cAddressList."
        ),
    )
    config_list: List[ChannelConfig] = Field(
        title="Config List",
        description=(
            "The information re timing of data polling and capture for the channels read by the "
            "node."
        ),
    )
    thermistor_config_list: List[ThermistorDataProcessingConfig] = Field(
        title="Thermistor Config List",
        description=(
            "This includes the list of configuration information needed for data processing and "
            "reporting for the data collected by thermistors - both voltage and (derived) temperature. "
            "It also includes the information about what TYPE of thermistor is used."
        ),
    )
    hw_uid: Optional[str] = Field(
        title="Hardware Unique Id",
        default=None,
    )
    type_name: Literal["ads111x.based.component.gt"] = "ads111x.based.component.gt"
    version: Literal["000"] = "000"
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

    @field_validator("open_voltage_by_ads")
    @classmethod
    def _check_open_voltage_by_ads(cls, v: List[float]) -> List[float]:
        for elt in v:
            try:
                check_is_near5(elt)
            except ValueError as e:
                raise ValueError(
                    f"OpenVoltageByAds element {elt} failed Near5 format validation: {e}",
                ) from e
        return v

    @field_validator("thermistor_config_list")
    @classmethod
    def check_thermistor_config_list(
        cls, v: List[ThermistorDataProcessingConfig]
    ) -> List[ThermistorDataProcessingConfig]:
        """
            Axiom 1: Terminal Block consistency and Channel Name uniqueness..
            Terminal Block consistency and Channel Name uniqueness. - Each TerminalBlockIdx occurs at
        most once in the ThermistorConfigList - Each data channel occurs at most once in the ThermistorConfigList
        """
        terminal_blocks = list(map(lambda x: x.terminal_block_idx, v))
        if len(set(terminal_blocks)) != len(terminal_blocks):
            raise ValueError(
                f"Axiom 1 failed! Terminal block used multiple times in "
                f"ThermistorDataProcessingConfig:\n <{v}>"
            )
        channel_names = list(map(lambda x: x.channel_name, v))
        if len(set(channel_names)) != len(channel_names):
            raise ValueError(
                f"Axiom 1 failed! Channel Name used multiple times in "
                f"ThermistorDataProcessingConfig:\n <{v}>"
            )
        return v

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: ThermistorConfig, ChannelConfig consistency.
        set(map(lambda x: x.ChannelName, ThermistorConfigList)) is equal to
        set(map(lambda x: x.ChannelName, ConfigList))
        """
        therm_names = set(map(lambda x: x.channel_name, self.thermistor_config_list))
        config_names = set(map(lambda x: x.channel_name, self.config_list))
        if therm_names != config_names:
            raise ValueError(
                "Axiom 2 failed! ThermistorConfigList and ConfigList "
                f"do not refer to same channels: <{self}>"
            )
        return self

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
        thermistor_config_list = []
        for elt in self.thermistor_config_list:
            thermistor_config_list.append(elt.as_dict())
        d["ThermistorConfigList"] = thermistor_config_list
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
        thermistor_config_list = []
        for elt in self.thermistor_config_list:
            thermistor_config_list.append(elt.as_dict())
        d["ThermistorConfigList"] = thermistor_config_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the ads111x.based.component.gt.000 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class Ads111xBasedComponentGtMaker:
    type_name = "ads111x.based.component.gt"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: Ads111xBasedComponentGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> Ads111xBasedComponentGt:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a ads111x.based.component.gt.000 type

        Returns:
            Ads111xBasedComponentGt instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> Ads111xBasedComponentGt:
        """
        Translates a dict representation of a ads111x.based.component.gt.000 message object
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
        if "OpenVoltageByAds" not in d2.keys():
            raise GwTypeError(f"dict missing OpenVoltageByAds: <{d2}>")
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
        if "ThermistorConfigList" not in d2.keys():
            raise GwTypeError(f"dict missing ThermistorConfigList: <{d2}>")
        if not isinstance(d2["ThermistorConfigList"], List):
            raise GwTypeError(
                f"ThermistorConfigList <{d2['ThermistorConfigList']}> must be a List!"
            )
        thermistor_config_list = []
        for elt in d2["ThermistorConfigList"]:
            if not isinstance(elt, dict):
                raise GwTypeError(
                    f"ThermistorConfigList <{d2['ThermistorConfigList']}> must be a List of ThermistorDataProcessingConfig types"
                )
            t = ThermistorDataProcessingConfigMaker.dict_to_tuple(elt)
            thermistor_config_list.append(t)
        d2["ThermistorConfigList"] = thermistor_config_list
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret ads111x.based.component.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return Ads111xBasedComponentGt(**d3)

    @classmethod
    def tuple_to_dc(cls, t: Ads111xBasedComponentGt) -> Ads111xBasedComponent:
        if t.component_id in Ads111xBasedComponent.by_id.keys():
            dc = Ads111xBasedComponent.by_id[t.component_id]
        else:
            dc = Ads111xBasedComponent(
                component_id=t.component_id,
                component_attribute_class_id=t.component_attribute_class_id,
                display_name=t.display_name,
                open_voltage_by_ads=t.open_voltage_by_ads,
                config_list=t.config_list,
                thermistor_config_list=t.thermistor_config_list,
                hw_uid=t.hw_uid,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: Ads111xBasedComponent) -> Ads111xBasedComponentGt:
        return Ads111xBasedComponentGt(
            component_id=dc.component_id,
            component_attribute_class_id=dc.component_attribute_class_id,
            display_name=dc.display_name,
            open_voltage_by_ads=dc.open_voltage_by_ads,
            config_list=dc.config_list,
            thermistor_config_list=dc.thermistor_config_list,
            hw_uid=dc.hw_uid,
        )

    @classmethod
    def type_to_dc(cls, t: str) -> Ads111xBasedComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: Ads111xBasedComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> Ads111xBasedComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))


def check_is_ads1115_i2c_address(v: str) -> None:
    """
    Ads1115I2cAddress: ToLower(v) in  ['0x48', '0x49', '0x4a', '0x4b'].

    One of the 4 allowable I2C addresses for Texas Instrument Ads1115 chips.

    Raises:
        ValueError: if not Ads1115I2cAddress format
    """
    if v.lower() not in ["0x48", "0x49", "0x4a", "0x4b"]:
        raise ValueError(f"Not Ads1115I2cAddress: <{v}>")


def check_is_near5(v: str) -> None:
    """
    4.5 <= v <= 5.5
    """
    if v < 4.5 or v > 5.5:
        raise ValueError(f"<{v}> is not between 4.5 and 5.5, not Near5")


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
