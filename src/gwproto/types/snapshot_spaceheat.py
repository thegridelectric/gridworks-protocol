"""Type snapshot.spaceheat, version 001"""
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
from gwproto.types.single_reading import SingleReading
from gwproto.types.single_reading import SingleReading_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class Snapshot(BaseModel):
    """
    Snapshot.

    Collection of all the latest measurements (timestamped) captured by the SCADA for all of
    its data channels.
    """

    FromGNodeAlias: str = Field(
        title="FromGNodeAlias",
    )
    FromGNodeInstanceId: str = Field(
        title="FromGNodeInstanceId",
    )
    SnapshotTimeUnixMs: int = Field(
        title="SnapshotTimeUnixMs",
        description="The time at which the snapshot was put together.",
    )
    LatestReadingList: List[SingleReading] = Field(
        title="LatestReadingList",
        description=(
            "The most up-to-date values the SCADA has for all channels, with timestamps of when "
            "they were last updated."
        ),
    )
    TypeName: Literal["snapshot.spaceheat"] = "snapshot.spaceheat"
    Version: Literal["001"] = "001"

    @validator("FromGNodeAlias")
    def _check_from_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("FromGNodeInstanceId")
    def _check_from_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("SnapshotTimeUnixMs")
    def _check_snapshot_time_unix_ms(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_ms(v)
        except ValueError as e:
            raise ValueError(
                f"SnapshotTimeUnixMs failed ReasonableUnixTimeMs format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        snapshot.spaceheat.001 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        snapshot.spaceheat.001 type. Unlike the standard python dict method,
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
        latest_reading_list = []
        for elt in self.LatestReadingList:
            latest_reading_list.append(elt.as_dict())
        d["LatestReadingList"] = latest_reading_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the snapshot.spaceheat.001 representation.

        Instances in the class are python-native representations of snapshot.spaceheat.001
        objects, while the actual snapshot.spaceheat.001 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is Snapshot.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class Snapshot_Maker:
    type_name = "snapshot.spaceheat"
    version = "001"

    @classmethod
    def tuple_to_type(cls, tuple: Snapshot) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> Snapshot:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> Snapshot:
        """
        Deserialize a dictionary representation of a snapshot.spaceheat.001 message object
        into a Snapshot python object for internal use.

        This is the near-inverse of the Snapshot.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a Snapshot object.

        Returns:
            Snapshot
        """
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeAlias: <{d2}>")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeInstanceId: <{d2}>")
        if "SnapshotTimeUnixMs" not in d2.keys():
            raise SchemaError(f"dict missing SnapshotTimeUnixMs: <{d2}>")
        if "LatestReadingList" not in d2.keys():
            raise SchemaError(f"dict missing LatestReadingList: <{d2}>")
        if not isinstance(d2["LatestReadingList"], List):
            raise SchemaError(
                f"LatestReadingList <{d2['LatestReadingList']}> must be a List!"
            )
        latest_reading_list = []
        for elt in d2["LatestReadingList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"LatestReadingList <{d2['LatestReadingList']}> must be a List of SingleReading types"
                )
            t = SingleReading_Maker.dict_to_tuple(elt)
            latest_reading_list.append(t)
        d2["LatestReadingList"] = latest_reading_list
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret snapshot.spaceheat version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        return Snapshot(**d2)


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
