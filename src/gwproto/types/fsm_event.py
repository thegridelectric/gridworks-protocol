"""Type fsm.event, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import validator

from gwproto.enums import FsmEventType
from gwproto.errors import SchemaError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class FsmEvent(BaseModel):
    """
    Finite State Machine Event Command.

    A message sent to a SpaceheatNode wher ethe Node implements a finite state machine. The
    message is intended to be an FSM Events (aka Trigger) that allow a state machine to react
    (by starting a Transition and any side-effect Actions).

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    FromHandle: str = Field(
        title="From Handle",
    )
    ToHandle: str = Field(
        title="To Handle",
    )
    EventType: FsmEventType = Field(
        title="Event Type",
        description=(
            "Typically the set of events allowed will be determined implicitly by the ToHandle. "
            "This is clarified in the message; and if the message does not clarify the appropriate "
            "understanding of the finite state machine and its events then the message will likely "
            "be ignored."
        ),
    )
    EventName: str = Field(
        title="Event Name",
        description=(
            "This should be the name that the receiving Spaceheat Node's finite state machine "
            "uses for an event that triggers a transition."
        ),
    )
    TriggerId: str = Field(
        title="Trigger Id",
        description=(
            "Reference uuid for the triggering event that started a cascade of transitions, events "
            "and side-effect actions - of which this event is one."
        ),
    )
    SendTimeUnixMs: int = Field(
        title="Sent Time Unix Ms",
    )
    TypeName: Literal["fsm.event"] = "fsm.event"
    Version: Literal["000"] = "000"

    class Config:
        extra = Extra.allow

    @validator("FromHandle")
    def _check_from_handle(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"FromHandle failed SpaceheatName format validation: {e}")
        return v

    @validator("ToHandle")
    def _check_to_handle(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"ToHandle failed SpaceheatName format validation: {e}")
        return v

    @validator("TriggerId")
    def _check_trigger_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"TriggerId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("SendTimeUnixMs")
    def _check_send_time_unix_ms(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_ms(v)
        except ValueError as e:
            raise ValueError(
                f"SendTimeUnixMs failed ReasonableUnixTimeMs format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        fsm.event.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        fsm.event.000 type. Unlike the standard python dict method,
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
        del d["EventType"]
        d["EventTypeGtEnumSymbol"] = FsmEventType.value_to_symbol(self.EventType)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the fsm.event.000 representation.

        Instances in the class are python-native representations of fsm.event.000
        objects, while the actual fsm.event.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is FsmEvent.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class FsmEvent_Maker:
    type_name = "fsm.event"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: FsmEvent) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> FsmEvent:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> FsmEvent:
        """
        Deserialize a dictionary representation of a fsm.event.000 message object
        into a FsmEvent python object for internal use.

        This is the near-inverse of the FsmEvent.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a FsmEvent object.

        Returns:
            FsmEvent
        """
        d2 = dict(d)
        if "FromHandle" not in d2.keys():
            raise SchemaError(f"dict missing FromHandle: <{d2}>")
        if "ToHandle" not in d2.keys():
            raise SchemaError(f"dict missing ToHandle: <{d2}>")
        if "EventTypeGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"EventTypeGtEnumSymbol missing from dict <{d2}>")
        value = FsmEventType.symbol_to_value(d2["EventTypeGtEnumSymbol"])
        d2["EventType"] = FsmEventType(value)
        del d2["EventTypeGtEnumSymbol"]
        if "EventName" not in d2.keys():
            raise SchemaError(f"dict missing EventName: <{d2}>")
        if "TriggerId" not in d2.keys():
            raise SchemaError(f"dict missing TriggerId: <{d2}>")
        if "SendTimeUnixMs" not in d2.keys():
            raise SchemaError(f"dict missing SendTimeUnixMs: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret fsm.event version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return FsmEvent(**d2)


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


def check_is_uuid_canonical_textual(v: str) -> None:
    """Checks UuidCanonicalTextual format

    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not UuidCanonicalTextual format
    """
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"<{v}> split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError(f"Words of <{v}> are not all hex")
    if len(x[0]) != 8:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[1]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[2]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[3]) != 4:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[4]) != 12:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
