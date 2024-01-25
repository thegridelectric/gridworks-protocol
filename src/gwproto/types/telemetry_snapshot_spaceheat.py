"""Type telemetry.snapshot.spaceheat, version 001"""
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

from gwproto.errors import SchemaError
from gwproto.types.data_channel import DataChannel
from gwproto.types.data_channel import DataChannel_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class TelemetrySnapshotSpaceheat(BaseModel):
    """
    Snapshot of Telemetry Data from a SpaceHeat SCADA.

    A snapshot of all current sensed states, sent from a spaceheat SCADA to its AtomicTNode.
    The nth element of each of the three lists refer to the same reading (i.e., what is getting
    read, what the value is, what the TelemetryNames are.)

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-node.html)
    """

    DataChannelList: List[DataChannel] = Field(
        title="Data Channel List",
        description=(
            "The list of Data Channels in the Snapshot"
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-node.html)"
        ),
    )
    ValueList: List[int] = Field(
        title="ValueList",
    )
    ScadaReadTimeUnixMsList: List[int] = Field(
        title="ReportTimeUnixMs",
        description="The time, in unix ms, that each reading was taken.",
    )
    TypeName: Literal["telemetry.snapshot.spaceheat"] = "telemetry.snapshot.spaceheat"
    Version: Literal["001"] = "001"

    @validator("ScadaReadTimeUnixMsList")
    def _check_scada_read_time_unix_ms_list(cls, v: List[int]) -> List[int]:
        for elt in v:
            try:
                check_is_reasonable_unix_time_ms(elt)
            except ValueError as e:
                raise ValueError(
                    f"ScadaReadTimeUnixMsList element {elt} failed ReasonableUnixTimeMs format validation: {e}"
                )
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: ListLengthConsistency.
        DataChannelList, ValueList, and ScadaReadTimeUnixMs must all have the same length.
        """
        # TODO: Implement check for axiom 1"
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        telemetry.snapshot.spaceheat.001 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        telemetry.snapshot.spaceheat.001 type. Unlike the standard python dict method,
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
        data_channel_list = []
        for elt in self.DataChannelList:
            data_channel_list.append(elt.as_dict())
        d["DataChannelList"] = data_channel_list
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the telemetry.snapshot.spaceheat.001 representation.

        Instances in the class are python-native representations of telemetry.snapshot.spaceheat.001
        objects, while the actual telemetry.snapshot.spaceheat.001 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is TelemetrySnapshotSpaceheat.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class TelemetrySnapshotSpaceheat_Maker:
    type_name = "telemetry.snapshot.spaceheat"
    version = "001"

    def __init__(
        self,
        data_channel_list: List[DataChannel],
        value_list: List[int],
        scada_read_time_unix_ms_list: List[int],
    ):
        self.tuple = TelemetrySnapshotSpaceheat(
            DataChannelList=data_channel_list,
            ValueList=value_list,
            ScadaReadTimeUnixMsList=scada_read_time_unix_ms_list,
        )

    @classmethod
    def tuple_to_type(cls, tuple: TelemetrySnapshotSpaceheat) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> TelemetrySnapshotSpaceheat:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> TelemetrySnapshotSpaceheat:
        """
        Deserialize a dictionary representation of a telemetry.snapshot.spaceheat.001 message object
        into a TelemetrySnapshotSpaceheat python object for internal use.

        This is the near-inverse of the TelemetrySnapshotSpaceheat.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a TelemetrySnapshotSpaceheat object.

        Returns:
            TelemetrySnapshotSpaceheat
        """
        d2 = dict(d)
        if "DataChannelList" not in d2.keys():
            raise SchemaError(f"dict missing DataChannelList: <{d2}>")
        if not isinstance(d2["DataChannelList"], List):
            raise SchemaError(
                f"DataChannelList <{d2['DataChannelList']}> must be a List!"
            )
        data_channel_list = []
        for elt in d2["DataChannelList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"DataChannelList <{d2['DataChannelList']}> must be a List of DataChannel types"
                )
            t = DataChannel_Maker.dict_to_tuple(elt)
            data_channel_list.append(t)
        d2["DataChannelList"] = data_channel_list
        if "ValueList" not in d2.keys():
            raise SchemaError(f"dict missing ValueList: <{d2}>")
        if "ScadaReadTimeUnixMsList" not in d2.keys():
            raise SchemaError(f"dict missing ScadaReadTimeUnixMsList: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret telemetry.snapshot.spaceheat version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        return TelemetrySnapshotSpaceheat(**d2)
