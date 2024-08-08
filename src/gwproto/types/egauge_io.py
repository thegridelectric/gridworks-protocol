"""Type egauge.io, version 001"""

import json
import logging
import os
from typing import Any, Dict, Literal

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, Field, field_validator

from gwproto.types.egauge_register_config import (
    EgaugeRegisterConfig,
    EgaugeRegisterConfigMaker,
)

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class EgaugeIo(BaseModel):
    """
    Used for an eGauge meter's component information in a hardware layout.

    When the component associated to a PowerMeter ShNode has MakeModel EGAUGE__4030, there is
    a significant amount of configuration required to specify both what is read from the eGauge
    (input) and what is then sent up to the SCADA (output). This type handles that information.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/egauge-io.html)
    """

    channel_name: str = Field(
        title="Name of the Data Channel",
        description=(
            "Each input on the egauge is associated with a unique Data Channel (for example, "
            "TelemetryName PowerW, AboutNodeName hp-idu-pwr, CapturedByNodeName pwr-meter). The "
            "Data Channel's name is meant to be an easy-to-read immutable and (locally to the "
            "SCADA) unique identifier. Stylistically, when there is no ambiguity about what node "
            "is capturing the data or what the telemetry name is, choose the data channel's name "
            "as the AboutNodeName (e.g. hp-idu-pwr)."
        ),
    )
    input_config: EgaugeRegisterConfig = Field(
        title="Input config for one channel of data for a specific eGauge meter",
        description=(
            "This is the data available from the modbus csv map provided by eGauge for this component, "
            "for example http://egauge14875.egaug.es/6001C/settings.html for a eGauge device "
            "with ID 14875"
        ),
    )
    type_name: Literal["egauge.io"] = "egauge.io"
    version: Literal["001"] = "001"

    class Config:
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
        d["InputConfig"] = self.input_config.as_dict()
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
        d["InputConfig"] = self.input_config.as_dict()
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the egauge.io.001 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class EgaugeIoMaker:
    type_name = "egauge.io"
    version = "001"

    @classmethod
    def tuple_to_type(cls, tuple: EgaugeIo) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> EgaugeIo:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a egauge.io.001 type

        Returns:
            EgaugeIo instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> EgaugeIo:
        """
        Translates a dict representation of a egauge.io.001 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "ChannelName" not in d2.keys():
            raise GwTypeError(f"dict missing ChannelName: <{d2}>")
        if "InputConfig" not in d2.keys():
            raise GwTypeError(f"dict missing InputConfig: <{d2}>")
        if not isinstance(d2["InputConfig"], dict):
            raise GwTypeError(
                f"InputConfig <{d2['InputConfig']}> must be a EgaugeRegisterConfig!"
            )
        input_config = EgaugeRegisterConfigMaker.dict_to_tuple(d2["InputConfig"])
        d2["InputConfig"] = input_config
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret egauge.io version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return EgaugeIo(**d3)


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
