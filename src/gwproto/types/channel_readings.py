"""Type channel.readings, version 000"""
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


class ChannelReadings(BaseModel):
    """
    A list of timestamped readings (values) for a data channel (AboutName, CapturedByName, TelemetryName).
    """

    DataChannel: DataChannel = Field(
        title="Data Channel",
        description=(
            "The Data Channel that this batch of timestamped values is about."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-node.html)"
        ),
    )
    ValueList: List[int] = Field(
        title="List of Values",
        description="The values of the readings.",
    )
    ScadaReadTimeUnixMsList: List[int] = Field(
        title="List of Read Times",
        description="The times that the MultipurposeSensor took the readings, in unix milliseconds",
    )
    TypeName: Literal["channel.readings"] = "channel.readings"
    Version: Literal["000"] = "000"

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
        ValueList and ReadTimeUnixMsList must have the same length.
        """
        # TODO: Implement check for axiom 1"
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        channel.readings.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        channel.readings.000 type. Unlike the standard python dict method,
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
        d["DataChannel"] = self.DataChannel.as_dict()
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the channel.readings.000 representation.

        Instances in the class are python-native representations of channel.readings.000
        objects, while the actual channel.readings.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is ChannelReadings.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ChannelReadings_Maker:
    type_name = "channel.readings"
    version = "000"

    def __init__(
        self,
        data_channel: DataChannel,
        value_list: List[int],
        scada_read_time_unix_ms_list: List[int],
    ):
        self.tuple = ChannelReadings(
            DataChannel=data_channel,
            ValueList=value_list,
            ScadaReadTimeUnixMsList=scada_read_time_unix_ms_list,
        )

    @classmethod
    def tuple_to_type(cls, tuple: ChannelReadings) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> ChannelReadings:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> ChannelReadings:
        """
        Deserialize a dictionary representation of a channel.readings.000 message object
        into a ChannelReadings python object for internal use.

        This is the near-inverse of the ChannelReadings.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a ChannelReadings object.

        Returns:
            ChannelReadings
        """
        d2 = dict(d)
        if "DataChannel" not in d2.keys():
            raise SchemaError(f"dict missing DataChannel: <{d2}>")
        if not isinstance(d2["DataChannel"], dict):
            raise SchemaError(
                f"DataChannel <{d2['DataChannel']}> must be a DataChannel!"
            )
        data_channel = DataChannel_Maker.dict_to_tuple(d2["DataChannel"])
        d2["DataChannel"] = data_channel
        if "ValueList" not in d2.keys():
            raise SchemaError(f"dict missing ValueList: <{d2}>")
        if "ScadaReadTimeUnixMsList" not in d2.keys():
            raise SchemaError(f"dict missing ScadaReadTimeUnixMsList: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret channel.readings version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return ChannelReadings(**d2)


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
