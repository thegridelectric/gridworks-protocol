"""Type snapshot.spaceheat, version 001"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from gwproto.types.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat
from gwproto.types.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat_Maker
from gwproto.errors import SchemaError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class SnapshotSpaceheat(BaseModel):
    """
    
    """

    FromGNodeAlias: str = Field(
        title="FromGNodeAlias",
    )
    FromGNodeInstanceId: str = Field(
        title="FromGNodeInstanceId",
    )
    Snapshot: TelemetrySnapshotSpaceheat = Field(
        title="Snapshot",
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
        d["Snapshot"] = self.Snapshot.as_dict()
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

        Its near-inverse is SnapshotSpaceheat.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class SnapshotSpaceheat_Maker:
    type_name = "snapshot.spaceheat"
    version = "001"

    def __init__(
        self,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        snapshot: TelemetrySnapshotSpaceheat,
    ):
        self.tuple = SnapshotSpaceheat(
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            Snapshot=snapshot,
        )

    @classmethod
    def tuple_to_type(cls, tuple: SnapshotSpaceheat) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> SnapshotSpaceheat:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> SnapshotSpaceheat:
        """
        Deserialize a dictionary representation of a snapshot.spaceheat.001 message object
        into a SnapshotSpaceheat python object for internal use.

        This is the near-inverse of the SnapshotSpaceheat.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a SnapshotSpaceheat object.

        Returns:
            SnapshotSpaceheat
        """
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeAlias: <{d2}>")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeInstanceId: <{d2}>")
        if "Snapshot" not in d2.keys():
            raise SchemaError(f"dict missing Snapshot: <{d2}>")
        if not isinstance(d2["Snapshot"], dict):
            raise SchemaError(f"Snapshot <{d2['Snapshot']}> must be a TelemetrySnapshotSpaceheat!")
        snapshot = TelemetrySnapshotSpaceheat_Maker.dict_to_tuple(d2["Snapshot"])
        d2["Snapshot"] = snapshot
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret snapshot.spaceheat version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        return SnapshotSpaceheat(**d2)
