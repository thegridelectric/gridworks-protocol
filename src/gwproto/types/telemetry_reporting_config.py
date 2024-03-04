"""Type telemetry.reporting.config, version 001"""
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
from gwproto.enums import TelemetryName as EnumTelemetryName
from gwproto.enums import Unit as EnumUnit
from gwproto.errors import SchemaError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class TelemetryReportingConfig(BaseModel):
    """
    
    """

    AboutNodeName: str = Field(
        title="About Node Name",
        description=(
            "The name of the SpaceheatNode that is getting measured. Typically this node will "
            "have a single data channel associated to it."
        ),
    )
    TelemetryName: EnumTelemetryName = Field(
        title="Telemetry Name",
        description="The Telemetry Name associated with this config.",
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
    TypeName: Literal["telemetry.reporting.config"] = "telemetry.reporting.config"
    Version: Literal["001"] = "001"

    class Config:
        extra = Extra.allow

    @validator("AboutNodeName")
    def _check_about_node_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(
                f"AboutNodeName failed SpaceheatName format validation: {e}"
            )
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
        telemetry.reporting.config.001 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        telemetry.reporting.config.001 type. Unlike the standard python dict method,
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
        d["TelemetryNameGtEnumSymbol"] = EnumTelemetryName.value_to_symbol(self.TelemetryName)
        del d["Unit"]
        d["UnitGtEnumSymbol"] = EnumUnit.value_to_symbol(self.Unit)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the telemetry.reporting.config.001 representation.

        Instances in the class are python-native representations of telemetry.reporting.config.001
        objects, while the actual telemetry.reporting.config.001 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is TelemetryReportingConfig.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class TelemetryReportingConfig_Maker:
    type_name = "telemetry.reporting.config"
    version = "001"

    def __init__(
        self,
        about_node_name: str,
        telemetry_name: EnumTelemetryName,
        poll_period_ms: int,
        capture_period_s: int,
        async_capture: bool,
        async_capture_delta: Optional[int],
        exponent: int,
        unit: EnumUnit,
    ):
        self.tuple = TelemetryReportingConfig(
            AboutNodeName=about_node_name,
            TelemetryName=telemetry_name,
            PollPeriodMs=poll_period_ms,
            CapturePeriodS=capture_period_s,
            AsyncCapture=async_capture,
            AsyncCaptureDelta=async_capture_delta,
            Exponent=exponent,
            Unit=unit,
        )

    @classmethod
    def tuple_to_type(cls, tuple: TelemetryReportingConfig) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> TelemetryReportingConfig:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> TelemetryReportingConfig:
        """
        Deserialize a dictionary representation of a telemetry.reporting.config.001 message object
        into a TelemetryReportingConfig python object for internal use.

        This is the near-inverse of the TelemetryReportingConfig.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a TelemetryReportingConfig object.

        Returns:
            TelemetryReportingConfig
        """
        d2 = dict(d)
        if "AboutNodeName" not in d2.keys():
            raise SchemaError(f"dict missing AboutNodeName: <{d2}>")
        if "TelemetryNameGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"TelemetryNameGtEnumSymbol missing from dict <{d2}>")
        value = EnumTelemetryName.symbol_to_value(d2["TelemetryNameGtEnumSymbol"])
        d2["TelemetryName"] = EnumTelemetryName(value)
        del d2["TelemetryNameGtEnumSymbol"]
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
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret telemetry.reporting.config version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        return TelemetryReportingConfig(**d2)


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
            if not (char.isalnum() or char == '-'):
                raise ValueError(f"words of <{v}> split by by '.' must be alphanumeric or hyphen.")
    if not v.islower():
        raise ValueError(f"<{v}> must be lowercase.")
