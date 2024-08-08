"""Type thermistor.data.processing.config, version 000"""

import json
import logging
import os
from typing import Any, Dict, Literal, Optional

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, Field, field_validator

from gwproto.enums import MakeModel, ThermistorDataMethod

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

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

    channel_name: str = Field(
        title="Channel Name",
        description="The name of the data channel associated with this thermistor",
    )
    terminal_block_idx: int = Field(
        title="Terminal Block Index",
        description=(
            "If the reading Node uses terminal blocks for inputs (e.g. thermistors or current "
            "transformers), and it has multiple terminal blocks, then one needs to know which "
            "terminal block to read. For example, al Ads111xBasedComponents use this."
        ),
    )
    thermistor_make_model: MakeModel = Field(
        title="Thermistor MakeModel",
        description="The Make/Model of the thermistor attached to this terminal block.",
    )
    data_processing_method: Optional[ThermistorDataMethod] = Field(
        title="Data Processing Method",
        description=(
            "What method is used to go from polled raw voltage to captured temperature readings? "
            "Not applicable if the data channel is voltage."
        ),
        default=None,
    )
    data_processing_description: Optional[str] = Field(
        title="Data Processing Description",
        description=(
            "Additional information to flesh out and articulate the data processing method enum. "
            "For example, if the method is an exponential weighted average of temperature readings "
            "achieved with the beta formula, how is the weighting determined?"
        ),
        default=None,
    )
    type_name: Literal["thermistor.data.processing.config"] = (
        "thermistor.data.processing.config"
    )
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

    @field_validator("terminal_block_idx")
    @classmethod
    def _check_terminal_block_idx(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(
                f"TerminalBlockIdx failed PositiveInteger format validation: {e}",
            ) from e
        return v

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
        d["ThermistorMakeModel"] = d["ThermistorMakeModel"].value
        if "DataProcessingMethod" in d.keys():
            d["DataProcessingMethod"] = d["DataProcessingMethod"].value
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
        del d["ThermistorMakeModel"]
        d["ThermistorMakeModelGtEnumSymbol"] = MakeModel.value_to_symbol(
            self.thermistor_make_model
        )
        if "DataProcessingMethod" in d.keys():
            del d["DataProcessingMethod"]
            d["DataProcessingMethodGtEnumSymbol"] = (
                ThermistorDataMethod.value_to_symbol(self.data_processing_method)
            )
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the thermistor.data.processing.config.000 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class ThermistorDataProcessingConfigMaker:
    type_name = "thermistor.data.processing.config"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: ThermistorDataProcessingConfig) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> ThermistorDataProcessingConfig:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a thermistor.data.processing.config.000 type

        Returns:
            ThermistorDataProcessingConfig instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ThermistorDataProcessingConfig:
        """
        Translates a dict representation of a thermistor.data.processing.config.000 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "ChannelName" not in d2.keys():
            raise GwTypeError(f"dict missing ChannelName: <{d2}>")
        if "TerminalBlockIdx" not in d2.keys():
            raise GwTypeError(f"dict missing TerminalBlockIdx: <{d2}>")
        if "ThermistorMakeModelGtEnumSymbol" in d2.keys():
            value = MakeModel.symbol_to_value(d2["ThermistorMakeModelGtEnumSymbol"])
            d2["ThermistorMakeModel"] = MakeModel(value)
            del d2["ThermistorMakeModelGtEnumSymbol"]
        elif "ThermistorMakeModel" in d2.keys():
            if d2["ThermistorMakeModel"] not in MakeModel.values():
                d2["ThermistorMakeModel"] = MakeModel.default()
            else:
                d2["ThermistorMakeModel"] = MakeModel(d2["ThermistorMakeModel"])
        else:
            raise GwTypeError(
                f"both ThermistorMakeModelGtEnumSymbol and ThermistorMakeModel missing from dict <{d2}>",
            )
        if "DataProcessingMethod" in d2.keys():
            if d2["DataProcessingMethod"] not in ThermistorDataMethod.values():
                d2["DataProcessingMethod"] = ThermistorDataMethod.default()
            else:
                d2["DataProcessingMethod"] = ThermistorDataMethod(
                    d2["DataProcessingMethod"]
                )
        if "DataProcessingMethodGtEnumSymbol" in d2.keys():
            value = ThermistorDataMethod.symbol_to_value(
                d2["DataProcessingMethodGtEnumSymbol"]
            )
            d2["DataProcessingMethod"] = ThermistorDataMethod(value)
            del d2["DataProcessingMethodGtEnumSymbol"]
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret thermistor.data.processing.config version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return ThermistorDataProcessingConfig(**d3)


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
        x = v.split(".")
    except Exception as e:
        raise ValueError(f"Failed to seperate <{v}> into words with split'.'") from e
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
