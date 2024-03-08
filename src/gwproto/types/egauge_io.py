"""Type egauge.io, version 001"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gwproto.errors import SchemaError
from gwproto.types.egauge_register_config import EgaugeRegisterConfig
from gwproto.types.egauge_register_config import EgaugeRegisterConfig_Maker


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

    ChannelName: str = Field(
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
    InputConfig: EgaugeRegisterConfig = Field(
        title="Input config for one channel of data for a specific eGauge meter",
        description=(
            "This is the data available from the modbus csv map provided by eGauge for this component, "
            "for example http://egauge14875.egaug.es/6001C/settings.html for a eGauge device "
            "with ID 14875"
        ),
    )
    TypeName: Literal["egauge.io"] = "egauge.io"
    Version: Literal["001"] = "001"

    @validator("ChannelName")
    def _check_channel_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"ChannelName failed SpaceheatName format validation: {e}")
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        egauge.io.001 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        egauge.io.001 type. Unlike the standard python dict method,
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
        d["InputConfig"] = self.InputConfig.as_dict()
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the egauge.io.001 representation.

        Instances in the class are python-native representations of egauge.io.001
        objects, while the actual egauge.io.001 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is EgaugeIo.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class EgaugeIo_Maker:
    type_name = "egauge.io"
    version = "001"

    @classmethod
    def tuple_to_type(cls, tuple: EgaugeIo) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> EgaugeIo:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> EgaugeIo:
        """
        Deserialize a dictionary representation of a egauge.io.001 message object
        into a EgaugeIo python object for internal use.

        This is the near-inverse of the EgaugeIo.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a EgaugeIo object.

        Returns:
            EgaugeIo
        """
        d2 = dict(d)
        if "ChannelName" not in d2.keys():
            raise SchemaError(f"dict missing ChannelName: <{d2}>")
        if "InputConfig" not in d2.keys():
            raise SchemaError(f"dict missing InputConfig: <{d2}>")
        if not isinstance(d2["InputConfig"], dict):
            raise SchemaError(
                f"InputConfig <{d2['InputConfig']}> must be a EgaugeRegisterConfig!"
            )
        input_config = EgaugeRegisterConfig_Maker.dict_to_tuple(d2["InputConfig"])
        d2["InputConfig"] = input_config
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "001":
            LOGGER.debug(
                f"Attempting to interpret egauge.io version {d2['Version']} as version 001"
            )
            d2["Version"] = "001"
        return EgaugeIo(**d2)


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
