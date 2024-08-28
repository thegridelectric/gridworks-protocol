"""Type electric.meter.component.gt, version 001"""

import json
import logging
import os
from typing import Any, Dict, List, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import ConfigDict, Field, field_validator, model_validator
from typing_extensions import Self

from gwproto.data_classes.components.electric_meter_component import (
    ElectricMeterComponent,
)
from gwproto.types.channel_config import ChannelConfig, ChannelConfigMaker
from gwproto.types.component_gt import ComponentGt
from gwproto.types.egauge_io import EgaugeIo, EgaugeIoMaker

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class ElectricMeterComponentGt(ComponentGt):
    """
    Type for tracking Electric Meter Components.

    Designed for specific instances of Electric Meters. It extends the component.gt.000 type.
    Authority for the attributes of the component.gt.000 (ComponentId, ComponentAttributeClassId,
    DisplayName, HwUid) belongs to the WorldRegistry. The WorldRegistry is part of the GridWorks
    'BackOffice' structure for managing relational device data . Notably, ComponentId and ComponentAttributeClass
    are both required and immutable. HwUid is optional but once it is set to a non-null value
    that is also immutable - it is meant to be an immutable identifier associated to a specific
    physical device, ideally one that can be read remotely by the SCADA and also by the naked
    eye. The DisplayName is mutable, with its current value in time governed by the WorldRegistry.

    [More info](https://g-node-registry.readthedocs.io/en/latest/electric-meters.html)
    """

    component_id: str = Field(
        title="Component Id",
        description=(
            "Primary GridWorks identifier for a specific physical instance of an ElectricMeter, "
            "and also as a more generic Component."
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
        title="Display Name for the Power Meter",
        description="Sample: Oak EGauge6074",
        default=None,
    )
    config_list: List[ChannelConfig] = Field(
        title="List of Data Channel configs ",
        description=(
            "Information re timing of data polling and capture for the channels read by the node "
            "(i.e. channels that convey power, current, voltage, frequency for various power "
            "consuming elements of the system)."
        ),
    )
    hw_uid: Optional[str] = Field(
        title="Unique Hardware Id for the Power Meter",
        description="For eGauge, use what comes back over modbus address 100.",
        default=None,
    )
    modbus_host: Optional[str] = Field(
        title="Host on LAN when power meter is modbus over Ethernet",
        default=None,
    )
    modbus_port: Optional[int] = Field(
        title="ModbusPort",
        default=None,
    )
    egauge_io_list: List[EgaugeIo] = Field(
        title="Bijecton from EGauge4030 input to ConfigList output",
        description=(
            "This should be empty unless the MakeModel of the corresponding component attribute "
            "class is EGauge 4030. The channels that can be read from an EGauge 4030 are configurable "
            "by the person who installs the device. The information is encapsulated in a modbus "
            "map provided by eGauge as a csv from a device-specific API. The EGaugeIoList maps "
            "the data from this map to the data that the SCADA expects to see."
        ),
    )
    type_name: Literal["electric.meter.component.gt"] = "electric.meter.component.gt"
    version: Literal["001"] = "001"
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

    @field_validator("modbus_port")
    @classmethod
    def _check_modbus_port(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"ModbusPort failed PositiveInteger format validation: {e}",
            ) from e
        return v

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Modbus consistency.
        ModbusHost is None if and only if ModbusPort is None
        """
        axiom_passes = True
        if self.modbus_host is not None:
            if self.modbus_port is None:
                axiom_passes = False

        if self.modbus_port is not None:
            if self.modbus_host is None:
                axiom_passes = False
        if not axiom_passes:
            raise ValueError(
                f"Violates Axiom 1:  ModbusHost is None if and only if ModbusPort is None:\n <{self}>"
            )
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: Egauge4030 Means Modbus.
        If the EgaugeIoList has non-zero length, then the ModbusHost is not None
        """
        if len(self.egauge_io_list) == 0:
            return self

        # If the EgaugeIoList has non-zero length, then the ModbusHost is not Non
        if self.modbus_host is None:
            raise ValueError(
                "Axiom 2 fails: If the EgaugeIoList has non-zero "
                "length, then the ModbusHost is not None "
            )
        return self

    @model_validator(mode="after")
    def check_axiom_3(self) -> Self:
        """
        Axiom 3: Channel Name Consistency.
        If the EgaugeIoList has non-zero length:
          1) Len(EgaugeIoList) == Len(ConfigList)
          2) There are no duplicates of ChannelName in the ConfigList or EgaugeIoList
          3) The set of ChannelNames in IoConfig is equal to the set of ChannelNames in ConfigList
        """

        if len(self.egauge_io_list) == 0:
            return self

        # If the EgaugeIoList has non-zero length, then Len(EgaugeIoList) == Len(ConfigList)
        if len(self.egauge_io_list) != len(self.config_list):
            raise ValueError(
                "Axiom 3 fails: EgaugeIoList and ConfigList must have equal length"
            )

        config_channel_names = list(map(lambda x: x.channel_name, self.config_list))
        if len(config_channel_names) != len(set(config_channel_names)):
            raise ValueError(
                f"Axiom 3 fails: duplicate channel name(s) in ConfigList:\n {self}"
            )

        io_channel_names = list(map(lambda x: x.channel_name, self.egauge_io_list))
        if len(io_channel_names) != len(set(io_channel_names)):
            raise ValueError(
                f"Axiom 3 fails: duplicate channel name(s) in EgaugeIoList:\n {self}"
            )

        if set(config_channel_names) != set(io_channel_names):
            raise ValueError(
                "Axiom 3 fails: The set of ChannelNames in IoConfig is NOT "
                f"equal to the set of ChannelNames in ConfigList:\n {self} "
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
        egauge_io_list = []
        for elt in self.egauge_io_list:
            egauge_io_list.append(elt.as_dict())
        d["EgaugeIoList"] = egauge_io_list
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
        egauge_io_list = []
        for elt in self.egauge_io_list:
            egauge_io_list.append(elt.as_dict())
        d["EgaugeIoList"] = egauge_io_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the electric.meter.component.gt.001 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ElectricMeterComponentGtMaker:
    type_name = "electric.meter.component.gt"
    version = "001"

    @classmethod
    def tuple_to_type(cls, tuple: ElectricMeterComponentGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> ElectricMeterComponentGt:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a electric.meter.component.gt.001 type

        Returns:
            ElectricMeterComponentGt instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ElectricMeterComponentGt:
        """
        Translates a dict representation of a electric.meter.component.gt.001 message object
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
        if "EgaugeIoList" not in d2.keys():
            raise GwTypeError(f"dict missing EgaugeIoList: <{d2}>")
        if not isinstance(d2["EgaugeIoList"], List):
            raise GwTypeError(f"EgaugeIoList <{d2['EgaugeIoList']}> must be a List!")
        egauge_io_list = []
        for elt in d2["EgaugeIoList"]:
            if not isinstance(elt, dict):
                raise GwTypeError(
                    f"EgaugeIoList <{d2['EgaugeIoList']}> must be a List of EgaugeIo types"
                )
            t = EgaugeIoMaker.dict_to_tuple(elt)
            egauge_io_list.append(t)
        d2["EgaugeIoList"] = egauge_io_list
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret electric.meter.component.gt version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return ElectricMeterComponentGt(**d3)

    @classmethod
    def tuple_to_dc(cls, t: ElectricMeterComponentGt) -> ElectricMeterComponent:
        if t.component_id in ElectricMeterComponent.by_id.keys():
            dc = ElectricMeterComponent.by_id[t.component_id]
        else:
            dc = ElectricMeterComponent(
                component_id=t.component_id,
                component_attribute_class_id=t.component_attribute_class_id,
                display_name=t.display_name,
                config_list=t.config_list,
                hw_uid=t.hw_uid,
                modbus_host=t.modbus_host,
                modbus_port=t.modbus_port,
                egauge_io_list=t.egauge_io_list,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ElectricMeterComponent) -> ElectricMeterComponentGt:
        return ElectricMeterComponentGt(
            component_id=dc.component_id,
            component_attribute_class_id=dc.component_attribute_class_id,
            display_name=dc.display_name,
            config_list=dc.config_list,
            hw_uid=dc.hw_uid,
            modbus_host=dc.modbus_host,
            modbus_port=dc.modbus_port,
            egauge_io_list=dc.egauge_io_list,
        )

    @classmethod
    def type_to_dc(cls, t: str) -> ElectricMeterComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: ElectricMeterComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> ElectricMeterComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))


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
