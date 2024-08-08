"""Type egauge.register.config, version 000"""

import json
import logging
import os
from typing import Any, Dict, Literal

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, Field

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class EgaugeRegisterConfig(BaseModel):
    """
    Used to translate eGauge's Modbus Map.

    This type captures the information provided by eGauge in its modbus csv map, when reading
    current, power, energy, voltage, frequency etc from an eGauge 4030.
    """

    address: int = Field(
        title="Address",
        description=(
            "EGauge's modbus holding address. Note that the EGauge modbus map for holding address "
            "100 will be 30100 - the '+30000' indicates it is a holding address. We use the 4-digit "
            "address after the '3'."
        ),
    )
    name: str = Field(
        title="Name",
        description=(
            "The name assigned in the EGauge's modbus map. This is configured by the user (see "
            "URL)"
            "[More info](https://docs.google.com/document/d/1VeAt-V_AVqqiB0EVf-4JL_k_hVOsgbqldeAPVNwG1yI/edit#heading=h.7ct5hku166ut)"
        ),
    )
    description: str = Field(
        title="Description",
        description="Again, assigned by the EGauge modbus map. Is usually 'change in value'",
    )
    type: str = Field(
        title="Type",
        description=(
            "EGauge's numerical data type. Typically our power measurements are f32 ( 32-bit "
            "floating-point number). The serial number & firmware are t16 (which work to treat "
            "as 16-bit unsigned integer) and timestamps are u32 (32-bit unsigned integer)."
        ),
    )
    denominator: int = Field(
        title="Denominator",
        description=(
            "Some of the modbus registers divide by 3.60E+06 (cumulative energy registers typically). "
            "For the power, current, voltage and phase angle the denominator is 1."
        ),
    )
    unit: str = Field(
        title="Unit",
        description="The EGauge unit - typically A, Hz, or W.",
    )
    type_name: Literal["egauge.register.config"] = "egauge.register.config"
    version: Literal["000"] = "000"

    class Config:
        populate_by_name = True
        alias_generator = snake_to_pascal

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
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the egauge.register.config.000 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class EgaugeRegisterConfigMaker:
    type_name = "egauge.register.config"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: EgaugeRegisterConfig) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> EgaugeRegisterConfig:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a egauge.register.config.000 type

        Returns:
            EgaugeRegisterConfig instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> EgaugeRegisterConfig:
        """
        Translates a dict representation of a egauge.register.config.000 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "Address" not in d2.keys():
            raise GwTypeError(f"dict missing Address: <{d2}>")
        if "Name" not in d2.keys():
            raise GwTypeError(f"dict missing Name: <{d2}>")
        if "Description" not in d2.keys():
            raise GwTypeError(f"dict missing Description: <{d2}>")
        if "Type" not in d2.keys():
            raise GwTypeError(f"dict missing Type: <{d2}>")
        if "Denominator" not in d2.keys():
            raise GwTypeError(f"dict missing Denominator: <{d2}>")
        if "Unit" not in d2.keys():
            raise GwTypeError(f"dict missing Unit: <{d2}>")
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret egauge.register.config version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return EgaugeRegisterConfig(**d3)
