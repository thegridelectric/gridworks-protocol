"""Type channel.config, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gwproto.enums import Unit as EnumUnit
from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class ChannelConfig(BaseModel):
    """
    Channel Configuration.

    Configuration data used to articulate how time series data is polled and captured for a
    particular channel. ExtraAllowed. Replace the ambigious "SamplePeriodS" with "CapturePeriodS"
    and "PollPeriodMs" added.
    """

    ChannelName: str = Field(
        title="Data Channel Name",
        description=(
            "The (locally unique, immutable) name of the Data Channel to which the configuration "
            "applies (What node is getting read, what telemetry name is getting read, and what "
            "node is doing the reading)."
        ),
    )
    PollPeriodMs: int = Field(
        title="Poll Period in Milliseconds",
        description=(
            "Poll Period refers to the period of time between two readings by the local actor. "
            "This is in contrast to Capture Period, which refers to the period between readings "
            "that are sent up to the cloud (or otherwise saved for the long-term)."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/data-polling-capturing-transmitting.rst)"
        ),
    )
    CapturePeriodS: int = Field(
        title="Capture Period Seconds",
        description=(
            "This telemetry data channel will capture data periodically, at this rate. It will "
            "be shared (although not necessarily immediately) with the AtomicTNode. The capture "
            "period must be longer than the poll period. If the channel is also capturing on "
            "change, those asynchronous reports do not reset this period."
        ),
    )
    AsyncCapture: bool = Field(
        title="Asynchronous Capture",
        description=(
            "Set CaptureOnChange to true for asynchronous reporting of captured data, in addition "
            "to the synchronous periodic capture reflected by the CapturePeriodS."
        ),
    )
    AsyncCaptureDelta: Optional[int] = Field(
        title="Asynchronous Capture Delta",
        description=(
            "Represents the threshold or minimum change in value required for asynchronous reporting "
            "of telemetry data, assuming CaptureOnChange. For example, if TelemetryName is WaterTempCTimes1000 "
            "and one wants 0.25 deg C to trigger a new capture, then this would be set to 250."
        ),
        default=None,
    )
    Exponent: int = Field(
        title="Exponent",
        description=(
            "Say the TelemetryName is WaterTempCTimes1000; this corresponds to units of Celsius. "
            "To match the implication in the name, the Exponent should be 3, and a Value of 65300 "
            "would indicate 65.3 deg C"
        ),
    )
    Unit: EnumUnit = Field(
        title="Unit",
        description="Say TelemetryName is WaterTempCTimes1000. The unit would be Celcius.",
    )
    TypeName: Literal["channel.config"] = "channel.config"
    Version: Literal["000"] = "000"

    class Config:
        extra = Extra.allow

    @validator("ChannelName")
    def _check_channel_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"ChannelName failed SpaceheatName format validation: {e}")
        return v

    @validator("PollPeriodMs")
    def _check_poll_period_ms(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"PollPeriodMs failed PositiveInteger format validation: {e}"
            )
        return v

    @validator("CapturePeriodS")
    def _check_capture_period_s(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"CapturePeriodS failed PositiveInteger format validation: {e}"
            )
        return v

    @validator("AsyncCaptureDelta")
    def _check_async_capture_delta(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"AsyncCaptureDelta failed PositiveInteger format validation: {e}"
            )
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Async Capture Consistency.
        If ReportOnChange is true, then AsyncReportThreshold and NameplateMaxValue also exist.
        """
        # TODO: Implement check for axiom 1"
        return v

    @root_validator
    def check_axiom_2(cls, v: dict) -> dict:
        """
        Axiom 2: Capture and Polling Consistency.
        CapturePeriodMs (CapturePeriodS * 1000) must be larger than PollPeriodMs. If CapturePeriodMs < 10 * PollPeriodMs then CapturePeriodMs must be a multiple of PollPeriodMs.
        """
        # TODO: Implement check for axiom 2"
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        channel.config.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        channel.config.000 type. Unlike the standard python dict method,
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
        del d["Unit"]
        d["UnitGtEnumSymbol"] = EnumUnit.value_to_symbol(self.Unit)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the channel.config.000 representation.

        Instances in the class are python-native representations of channel.config.000
        objects, while the actual channel.config.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is ChannelConfig.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ChannelConfig_Maker:
    type_name = "channel.config"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: ChannelConfig) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> ChannelConfig:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> ChannelConfig:
        """
        Deserialize a dictionary representation of a channel.config.000 message object
        into a ChannelConfig python object for internal use.

        This is the near-inverse of the ChannelConfig.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a ChannelConfig object.

        Returns:
            ChannelConfig
        """
        d2 = dict(d)
        if "ChannelName" not in d2.keys():
            raise SchemaError(f"dict missing ChannelName: <{d2}>")
        if "PollPeriodMs" not in d2.keys():
            raise SchemaError(f"dict missing PollPeriodMs: <{d2}>")
        if "CapturePeriodS" not in d2.keys():
            raise SchemaError(f"dict missing CapturePeriodS: <{d2}>")
        if "AsyncCapture" not in d2.keys():
            raise SchemaError(f"dict missing AsyncCapture: <{d2}>")
        if "Exponent" not in d2.keys():
            raise SchemaError(f"dict missing Exponent: <{d2}>")
        if "UnitGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"UnitGtEnumSymbol missing from dict <{d2}>")
        value = EnumUnit.symbol_to_value(d2["UnitGtEnumSymbol"])
        d2["Unit"] = EnumUnit(value)
        del d2["UnitGtEnumSymbol"]
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret channel.config version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return ChannelConfig(**d2)


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
            if not (char.isalnum() or char == "-"):
                raise ValueError(
                    f"words of <{v}> split by by '.' must be alphanumeric or hyphen."
                )
    if not v.islower():
        raise ValueError(f"<{v}> must be lowercase.")