"""Type simple.temp.sensor.cac.gt, version 000"""

import json
import logging
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.data_classes.cacs.simple_temp_sensor_cac import SimpleTempSensorCac
from gwproto.enums import MakeModel as EnumMakeModel
from gwproto.enums import TelemetryName as EnumTelemetryName
from gwproto.enums import Unit
from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class SimpleTempSensorCacGt(BaseModel):
    """
    Type for tracking Simple Temp Sensor ComponentAttributeClasses.

    GridWorks Spaceheat SCADA uses the GridWorks GNodeRegistry structures and abstractions for
    managing relational device data. The Cac, or ComponentAttributeClass, is part of this structure.

    [More info](https://g-node-registry.readthedocs.io/en/latest/component-attribute-class.html)
    """

    ComponentAttributeClassId: str = Field(
        title="ComponentAttributeClassId",
        description=(
            "Unique identifier for the device class (aka 'cac' or Component Attribute Class). "
            "Authority is maintained by the World Registry."
        ),
    )
    MakeModel: EnumMakeModel = Field(
        title="MakeModel",
    )
    TypicalResponseTimeMs: int = Field(
        title="TypicalResponseTimeMs",
    )
    Exponent: int = Field(
        title="Exponent",
        description=(
            "Say the TelemetryName is WaterTempCTimes1000; this corresponds to units of Celsius. "
            "To match the implication in the name, the Exponent should be 3, and a Value of 65300 "
            "would indicate 65.3 deg C"
        ),
    )
    TempUnit: Unit = Field(
        title="TempUnit",
    )
    TelemetryName: EnumTelemetryName = Field(
        title="TelemetryName",
    )
    DisplayName: Optional[str] = Field(
        title="DisplayName",
        default=None,
    )
    CommsMethod: Optional[str] = Field(
        title="CommsMethod",
        default=None,
    )
    TypeName: Literal["simple.temp.sensor.cac.gt"] = "simple.temp.sensor.cac.gt"
    Version: Literal["000"] = "000"

    @validator("ComponentAttributeClassId")
    def _check_component_attribute_class_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentAttributeClassId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        simple.temp.sensor.cac.gt.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        simple.temp.sensor.cac.gt.000 type. Unlike the standard python dict method,
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
        del d["TempUnit"]
        d["TempUnitGtEnumSymbol"] = Unit.value_to_symbol(self.TempUnit)
        del d["TelemetryName"]
        d["TelemetryNameGtEnumSymbol"] = EnumTelemetryName.value_to_symbol(
            self.TelemetryName
        )
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the simple.temp.sensor.cac.gt.000 representation.

        Instances in the class are python-native representations of simple.temp.sensor.cac.gt.000
        objects, while the actual simple.temp.sensor.cac.gt.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is SimpleTempSensorCacGt.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class SimpleTempSensorCacGt_Maker:
    type_name = "simple.temp.sensor.cac.gt"
    version = "000"

    def __init__(
        self,
        component_attribute_class_id: str,
        make_model: EnumMakeModel,
        typical_response_time_ms: int,
        exponent: int,
        temp_unit: Unit,
        telemetry_name: EnumTelemetryName,
        display_name: Optional[str],
        comms_method: Optional[str],
    ):
        self.tuple = SimpleTempSensorCacGt(
            ComponentAttributeClassId=component_attribute_class_id,
            MakeModel=make_model,
            TypicalResponseTimeMs=typical_response_time_ms,
            Exponent=exponent,
            TempUnit=temp_unit,
            TelemetryName=telemetry_name,
            DisplayName=display_name,
            CommsMethod=comms_method,
        )

    @classmethod
    def tuple_to_type(cls, tuple: SimpleTempSensorCacGt) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> SimpleTempSensorCacGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> SimpleTempSensorCacGt:
        """
        Deserialize a dictionary representation of a simple.temp.sensor.cac.gt.000 message object
        into a SimpleTempSensorCacGt python object for internal use.

        This is the near-inverse of the SimpleTempSensorCacGt.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a SimpleTempSensorCacGt object.

        Returns:
            SimpleTempSensorCacGt
        """
        d2 = dict(d)
        if "ComponentAttributeClassId" not in d2.keys():
            raise SchemaError(f"dict missing ComponentAttributeClassId: <{d2}>")
        if "MakeModelGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"MakeModelGtEnumSymbol missing from dict <{d2}>")
        value = EnumMakeModel.symbol_to_value(d2["MakeModelGtEnumSymbol"])
        d2["MakeModel"] = EnumMakeModel(value)
        if "TypicalResponseTimeMs" not in d2.keys():
            raise SchemaError(f"dict missing TypicalResponseTimeMs: <{d2}>")
        if "Exponent" not in d2.keys():
            raise SchemaError(f"dict missing Exponent: <{d2}>")
        if "TempUnitGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"TempUnitGtEnumSymbol missing from dict <{d2}>")
        value = Unit.symbol_to_value(d2["TempUnitGtEnumSymbol"])
        d2["TempUnit"] = Unit(value)
        if "TelemetryNameGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"TelemetryNameGtEnumSymbol missing from dict <{d2}>")
        value = EnumTelemetryName.symbol_to_value(d2["TelemetryNameGtEnumSymbol"])
        d2["TelemetryName"] = EnumTelemetryName(value)
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret simple.temp.sensor.cac.gt version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return SimpleTempSensorCacGt(**d2)

    @classmethod
    def tuple_to_dc(cls, t: SimpleTempSensorCacGt) -> SimpleTempSensorCac:
        if t.ComponentAttributeClassId in SimpleTempSensorCac.by_id.keys():
            dc = SimpleTempSensorCac.by_id[t.ComponentAttributeClassId]
        else:
            dc = SimpleTempSensorCac(
                component_attribute_class_id=t.ComponentAttributeClassId,
                make_model=t.MakeModel,
                typical_response_time_ms=t.TypicalResponseTimeMs,
                exponent=t.Exponent,
                temp_unit=t.TempUnit,
                telemetry_name=t.TelemetryName,
                display_name=t.DisplayName,
                comms_method=t.CommsMethod,
            )
        return dc

    @classmethod
    def dc_to_tuple(cls, dc: SimpleTempSensorCac) -> SimpleTempSensorCacGt:
        t = SimpleTempSensorCacGt_Maker(
            component_attribute_class_id=dc.component_attribute_class_id,
            make_model=dc.make_model,
            typical_response_time_ms=dc.typical_response_time_ms,
            exponent=dc.exponent,
            temp_unit=dc.temp_unit,
            telemetry_name=dc.telemetry_name,
            display_name=dc.display_name,
            comms_method=dc.comms_method,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> SimpleTempSensorCac:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: SimpleTempSensorCac) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> SimpleTempSensorCac:
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
