"""Type simple.sensor.telemetry, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class SimpleSensorTelemetry(BaseModel):
    """
    Simple Sensor Telemetry.

    A reading sent from a simple sensor to its SCADA Spaceheat Node. A simple sensor is one
    whose CapturedBy Spaceheat Node is the same as the AboutNode.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-actor.html)
    """

    Name: TelemetryName = Field(
        title="Name",
        description=(
            "The name of the Simple Sensing Spaceheat Node. This is both the AboutNodeName and "
            "FromNodeName for a data channel. The TelemetryName (and thus Units) are expected "
            "to be inferred by the Spaceheat Node. For example this is done initially in SCADA "
            "code according to whether the component of the Node is a PipeFlowSensorComponent, "
            "SimpleTempSensorComponent etc."
        ),
    )
    Value: int = Field(
        title="Value",
        description="The value of the reading.",
    )
    ScadaReadTimeUnixMs: int = Field(
        title="Scada Read Time in Unix Milliseconds",
    )
    TypeName: Literal["simple.sensor.telemetry"] = "simple.sensor.telemetry"
    Version: Literal["000"] = "000"

    @validator("ScadaReadTimeUnixMs")
    def _check_scada_read_time_unix_ms(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_ms(v)
        except ValueError as e:
            raise ValueError(
                f"ScadaReadTimeUnixMs failed ReasonableUnixTimeMs format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        simple.sensor.telemetry.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        simple.sensor.telemetry.000 type. Unlike the standard python dict method,
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
        del d["Name"]
        d["NameGtEnumSymbol"] = TelemetryName.value_to_symbol(self.Name)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the simple.sensor.telemetry.000 representation.

        Instances in the class are python-native representations of simple.sensor.telemetry.000
        objects, while the actual simple.sensor.telemetry.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is SimpleSensorTelemetry.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class SimpleSensorTelemetry_Maker:
    type_name = "simple.sensor.telemetry"
    version = "000"

    def __init__(
        self,
        name: TelemetryName,
        value: int,
        scada_read_time_unix_ms: int,
    ):
        self.tuple = SimpleSensorTelemetry(
            Name=name,
            Value=value,
            ScadaReadTimeUnixMs=scada_read_time_unix_ms,
        )

    @classmethod
    def tuple_to_type(cls, tuple: SimpleSensorTelemetry) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> SimpleSensorTelemetry:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> SimpleSensorTelemetry:
        """
        Deserialize a dictionary representation of a simple.sensor.telemetry.000 message object
        into a SimpleSensorTelemetry python object for internal use.

        This is the near-inverse of the SimpleSensorTelemetry.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a SimpleSensorTelemetry object.

        Returns:
            SimpleSensorTelemetry
        """
        d2 = dict(d)
        if "NameGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"NameGtEnumSymbol missing from dict <{d2}>")
        value = TelemetryName.symbol_to_value(d2["NameGtEnumSymbol"])
        d2["Name"] = TelemetryName(value)
        del d2["NameGtEnumSymbol"]
        if "Value" not in d2.keys():
            raise SchemaError(f"dict missing Value: <{d2}>")
        if "ScadaReadTimeUnixMs" not in d2.keys():
            raise SchemaError(f"dict missing ScadaReadTimeUnixMs: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret simple.sensor.telemetry version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return SimpleSensorTelemetry(**d2)
