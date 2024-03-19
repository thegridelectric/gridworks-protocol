"""Type gt.sh.simple.telemetry.status, version 100"""
import json
import logging
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gwproto.enums import TelemetryName as EnumTelemetryName
from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class GtShSimpleTelemetryStatus100(BaseModel):
    """
    Data read from a SimpleSensor run by a SpaceHeat SCADA.

    A list of readings from a simple sensor for a Spaceheat SCADA. Designed as part of a status
    message sent from the SCADA to its AtomicTNode typically once every 5 minutes. The nth element
    of each of its two lists refer to the same reading (i.e. what the value is, when it was
    read).

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/simple-sensor.html)
    """

    ShNodeAlias: str = Field(
        title="SpaceheatNodeAlias",
        description="The Alias of the SimpleSensor associated to the readings",
    )
    TelemetryName: EnumTelemetryName = Field(
        title="TelemetryName",
        description=(
            "The TelemetryName of the readings. This is used to interpet the meaning of the reading "
            "values. For example, WaterTempCTimes1000 means the reading is measuring the temperature "
            "of water, in Celsius multiplied by 1000. So a value of 37000 would be a reading "
            "of 37 deg C."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/enums.html#gridworks-protocol.enums.TelemetryName)"
        ),
    )
    ValueList: List[int] = Field(
        title="List of Values",
        description="The values of the readings.",
    )
    ReadTimeUnixMsList: List[int] = Field(
        title="List of Read Times",
        description="The times that the SImpleSensor took the readings, in unix milliseconds",
    )
    TypeName: Literal["gt.sh.simple.telemetry.status"] = "gt.sh.simple.telemetry.status"
    Version: Literal["100"] = "100"

    @validator("ShNodeAlias")
    def _check_sh_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"ShNodeAlias failed LeftRightDot format validation: {e}")
        return v

    @validator("ReadTimeUnixMsList")
    def _check_read_time_unix_ms_list(cls, v: List[int]) -> List[int]:
        for elt in v:
            try:
                check_is_reasonable_unix_time_ms(elt)
            except ValueError as e:
                raise ValueError(
                    f"ReadTimeUnixMsList element {elt} failed ReasonableUnixTimeMs format validation: {e}"
                )
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: ListLengthConsistency.
        ValueList and ReadTimeUnixMsList must have the same length.
        """
        value_list: List[int] = v.get("ValueList", None)
        time_list: List[int] = v.get("ReadTimeUnixMsList", None)
        if len(value_list) != len(time_list):
            raise ValueError(
                "Axiom 1: ValueList and ReadTimeUnixMsList must have the same length."
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        gt.sh.simple.telemetry.status.100 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        gt.sh.simple.telemetry.status.100 type. Unlike the standard python dict method,
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
        del d["TelemetryName"]
        d["TelemetryNameGtEnumSymbol"] = EnumTelemetryName.value_to_symbol(
            self.TelemetryName
        )
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the gt.sh.simple.telemetry.status.100 representation.

        Instances in the class are python-native representations of gt.sh.simple.telemetry.status.100
        objects, while the actual gt.sh.simple.telemetry.status.100 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is GtShSimpleTelemetryStatus.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class GtShSimpleTelemetryStatus100_Maker:
    type_name = "gt.sh.simple.telemetry.status"
    version = "100"

    def __init__(
        self,
        sh_node_alias: str,
        telemetry_name: EnumTelemetryName,
        value_list: List[int],
        read_time_unix_ms_list: List[int],
    ):
        self.tuple = GtShSimpleTelemetryStatus100(
            ShNodeAlias=sh_node_alias,
            TelemetryName=telemetry_name,
            ValueList=value_list,
            ReadTimeUnixMsList=read_time_unix_ms_list,
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShSimpleTelemetryStatus100) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> GtShSimpleTelemetryStatus100:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> GtShSimpleTelemetryStatus100:
        """
        Deserialize a dictionary representation of a gt.sh.simple.telemetry.status.100 message object
        into a GtShSimpleTelemetryStatus python object for internal use.

        This is the near-inverse of the GtShSimpleTelemetryStatus.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a GtShSimpleTelemetryStatus object.

        Returns:
            GtShSimpleTelemetryStatus
        """
        d2 = dict(d)
        if "ShNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing ShNodeAlias: <{d2}>")
        if "TelemetryNameGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"TelemetryNameGtEnumSymbol missing from dict <{d2}>")
        value = EnumTelemetryName.symbol_to_value(d2["TelemetryNameGtEnumSymbol"])
        d2["TelemetryName"] = EnumTelemetryName(value)
        if "ValueList" not in d2.keys():
            raise SchemaError(f"dict missing ValueList: <{d2}>")
        if "ReadTimeUnixMsList" not in d2.keys():
            raise SchemaError(f"dict missing ReadTimeUnixMsList: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "100":
            LOGGER.debug(
                f"Attempting to interpret gt.sh.simple.telemetry.status version {d2['Version']} as version 100"
            )
            d2["Version"] = "100"
        return GtShSimpleTelemetryStatus100(**d2)


def check_is_left_right_dot(v: str) -> None:
    """Checks LeftRightDot Format

    LeftRightDot format: Lowercase alphanumeric words separated by periods, with
    the most significant word (on the left) starting with an alphabet character.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate <{v}> into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of <{v}> must start with alphabet char."
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of <{v}> split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of <{v}> must be lowercase.")


def check_is_reasonable_unix_time_ms(v: int) -> None:
    """Checks ReasonableUnixTimeMs format

    ReasonableUnixTimeMs format: unix milliseconds between Jan 1 2000 and Jan 1 3000

    Args:
        v (int): the candidate

    Raises:
        ValueError: if v is not ReasonableUnixTimeMs format
    """
    import pendulum

    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp * 1000 > v:  # type: ignore[attr-defined]
        raise ValueError(f"<{v}> must be after Jan 1 2000")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp * 1000 < v:  # type: ignore[attr-defined]
        raise ValueError(f"<{v}> must be before Jan 1 3000")
