"""Type channel.config, version 000"""

import json
import logging
import os
from typing import Any, Dict, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, Field, field_validator, model_validator
from typing_extensions import Self

from gwproto.enums import Unit

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

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

    channel_name: str = Field(
        title="Data Channel Name",
        description=(
            "The (locally unique, immutable) name of the Data Channel to which the configuration "
            "applies (What node is getting read, what telemetry name is getting read, and what "
            "node is doing the reading)."
        ),
    )
    poll_period_ms: int = Field(
        title="Poll Period in Milliseconds",
        description=(
            "Poll Period refers to the period of time between two readings by the local actor. "
            "This is in contrast to Capture Period, which refers to the period between readings "
            "that are sent up to the cloud (or otherwise saved for the long-term)."
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/data-polling-capturing-transmitting.rst)"
        ),
    )
    capture_period_s: int = Field(
        title="Capture Period Seconds",
        description=(
            "This telemetry data channel will capture data periodically, at this rate. It will "
            "be shared (although not necessarily immediately) with the AtomicTNode. The capture "
            "period must be longer than the poll period. If the channel is also capturing on "
            "change, those asynchronous reports do not reset this period."
        ),
    )
    async_capture: bool = Field(
        title="Asynchronous Capture",
        description=(
            "Set CaptureOnChange to true for asynchronous reporting of captured data, in addition "
            "to the synchronous periodic capture reflected by the CapturePeriodS."
        ),
    )
    async_capture_delta: Optional[int] = Field(
        title="Asynchronous Capture Delta",
        description=(
            "Represents the threshold or minimum change in value required for asynchronous reporting "
            "of telemetry data, assuming CaptureOnChange. For example, if TelemetryName is WaterTempCTimes1000 "
            "and one wants 0.25 deg C to trigger a new capture, then this would be set to 250."
        ),
        default=None,
    )
    exponent: int = Field(
        title="Exponent",
        description=(
            "Say the TelemetryName is WaterTempCTimes1000; this corresponds to units of Celsius. "
            "To match the implication in the name, the Exponent should be 3, and a Value of 65300 "
            "would indicate 65.3 deg C"
        ),
    )
    unit: Unit = Field(
        title="Unit",
        description="Say TelemetryName is WaterTempCTimes1000. The unit would be Celcius.",
    )
    type_name: Literal["channel.config"] = "channel.config"
    version: Literal["000"] = "000"

    class Config:
        extra = "allow"
        populate_by_name = True
        alias_generator = snake_to_pascal

    @field_validator("channel_name")
    @classmethod
    def _check_channel_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(
                f"ChannelName failed SpaceheatName format validation: {e}"
            ) from e
        return v

    @field_validator("poll_period_ms")
    @classmethod
    def _check_poll_period_ms(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"PollPeriodMs failed PositiveInteger format validation: {e}",
            ) from e
        return v

    @field_validator("capture_period_s")
    @classmethod
    def _check_capture_period_s(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"CapturePeriodS failed PositiveInteger format validation: {e}",
            ) from e
        return v

    @field_validator("async_capture_delta")
    @classmethod
    def _check_async_capture_delta(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"AsyncCaptureDelta failed PositiveInteger format validation: {e}",
            ) from e
        return v

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Async Capture Consistency.
        If AsyncCapture is True, then AsyncCaptureDelta exists
        """
        # TODO: Implement check for axiom 1"
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: Capture and Polling Consistency.
        CapturePeriodMs (CapturePeriodS * 1000) must be larger than PollPeriodMs. If CapturePeriodMs < 10 * PollPeriodMs then CapturePeriodMs must be a multiple of PollPeriodMs.
        """
        # TODO: Implement check for axiom 2"
        return self

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
        d["Unit"] = d["Unit"].value
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
        del d["Unit"]
        d["UnitGtEnumSymbol"] = Unit.value_to_symbol(self.unit)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the channel.config.000 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ChannelConfigMaker:
    type_name = "channel.config"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: ChannelConfig) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> ChannelConfig:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a channel.config.000 type

        Returns:
            ChannelConfig instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ChannelConfig:
        """
        Translates a dict representation of a channel.config.000 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "ChannelName" not in d2.keys():
            raise GwTypeError(f"dict missing ChannelName: <{d2}>")
        if "PollPeriodMs" not in d2.keys():
            raise GwTypeError(f"dict missing PollPeriodMs: <{d2}>")
        if "CapturePeriodS" not in d2.keys():
            raise GwTypeError(f"dict missing CapturePeriodS: <{d2}>")
        if "AsyncCapture" not in d2.keys():
            raise GwTypeError(f"dict missing AsyncCapture: <{d2}>")
        if "Exponent" not in d2.keys():
            raise GwTypeError(f"dict missing Exponent: <{d2}>")
        if "UnitGtEnumSymbol" in d2.keys():
            value = Unit.symbol_to_value(d2["UnitGtEnumSymbol"])
            d2["Unit"] = Unit(value)
            del d2["UnitGtEnumSymbol"]
        elif "Unit" in d2.keys():
            if d2["Unit"] not in Unit.values():
                d2["Unit"] = Unit.default()
            else:
                d2["Unit"] = Unit(d2["Unit"])
        else:
            raise GwTypeError(
                f"both UnitGtEnumSymbol and Unit missing from dict <{d2}>",
            )
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret channel.config version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return ChannelConfig(**d3)


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
    Lowercase alphanumeric words separated by hypens

    Args:
        candidate (str): The string to be validated.

    Raises:
        ValueError: If the provided string is not in SpaceheatName format.
    """
    try:
        x = v.split("-")
    except Exception as e:
        raise ValueError(f"Failed to seperate <{v}> into words with split'-'") from e
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of <{v}> must start with alphabet char."
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of <{v}> split by by '-' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of <{v}> must be lowercase.")
