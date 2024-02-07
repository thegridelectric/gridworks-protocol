"""Type thermistor.data.processing.config, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import validator

from gwproto.enums import ThermistorDataMethod
from gwproto.errors import SchemaError
from gwproto.types.telemetry_reporting_config import TelemetryReportingConfig
from gwproto.types.telemetry_reporting_config import TelemetryReportingConfig_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class ThermistorDataProcessingConfig(BaseModel):
    """
    How does polled raw data get turned into a captured temperature reading? This config type
    provides that information.
    """

    TerminalBlockIdx: int = Field(
        title="Terminal Block Index",
        description=(
            "If the reading Node uses terminal blocks for inputs (e.g. thermistors or current "
            "transformers), and it has multiple terminal blocks, then one needs to know which "
            "terminal block to read. For example, al Ads111xBasedComponents use this."
        ),
    )
    ReportingConfig: TelemetryReportingConfig = Field(
        title="Telemetry Reporting Config",
        description=(
            "This includes the standard non-thermistor-specific reporting configuration data."
        ),
    )
    DataProcessingMethod: Optional[ThermistorDataMethod] = Field(
        title="Data Processing Method",
        description=(
            "What method is used to go from polled raw voltage to captured temperature readings? "
            "Not applicable if the data channel is voltage."
        ),
        default=None,
    )
    DataProcessingDescription: Optional[str] = Field(
        title="Data Processing Description",
        description=(
            "Additional information to flesh out and articulate the data processing method enum. "
            "For example, if the method is an exponential weighted average of temperature readings "
            "achieved with the beta formula, how is the weighting determined?"
        ),
        default=None,
    )
    TypeName: Literal[
        "thermistor.data.processing.config"
    ] = "thermistor.data.processing.config"
    Version: Literal["000"] = "000"

    class Config:
        extra = Extra.allow

    @validator("TerminalBlockIdx")
    def _check_terminal_block_idx(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"TerminalBlockIdx failed PositiveInteger format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        thermistor.data.processing.config.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        thermistor.data.processing.config.000 type. Unlike the standard python dict method,
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
        d["ReportingConfig"] = self.ReportingConfig.as_dict()
        if "DataProcessingMethod" in d.keys():
            del d["DataProcessingMethod"]
            d[
                "DataProcessingMethodGtEnumSymbol"
            ] = ThermistorDataMethod.value_to_symbol(self.DataProcessingMethod)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the thermistor.data.processing.config.000 representation.

        Instances in the class are python-native representations of thermistor.data.processing.config.000
        objects, while the actual thermistor.data.processing.config.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is ThermistorDataProcessingConfig.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ThermistorDataProcessingConfig_Maker:
    type_name = "thermistor.data.processing.config"
    version = "000"

    def __init__(
        self,
        terminal_block_idx: int,
        reporting_config: TelemetryReportingConfig,
        data_processing_method: Optional[ThermistorDataMethod],
        data_processing_description: Optional[str],
    ):
        self.tuple = ThermistorDataProcessingConfig(
            TerminalBlockIdx=terminal_block_idx,
            ReportingConfig=reporting_config,
            DataProcessingMethod=data_processing_method,
            DataProcessingDescription=data_processing_description,
        )

    @classmethod
    def tuple_to_type(cls, tuple: ThermistorDataProcessingConfig) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> ThermistorDataProcessingConfig:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> ThermistorDataProcessingConfig:
        """
        Deserialize a dictionary representation of a thermistor.data.processing.config.000 message object
        into a ThermistorDataProcessingConfig python object for internal use.

        This is the near-inverse of the ThermistorDataProcessingConfig.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a ThermistorDataProcessingConfig object.

        Returns:
            ThermistorDataProcessingConfig
        """
        d2 = dict(d)
        if "TerminalBlockIdx" not in d2.keys():
            raise SchemaError(f"dict missing TerminalBlockIdx: <{d2}>")
        if "ReportingConfig" not in d2.keys():
            raise SchemaError(f"dict missing ReportingConfig: <{d2}>")
        if not isinstance(d2["ReportingConfig"], dict):
            raise SchemaError(
                f"ReportingConfig <{d2['ReportingConfig']}> must be a TelemetryReportingConfig!"
            )
        reporting_config = TelemetryReportingConfig_Maker.dict_to_tuple(
            d2["ReportingConfig"]
        )
        d2["ReportingConfig"] = reporting_config
        if "DataProcessingMethod" in d2.keys():
            value = ThermistorDataMethod.symbol_to_value(
                d2["DataProcessingMethodGtEnumSymbol"]
            )
            d2["DataProcessingMethod"] = ThermistorDataMethod(value)
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret thermistor.data.processing.config version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return ThermistorDataProcessingConfig(**d2)


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
