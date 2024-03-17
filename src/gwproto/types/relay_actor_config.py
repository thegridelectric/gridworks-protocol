"""Type relay.actor.config, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator
from gwproto.enums import RelayWiringConfig
from gwproto.enums import FsmEventType
from gwproto.errors import SchemaError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class RelayActorConfig(BaseModel):
    """
    Relay Actor Config.

    Used to associate individual relays on a multi-channel relay board to specific SpaceheatNode
    actors. Each actor managed by the Spaceheat SCADA has an associated SpaceheatNode. That
    Node will be associated to a relay board component with multiple relays. Th relay board
    will have a list of relay actor configs so that the actor can identify which relay it has
    purview over.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-actor.html)
    """

    RelayIdx: int = Field(
        title="Relay Index",
    )
    ActorName: str = Field(
        title="Name of the Actor's SpaceheatNode",
        description="[More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-actor.html)",
    )
    WiringConfig: RelayWiringConfig = Field(
        title="Wiring Config",
        description=(
            "Is the relay a simple Normally Open or Normally Closed or is it a double throw relay?"
        ),
    )
    EventType: FsmEventType = Field(
        title="Finite State Machine Event Type",
        description=(
            "Every pair of energization/de-energization actions for a relay are associated with "
            "two events for an associated finite state event."
        ),
    )
    DeEnergizingEvent: str = Field(
        title="DeEnergizing Action",
        description=(
            "Which of the two choices provided by the EventType is intended to result in de-energizing "
            "the pin for the relay?"
        ),
    )
    TypeName: Literal["relay.actor.config"] = "relay.actor.config"
    Version: Literal["000"] = "000"

    @validator("RelayIdx")
    def _check_relay_idx(cls, v: int) -> int:
        try:
            check_is_positive_integer(v)
        except ValueError as e:
            raise ValueError(f"RelayIdx failed PositiveInteger format validation: {e}")
        return v

    @validator("ActorName")
    def _check_actor_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"ActorName failed SpaceheatName format validation: {e}")
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: EventType, DeEnergizingEvent consistency.
        a) The EventType must belong to one of the boolean choices for FsmEventType (for example, 
        it is NOT SetAnalog010V):
            ChangeRelayState
            ChangeValveState
            ChangeStoreFlowDirection
            ChangeHeatcallSource
            ChangeBoilerControl
            ChangeHeatPumpControl
            ChangeLgOperatingMode 

        b) The DeEnergizingEvent string must be one of the two choices for the EventType as an enum. 
        For example, if the EventType is ChangeValveState then the  DeEnergizingEvent  must either 
        be OpenValve or CloseValve. 

        c) If the EventType is ChangeRelayState, then 
            i) the WiringConfig cannot be DoubleThrow;
            ii) if the Wiring Config is NormallyOpen then the DeEnergizingEvent must be OpenRelay; and 
            iii) if the WiringConfig is NormallyClosed then the DeEnergizingEvent must be CloseRelay.
        """
        # TODO: Implement check for axiom 1"
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        relay.actor.config.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        relay.actor.config.000 type. Unlike the standard python dict method,
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
        del d["WiringConfig"]
        d["WiringConfigGtEnumSymbol"] = RelayWiringConfig.value_to_symbol(self.WiringConfig)
        del d["EventType"]
        d["EventTypeGtEnumSymbol"] = FsmEventType.value_to_symbol(self.EventType)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the relay.actor.config.000 representation.

        Instances in the class are python-native representations of relay.actor.config.000
        objects, while the actual relay.actor.config.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is RelayActorConfig.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class RelayActorConfig_Maker:
    type_name = "relay.actor.config"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: RelayActorConfig) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> RelayActorConfig:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> RelayActorConfig:
        """
        Deserialize a dictionary representation of a relay.actor.config.000 message object
        into a RelayActorConfig python object for internal use.

        This is the near-inverse of the RelayActorConfig.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a RelayActorConfig object.

        Returns:
            RelayActorConfig
        """
        d2 = dict(d)
        if "RelayIdx" not in d2.keys():
            raise SchemaError(f"dict missing RelayIdx: <{d2}>")
        if "ActorName" not in d2.keys():
            raise SchemaError(f"dict missing ActorName: <{d2}>")
        if "WiringConfigGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"WiringConfigGtEnumSymbol missing from dict <{d2}>")
        value = RelayWiringConfig.symbol_to_value(d2["WiringConfigGtEnumSymbol"])
        d2["WiringConfig"] = RelayWiringConfig(value)
        del d2["WiringConfigGtEnumSymbol"]
        if "EventTypeGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"EventTypeGtEnumSymbol missing from dict <{d2}>")
        value = FsmEventType.symbol_to_value(d2["EventTypeGtEnumSymbol"])
        d2["EventType"] = FsmEventType(value)
        del d2["EventTypeGtEnumSymbol"]
        if "DeEnergizingEvent" not in d2.keys():
            raise SchemaError(f"dict missing DeEnergizingEvent: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret relay.actor.config version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return RelayActorConfig(**d2)


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
                raise ValueError(f"words of <{v}> split by by '.' must be alphanumeric or hyphen."
                )
    if not v.islower():
        raise ValueError(f"<{v}> must be lowercase.")
