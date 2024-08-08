"""Type electric.meter.cac.gt, version 001"""

import json
import logging
import os
from typing import Any, Dict, List, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import Field, field_validator

from gwproto.data_classes.cacs.electric_meter_cac import ElectricMeterCac
from gwproto.enums import MakeModel, TelemetryName
from gwproto.types import ComponentAttributeClassGt as CacGt

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class ElectricMeterCacGt(CacGt):
    """
    Type for tracking  Electric Meter ComponentAttributeClasses.

    GridWorks Spaceheat SCADA uses the GridWorks GNodeRegistry structures and abstractions for
    managing relational device data. The Cac, or ComponentAttributeClass, is part of this structure.
    PollPeriodMs -> MinPollPeriodMs, remove LocalCommInterface, AllowExtra, add axiom enforcing
    that it also meets requirements for a ComponentAttributeClassGt.

    [More info](https://g-node-registry.readthedocs.io/en/latest/component-attribute-class.html)
    """

    component_attribute_class_id: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class (aka 'cac' or Component Attribute Class). "
            "Authority is maintained by the World Registry."
        ),
    )
    make_model: MakeModel = Field(
        title="MakeModel",
        description=(
            "The brand name identifier for the electric meter (what you would specify in order "
            "to buy one)."
        ),
    )
    display_name: Optional[str] = Field(
        title="DisplayName",
        description="Sample: EGauge 4030",
        default=None,
    )
    telemetry_name_list: List[TelemetryName] = Field(
        title="TelemetryNames read by this power meter",
    )
    min_poll_period_ms: int = Field(
        title="Poll Period in Milliseconds",
        description=(
            "Poll Period refers to the period of time between two readings by the local actor. "
            "This is in contrast to Capture Period, which refers to the period between readings "
            "that are sent up to the cloud (or otherwise saved for the long-term)."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/data-polling-capturing-transmitting.rst)"
        ),
    )
    default_baud: Optional[int] = Field(
        title="To be used when the comms method requires a baud rate",
        default=None,
    )
    type_name: Literal["electric.meter.cac.gt"] = "electric.meter.cac.gt"
    version: Literal["001"] = "001"

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
        Serialize to the electric.meter.cac.gt.001 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ElectricMeterCacGtMaker:
    type_name = "electric.meter.cac.gt"
    version = "001"

    @classmethod
    def tuple_to_type(cls, tuple: ElectricMeterCacGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> ElectricMeterCacGt:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a electric.meter.cac.gt.001 type

        Returns:
            ElectricMeterCacGt instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ElectricMeterCacGt:
        """
        Translates a dict representation of a electric.meter.cac.gt.001 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "ComponentAttributeClassId" not in d2.keys():
            raise GwTypeError(f"dict missing ComponentAttributeClassId: <{d2}>")
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
        if "MinPollPeriodMs" not in d2.keys():
            raise GwTypeError(f"dict missing MinPollPeriodMs: <{d2}>")
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret electric.meter.cac.gt version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return ElectricMeterCacGt(**d3)

    @classmethod
    def tuple_to_dc(cls, t: ElectricMeterCacGt) -> ElectricMeterCac:
        if t.component_attribute_class_id in ElectricMeterCac.by_id.keys():
            dc = ElectricMeterCac.by_id[t.component_attribute_class_id]
        else:
            dc = ElectricMeterCac(
                component_attribute_class_id=t.component_attribute_class_id,
                make_model=t.make_model,
                display_name=t.display_name,
                telemetry_name_list=t.telemetry_name_list,
                min_poll_period_ms=t.min_poll_period_ms,
                default_baud=t.default_baud,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ElectricMeterCac) -> ElectricMeterCacGt:
        return ElectricMeterCacGt(
            component_attribute_class_id=dc.component_attribute_class_id,
            make_model=dc.make_model,
            display_name=dc.display_name,
            telemetry_name_list=dc.telemetry_name_list,
            min_poll_period_ms=dc.min_poll_period_ms,
            default_baud=dc.default_baud,
        )

    @classmethod
    def type_to_dc(cls, t: str) -> ElectricMeterCac:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: ElectricMeterCac) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> ElectricMeterCac:
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
