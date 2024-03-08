"""Type ads111x.based.cac.gt, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gwproto.data_classes.cacs.ads111x_based_cac import Ads111xBasedCac
from gwproto.enums import MakeModel as EnumMakeModel
from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class Ads111xBasedCacGt(BaseModel):
    """
    TI ADS111x Based Temp Sensing Component Attribute Class.

    Component Attribute Class for sensors using the Texas Instrument ADS111X series of chips
    used with 10K thermistors for reading temperature. The ADS111X is a class of I2C-based 16-bit
    Analog Digital Convertors. The chip has 4 possible I2C addresses, and the address can be
    set by jumpering the "Addr" pin of the ADS111X chip to one of the 4 I2C pins. 0x48: GND,
    0x49: VDD, 0x4A: SDA, 0x4B: SCL. GridWorks Spaceheat SCADA uses the GridWorks GNodeRegistry
    structures and abstractions for managing relational device data. The Cac, or ComponentAttributeClass,
    is part of this structure.

    [More info](https://drive.google.com/drive/u/0/folders/1oFvs4-kvwyzt220eYlFnwdzEgVCIbbt6)
    """

    ComponentAttributeClassId: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class (aka 'cac' or Component Attribute Class). "
            "Authority is maintained by the World Registry."
        ),
    )
    MinPollPeriodMs: int = Field(
        title="Min Poll Period in Milliseconds",
        description=(
            "Poll Period refers to the period of time between two readings by the local actor. "
            "This is in contrast to Capture Period, which refers to the period between readings "
            "that are sent up to the cloud (or otherwise saved for the long-term)."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/data-polling-capturing-transmitting.rst)"
        ),
    )
    MakeModel: EnumMakeModel = Field(
        title="MakeModel",
        description=(
            "Meant to be enough to articulate any difference in how GridWorks code would interact "
            "with a device. Should be able to use this information to buy or build a device."
        ),
    )
    AdsI2cAddressList: List[str] = Field(
        title="Ads I2c Address List",
        description=(
            "The list of I2C Addresses for the Texas Instrument Ads111X chips comprising this "
            "device."
        ),
    )
    TotalTerminalBlocks: int = Field(
        title="Total Thermistor Channels",
        description=(
            "There are at most 4 thermisters per Ads111X chip. The channels always start with "
            "the number 1, and the channels are expected to follow the natural enumeration set "
            "by the AdsI2cAddressList and the associated AI0 through AI3 on those chips. Analog "
            "In 3 on the final chip may be reserved for calculating a reference open voltage. "
            "The total number of channels may also be constrained by the screw terminal situation."
        ),
    )
    TelemetryNameList: List[TelemetryName] = Field(
        title="Telemetry Name List",
        description=(
            "The list of TelemetryNames that this device/driver combination is capable of producing."
        ),
    )
    DisplayName: Optional[str] = Field(
        title="Display Name",
        description="Sample: GridWorks TSnap1.0 as 12-channel analog temp sensor",
        default=None,
    )
    TypeName: Literal["ads111x.based.cac.gt"] = "ads111x.based.cac.gt"
    Version: Literal["000"] = "000"

    class Config:
        extra = Extra.allow

    @validator("ComponentAttributeClassId")
    def _check_component_attribute_class_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentAttributeClassId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("MinPollPeriodMs")
    def _check_min_poll_period_ms(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"MinPollPeriodMs failed PositiveInteger format validation: {e}"
            )
        return v

    @validator("AdsI2cAddressList")
    def _check_ads_i2c_address_list(cls, v: List[str]) -> List[str]:
        for elt in v:
            try:
                check_is_ads1115_i2c_address(elt)
            except ValueError as e:
                raise ValueError(
                    f"AdsI2cAddressList element {elt} failed Ads1115I2cAddress format validation: {e}"
                )
        return v

    @validator("TotalTerminalBlocks")
    def _check_total_terminal_blocks(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"TotalTerminalBlocks failed PositiveInteger format validation: {e}"
            )
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: TerminalBlock Ads Chip consistency.
        TotalTerminalBlocks should be greater than 4 * (len(AdsI2cAddressList) - 1 ) and less than or equal to 4*len(AdsI2cAddressList)
        """
        # TODO: Implement check for axiom 1"
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        ads111x.based.cac.gt.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        ads111x.based.cac.gt.000 type. Unlike the standard python dict method,
        it makes the following substantive changes:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.
        """
        d = {
            key: value
            for key, value in self.dict(
                include=self.__fields_set__ | {"TypeName", "Version"}
            ).items()
            if value is not None
        }
        del d["MakeModel"]
        d["MakeModelGtEnumSymbol"] = EnumMakeModel.value_to_symbol(self.MakeModel)
        del d["TelemetryNameList"]
        telemetry_name_list = []
        for elt in self.TelemetryNameList:
            telemetry_name_list.append(TelemetryName.value_to_symbol(elt.value))
        d["TelemetryNameList"] = telemetry_name_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the ads111x.based.cac.gt.000 representation.

        Instances in the class are python-native representations of ads111x.based.cac.gt.000
        objects, while the actual ads111x.based.cac.gt.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is Ads111xBasedCacGt.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class Ads111xBasedCacGt_Maker:
    type_name = "ads111x.based.cac.gt"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: Ads111xBasedCacGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> Ads111xBasedCacGt:
        """
        Given a serialized JSON type object, returns the Python class object.
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing <{t}> must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> Ads111xBasedCacGt:
        """
        Deserialize a dictionary representation of a ads111x.based.cac.gt.000 message object
        into a Ads111xBasedCacGt python object for internal use.

        This is the near-inverse of the Ads111xBasedCacGt.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a Ads111xBasedCacGt object.

        Returns:
            Ads111xBasedCacGt
        """
        d2 = dict(d)
        if "ComponentAttributeClassId" not in d2.keys():
            raise SchemaError(f"dict missing ComponentAttributeClassId: <{d2}>")
        if "MinPollPeriodMs" not in d2.keys():
            raise SchemaError(f"dict missing MinPollPeriodMs: <{d2}>")
        if "MakeModelGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"MakeModelGtEnumSymbol missing from dict <{d2}>")
        value = EnumMakeModel.symbol_to_value(d2["MakeModelGtEnumSymbol"])
        d2["MakeModel"] = EnumMakeModel(value)
        del d2["MakeModelGtEnumSymbol"]
        if "AdsI2cAddressList" not in d2.keys():
            raise SchemaError(f"dict missing AdsI2cAddressList: <{d2}>")
        if "TotalTerminalBlocks" not in d2.keys():
            raise SchemaError(f"dict missing TotalTerminalBlocks: <{d2}>")
        if "TelemetryNameList" not in d2.keys():
            raise SchemaError(f"dict <{d2}> missing TelemetryNameList")
        if not isinstance(d2["TelemetryNameList"], List):
            raise SchemaError("TelemetryNameList must be a List!")
        telemetry_name_list = []
        for elt in d2["TelemetryNameList"]:
            value = TelemetryName.symbol_to_value(elt)
            telemetry_name_list.append(TelemetryName(value))
        d2["TelemetryNameList"] = telemetry_name_list
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret ads111x.based.cac.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return Ads111xBasedCacGt(**d2)

    @classmethod
    def tuple_to_dc(cls, t: Ads111xBasedCacGt) -> Ads111xBasedCac:
        if t.ComponentAttributeClassId in Ads111xBasedCac.by_id.keys():
            dc = Ads111xBasedCac.by_id[t.ComponentAttributeClassId]
        else:
            dc = Ads111xBasedCac(
                component_attribute_class_id=t.ComponentAttributeClassId,
                min_poll_period_ms=t.MinPollPeriodMs,
                make_model=t.MakeModel,
                ads_i2c_address_list=t.AdsI2cAddressList,
                total_terminal_blocks=t.TotalTerminalBlocks,
                telemetry_name_list=t.TelemetryNameList,
                display_name=t.DisplayName,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: Ads111xBasedCac) -> Ads111xBasedCacGt:
        return Ads111xBasedCacGt(
            ComponentAttributeClassId=dc.component_attribute_class_id,
            MinPollPeriodMs=dc.min_poll_period_ms,
            MakeModel=dc.make_model,
            AdsI2cAddressList=dc.ads_i2c_address_list,
            TotalTerminalBlocks=dc.total_terminal_blocks,
            TelemetryNameList=dc.telemetry_name_list,
            DisplayName=dc.display_name,
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
    Ads1115I2cAddress: ToLower(v) in ["0x48", "0x49", "0x4a", "0x4b"].

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
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"<{v}> split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError(f"Words of <{v}> are not all hex")
    if len(x[0]) != 8:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[1]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[2]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[3]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[4]) != 12:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
