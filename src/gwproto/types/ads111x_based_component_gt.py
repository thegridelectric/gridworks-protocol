"""Type ads111x.based.component.gt, version 000"""
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
from pydantic import validator

from gwproto.data_classes.components.ads111x_based_component import (
    Ads111xBasedComponent,
)
from gwproto.errors import SchemaError
from gwproto.types.thermistor_data_processing_config import (
    ThermistorDataProcessingConfig,
)
from gwproto.types.thermistor_data_processing_config import (
    ThermistorDataProcessingConfig_Maker,
)


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class Ads111xBasedComponentGt(BaseModel):
    """
    TI ADS111x Based Temp Sensing Component.

    Designed for specific instances of a temp sensor based on the Texas Instrument ADS111X series
    of chips used w 10K thermistors for reading temperature.

    [More info](https://drive.google.com/drive/u/0/folders/1oFvs4-kvwyzt220eYlFnwdzEgVCIbbt6)
    """

    ComponentId: str = Field(
        title="Component Id",
        description=(
            "Primary GridWorks identifier for a specific physical instance of a MultipurposeSensor "
            "(perhaps only the 12-channel analog temp sensor), and also as a more generic Component."
        ),
    )
    ComponentAttributeClassId: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class. Authority for these, as well as the relationship "
            "between Components and ComponentAttributeClasses (Cacs) is maintained by the World "
            "Registry."
        ),
    )
    DisplayName: Optional[str] = Field(
        title="Display Name",
        description="Sample: Oak 16-channel AdsTemp Sensor <100>",
        default=None,
    )
    OpenVoltageByAds: List[float] = Field(
        title="Open Voltage By Ads",
        description=(
            "The voltage reading with no thermistor attached is called the 'open voltage.' It "
            "is close to the power supply voltage (e.g. 5V) , but we have found that there is "
            "non-trivial variation (~0.2 V), and there can even be variation in the average open "
            "voltage in the same installation across different ADS chips (~0.01 or 0.02V). This "
            "list follows the same order as the self.cac.AdsI2cAddressList."
        ),
    )
    ConfigList: List[ThermistorDataProcessingConfig] = Field(
        title="Thermistor Config List",
        description=(
            "This includes the list of configuration information needed for data processing and "
            "reporting for the data collected by thermistors - both voltage and (derived) temperature."
        ),
    )
    HwUid: Optional[str] = Field(
        title="Hardware Unique Id",
        default=None,
    )
    TypeName: Literal["ads111x.based.component.gt"] = "ads111x.based.component.gt"
    Version: Literal["000"] = "000"

    class Config:
        extra = Extra.allow

    @validator("ComponentId")
    def _check_component_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("ComponentAttributeClassId")
    def _check_component_attribute_class_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentAttributeClassId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("OpenVoltageByAds")
    def _check_open_voltage_by_ads(cls, v: List[float]) -> List[float]:
        for elt in v:
            try:
                check_is_near5(elt)
            except ValueError as e:
                raise ValueError(
                    f"OpenVoltageByAds element {elt} failed Near5 format validation: {e}"
                )
        return v

    @validator("ConfigList")
    def check_config_list(cls, v: List[ThermistorDataProcessingConfig]) -> List[ThermistorDataProcessingConfig]:
        """
        Axiom 1: Terminal Block, TelemetryName uniqueness.
        Each pair (x.TerminalBlockIdx, x.ReportingConfig.TelemetryName) in the ConfigList is unique.
        """
        ...
        # TODO: Implement Axiom(s)

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        ads111x.based.component.gt.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        ads111x.based.component.gt.000 type. Unlike the standard python dict method,
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
        # Recursively calling as_dict()
        config_list = []
        for elt in self.ConfigList:
            config_list.append(elt.as_dict())
        d["ConfigList"] = config_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the ads111x.based.component.gt.000 representation.

        Instances in the class are python-native representations of ads111x.based.component.gt.000
        objects, while the actual ads111x.based.component.gt.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is Ads111xBasedComponentGt.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class Ads111xBasedComponentGt_Maker:
    type_name = "ads111x.based.component.gt"
    version = "000"

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        display_name: Optional[str],
        open_voltage_by_ads: List[float],
        config_list: List[ThermistorDataProcessingConfig],
        hw_uid: Optional[str],
    ):
        self.tuple = Ads111xBasedComponentGt(
            ComponentId=component_id,
            ComponentAttributeClassId=component_attribute_class_id,
            DisplayName=display_name,
            OpenVoltageByAds=open_voltage_by_ads,
            ConfigList=config_list,
            HwUid=hw_uid,
        )

    @classmethod
    def tuple_to_type(cls, tuple: Ads111xBasedComponentGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> Ads111xBasedComponentGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> Ads111xBasedComponentGt:
        """
        Deserialize a dictionary representation of a ads111x.based.component.gt.000 message object
        into a Ads111xBasedComponentGt python object for internal use.

        This is the near-inverse of the Ads111xBasedComponentGt.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a Ads111xBasedComponentGt object.

        Returns:
            Ads111xBasedComponentGt
        """
        d2 = dict(d)
        if "ComponentId" not in d2.keys():
            raise SchemaError(f"dict missing ComponentId: <{d2}>")
        if "ComponentAttributeClassId" not in d2.keys():
            raise SchemaError(f"dict missing ComponentAttributeClass: <{d2}>")
        if "OpenVoltageByAds" not in d2.keys():
            raise SchemaError(f"dict missing OpenVoltageByAds: <{d2}>")
        if "ConfigList" not in d2.keys():
            raise SchemaError(f"dict missing ConfigList: <{d2}>")
        if not isinstance(d2["ConfigList"], List):
            raise SchemaError(f"ConfigList <{d2['ConfigList']}> must be a List!")
        config_list = []
        for elt in d2["ConfigList"]:
            if not isinstance(elt, dict):
                raise SchemaError(f"ConfigList <{d2['ConfigList']}> must be a List of ThermistorDataProcessingConfig types")
            t = ThermistorDataProcessingConfig_Maker.dict_to_tuple(elt)
            config_list.append(t)
        d2["ConfigList"] = config_list
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret ads111x.based.component.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return Ads111xBasedComponentGt(**d2)

    @classmethod
    def tuple_to_dc(cls, t: Ads111xBasedComponentGt) -> Ads111xBasedComponent:
        if t.ComponentId in Ads111xBasedComponent.by_id.keys():
            dc = Ads111xBasedComponent.by_id[t.ComponentId]
        else:
            dc = Ads111xBasedComponent(
                component_id=t.ComponentId,
                component_attribute_class_id=t.ComponentAttributeClassId,
                display_name=t.DisplayName,
                open_voltage_by_ads=t.OpenVoltageByAds,
                config_list=t.ConfigList,
                hw_uid=t.HwUid,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: Ads111xBasedComponent) -> Ads111xBasedComponentGt:
        t = Ads111xBasedComponentGt_Maker(
            component_id=dc.component_id,
            component_attribute_class_id=dc.component_attribute_class_id,
            display_name=dc.display_name,
            open_voltage_by_ads=dc.open_voltage_by_ads,
            config_list=dc.config_list,
            hw_uid=dc.hw_uid,
        ).tuple
        return t

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
    Ads1115I2cAddress: ToLower(v) in ["0x48", "0x49", "0x4a", "0x4b"].

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
