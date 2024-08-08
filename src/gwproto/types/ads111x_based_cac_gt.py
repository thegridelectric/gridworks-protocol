"""Type ads111x.based.cac.gt, version 000"""

import json
import logging
import os
from typing import Any, Dict, List, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import Field, field_validator, model_validator
from typing_extensions import Self

from gwproto.data_classes.cacs.ads111x_based_cac import Ads111xBasedCac
from gwproto.enums import MakeModel, TelemetryName
from gwproto.types.component_attribute_class_gt import (
    ComponentAttributeClassGt as CacGt,
)

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class Ads111xBasedCacGt(CacGt):
    """
    TI ADS111x Based Temp Sensing Component Attribute Class.

    Component Attribute Class for sensors using the Texas Instrument ADS111X series of chips
    used with 10K thermistors for reading temperature. The ADS111X is a class of I2C-based 16-bit
    Analog Digital Convertors. The chip has 4 possible I2C addresses, and the address can be
    set by jumpering the 'Addr' pin of the ADS111X chip to one of the 4 I2C pins. 0x48: GND,
    0x49: VDD, 0x4A: SDA, 0x4B: SCL. GridWorks Spaceheat SCADA uses the GridWorks GNodeRegistry
    structures and abstractions for managing relational device data. The Cac, or ComponentAttributeClass,
    is part of this structure.

    [More info](https://drive.google.com/drive/u/0/folders/1oFvs4-kvwyzt220eYlFnwdzEgVCIbbt6)
    """

    component_attribute_class_id: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class (aka 'cac' or Component Attribute Class). "
            "Authority is maintained by the World Registry."
        ),
    )
    min_poll_period_ms: int = Field(
        title="Min Poll Period in Milliseconds",
        description=(
            "Poll Period refers to the period of time between two readings by the local actor. "
            "This is in contrast to Capture Period, which refers to the period between readings "
            "that are sent up to the cloud (or otherwise saved for the long-term)."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/data-polling-capturing-transmitting.rst)"
        ),
    )
    make_model: MakeModel = Field(
        title="MakeModel",
        description=(
            "Meant to be enough to articulate any difference in how GridWorks code would interact "
            "with a device. Should be able to use this information to buy or build a device."
        ),
    )
    ads_i2c_address_list: List[str] = Field(
        title="Ads I2c Address List",
        description=(
            "The list of I2C Addresses for the Texas Instrument Ads111X chips comprising this "
            "device."
        ),
    )
    total_terminal_blocks: int = Field(
        title="Total Thermistor Channels",
        description=(
            "There are at most 4 thermisters per Ads111X chip. The channels always start with "
            "the number 1, and the channels are expected to follow the natural enumeration set "
            "by the AdsI2cAddressList and the associated AI0 through AI3 on those chips. Analog "
            "In 3 on the final chip may be reserved for calculating a reference open voltage. "
            "The total number of channels may also be constrained by the screw terminal situation."
        ),
    )
    telemetry_name_list: List[TelemetryName] = Field(
        title="Telemetry Name List",
        description=(
            "The list of TelemetryNames that this device/driver combination is capable of producing."
        ),
    )
    display_name: Optional[str] = Field(
        title="Display Name",
        description="Sample: GridWorks TSnap1.0 as 12-channel analog temp sensor",
        default=None,
    )
    type_name: Literal["ads111x.based.cac.gt"] = "ads111x.based.cac.gt"
    version: Literal["000"] = "000"

    class Config:
        extra = "allow"
        populate_by_name = True
        alias_generator = snake_to_pascal

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

    @field_validator("min_poll_period_ms")
    @classmethod
    def _check_min_poll_period_ms(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"MinPollPeriodMs failed PositiveInteger format validation: {e}",
            ) from e
        return v

    @field_validator("ads_i2c_address_list")
    @classmethod
    def _check_ads_i2c_address_list(cls, v: List[str]) -> List[str]:
        for elt in v:
            try:
                check_is_ads1115_i2c_address(elt)
            except ValueError as e:
                raise ValueError(
                    f"AdsI2cAddressList element {elt} failed Ads1115I2cAddress format validation: {e}",
                ) from e
        return v

    @field_validator("total_terminal_blocks")
    @classmethod
    def _check_total_terminal_blocks(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"TotalTerminalBlocks failed PositiveInteger format validation: {e}",
            ) from e
        return v

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: TerminalBlock Ads Chip consistency.
        TotalTerminalBlocks should be greater than 4 * (len(AdsI2cAddressList) - 1 ) and less than or equal to 4*len(AdsI2cAddressList)
        """
        num_ads_chips = len(self.ads_i2c_address_list)
        num_terminals = self.total_terminal_blocks
        if (
            num_terminals <= 4 * (num_ads_chips - 1)
            or num_terminals > 4 * num_ads_chips
        ):
            raise ValueError(
                "Axiom 1 violated! TotalTerminalBlocks should be greater than 4 * (len(AdsI2cAddressList) - 1 ) "
                "and less than or equal to 4*len(AdsI2cAddressList)"
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
        d["MakeModel"] = d["MakeModel"].value
        del d["TelemetryNameList"]
        telemetry_name_list = []
        for elt in self.telemetry_name_list:
            telemetry_name_list.append(elt.value)
        d["TelemetryNameList"] = telemetry_name_list
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
        del d["MakeModel"]
        d["MakeModelGtEnumSymbol"] = MakeModel.value_to_symbol(self.make_model)
        del d["TelemetryNameList"]
        telemetry_name_list = []
        for elt in self.telemetry_name_list:
            telemetry_name_list.append(TelemetryName.value_to_symbol(elt.value))
        d["TelemetryNameList"] = telemetry_name_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the ads111x.based.cac.gt.000 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class Ads111xBasedCacGtMaker:
    type_name = "ads111x.based.cac.gt"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: Ads111xBasedCacGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> Ads111xBasedCacGt:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a ads111x.based.cac.gt.000 type

        Returns:
            Ads111xBasedCacGt instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> Ads111xBasedCacGt:
        """
        Translates a dict representation of a ads111x.based.cac.gt.000 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "ComponentAttributeClassId" not in d2.keys():
            raise GwTypeError(f"dict missing ComponentAttributeClassId: <{d2}>")
        if "MinPollPeriodMs" not in d2.keys():
            raise GwTypeError(f"dict missing MinPollPeriodMs: <{d2}>")
        if "MakeModelGtEnumSymbol" in d2.keys():
            value = MakeModel.symbol_to_value(d2["MakeModelGtEnumSymbol"])
            d2["MakeModel"] = MakeModel(value)
            del d2["MakeModelGtEnumSymbol"]
        elif "MakeModel" in d2.keys():
            if d2["MakeModel"] not in MakeModel.values():
                d2["MakeModel"] = MakeModel.default()
            else:
                d2["MakeModel"] = MakeModel(d2["MakeModel"])
        else:
            raise GwTypeError(
                f"both MakeModelGtEnumSymbol and MakeModel missing from dict <{d2}>",
            )
        if "AdsI2cAddressList" not in d2.keys():
            raise GwTypeError(f"dict missing AdsI2cAddressList: <{d2}>")
        if "TotalTerminalBlocks" not in d2.keys():
            raise GwTypeError(f"dict missing TotalTerminalBlocks: <{d2}>")
        if "TelemetryNameList" not in d2.keys():
            raise GwTypeError(f"dict <{d2}> missing TelemetryNameList")
        if not isinstance(d2["TelemetryNameList"], List):
            raise GwTypeError("TelemetryNameList must be a List!")
        telemetry_name_list = []
        for elt in d2["TelemetryNameList"]:
            if elt in TelemetryName.symbols():
                value = TelemetryName.symbol_to_value(elt)
            elif elt in TelemetryName.values():
                value = elt
            else:
                value = TelemetryName.default()
            telemetry_name_list.append(TelemetryName(value))
        d2["TelemetryNameList"] = telemetry_name_list
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret ads111x.based.cac.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return Ads111xBasedCacGt(**d3)

    @classmethod
    def tuple_to_dc(cls, t: Ads111xBasedCacGt) -> Ads111xBasedCac:
        if t.component_attribute_class_id in Ads111xBasedCac.by_id.keys():
            dc = Ads111xBasedCac.by_id[t.component_attribute_class_id]
        else:
            dc = Ads111xBasedCac(
                component_attribute_class_id=t.component_attribute_class_id,
                min_poll_period_ms=t.min_poll_period_ms,
                make_model=t.make_model,
                ads_i2c_address_list=t.ads_i2c_address_list,
                total_terminal_blocks=t.total_terminal_blocks,
                telemetry_name_list=t.telemetry_name_list,
                display_name=t.display_name,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: Ads111xBasedCac) -> Ads111xBasedCacGt:
        return Ads111xBasedCacGt(
            component_attribute_class_id=dc.component_attribute_class_id,
            min_poll_period_ms=dc.min_poll_period_ms,
            make_model=dc.make_model,
            ads_i2c_address_list=dc.ads_i2c_address_list,
            total_terminal_blocks=dc.total_terminal_blocks,
            telemetry_name_list=dc.telemetry_name_list,
            display_name=dc.display_name,
        )

    @classmethod
    def type_to_dc(cls, t: str) -> Ads111xBasedCac:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: Ads111xBasedCac) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> Ads111xBasedCac:
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


def check_is_positive_integer(v: int) -> None:
    """
    Must be positive when interpreted as an integer. Interpretation as an
    integer follows the pydantic rules for this - which will round down
    rational numbers. So 1.7 will be interpreted as 1 and is also fine,
    while 0.5 is interpreted as 0 and will raise an exception.

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v < 1
    """
    v2 = int(v)
    if v2 < 1:
        raise ValueError(f"<{v}> is not PositiveInteger")


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
