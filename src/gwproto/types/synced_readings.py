"""Type synced.readings, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from gwproto.errors import SchemaError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class SyncedReadings(BaseModel):
    """
    A set of readings made at the same time by a multipurpose sensor, sent by SpaceheatNode
    actor capturing the data (which will be associated to some sort of multipurpose sensing
    component). The nth element of each of its three readings are coupled: AboutNodeName, what
    the value is, what the TelemetryName is.
    """

    ScadaReadTimeUnixMs: int = Field(
        title="ScadaReadTime in Unix MilliSeconds",
        description="The single time, in unix milliseconds, assigned to this list of readings.",
    )
    ChannelNameList: List[str] = Field(
        title="Channel Name List",
        description=(
            "List of the names of the Data Channels getting measured. These names are immutable "
            "and locally unique for the Scada."
        ),
    )
    ValueList: List[int] = Field(
        title="ValueList",
        description="List of the values read.",
    )
    TypeName: Literal["synced.readings"] = "synced.readings"
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

    @validator("ChannelNameList")
    def _check_channel_name_list(cls, v: List[str]) -> List[str]:
        for elt in v:
            try:
                check_is_spaceheat_name(elt)
            except ValueError as e:
                raise ValueError(
                    f"ChannelNameList element {elt} failed SpaceheatName format validation: {e}"
                )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        synced.readings.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        synced.readings.000 type. Unlike the standard python dict method,
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
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the synced.readings.000 representation.

        Instances in the class are python-native representations of synced.readings.000
        objects, while the actual synced.readings.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is SyncedReadings.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class SyncedReadings_Maker:
    type_name = "synced.readings"
    version = "000"

    def __init__(
        self,
        scada_read_time_unix_ms: int,
        channel_name_list: List[str],
        value_list: List[int],
    ):
        self.tuple = SyncedReadings(
            ScadaReadTimeUnixMs=scada_read_time_unix_ms,
            ChannelNameList=channel_name_list,
            ValueList=value_list,
        )

    @classmethod
    def tuple_to_type(cls, tuple: SyncedReadings) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> SyncedReadings:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> SyncedReadings:
        """
        Deserialize a dictionary representation of a synced.readings.000 message object
        into a SyncedReadings python object for internal use.

        This is the near-inverse of the SyncedReadings.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a SyncedReadings object.

        Returns:
            SyncedReadings
        """
        d2 = dict(d)
        if "ScadaReadTimeUnixMs" not in d2.keys():
            raise SchemaError(f"dict missing ScadaReadTimeUnixMs: <{d2}>")
        if "ChannelNameList" not in d2.keys():
            raise SchemaError(f"dict missing ChannelNameList: <{d2}>")
        if "ValueList" not in d2.keys():
            raise SchemaError(f"dict missing ValueList: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret synced.readings version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return SyncedReadings(**d2)


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


def check_is_spaceheat_name(v: str) -> None:
    """Check SpaceheatName Format.

    Validates if the provided string adheres to the SpaceheatName format:
    Lowercase words separated by periods, where word characters can be alphanumeric
    or a hyphen, and the first word starts with an alphabet character.

    Args:
        candidate (str): The string to be validated.

    Raises:
        ValueError: If the provided string is not in SpaceheatName format.
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
        for char in word:
            if not (char.isalnum() or char == '-'):
                raise ValueError(f"words of <{v}> split by by '.' must be alphanumeric or hyphen.")
    if not v.islower():
        raise ValueError(f"<{v}> must be lowercase.")
