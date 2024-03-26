"""Type fsm.trigger.from.atn, version 000"""

import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import validator

from gwproto.errors import SchemaError
from gwproto.types.fsm_event import FsmEvent
from gwproto.types.fsm_event import FsmEvent_Maker


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class FsmTriggerFromAtn(BaseModel):
    """
    This is an FSM Event sent from the AtomicTNode to its Scada. We use the word "trigger" to
    refer to an event that BEGINS a cause-and-effect chain of events in the hierarchical finite
    state machine.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    ToGNodeAlias: str = Field(
        title="GNodeAlias of the receiving SCADA",
    )
    FromGNodeAlias: str = Field(
        title="GNodeAlias of the sending AtomicTNode",
    )
    FromGNodeInstanceId: str = Field(
        title="GNodeInstance of the sending AtomicTNode",
    )
    Trigger: FsmEvent = Field(
        title="Trigger",
        description=(
            "This remote event will triggers a cascade of local events, transitions and actions "
            "in the Spaceheat Nodes of the SCADA. This comes from the language of Finite State "
            "Machines"
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)"
        ),
    )
    TypeName: Literal["fsm.trigger.from.atn"] = "fsm.trigger.from.atn"
    Version: Literal["000"] = "000"

    class Config:
        extra = Extra.allow

    @validator("ToGNodeAlias")
    def _check_to_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"ToGNodeAlias failed LeftRightDot format validation: {e}")
        return v

    @validator("FromGNodeAlias")
    def _check_from_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("FromGNodeInstanceId")
    def _check_from_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("Trigger")
    def check_trigger(cls, v: FsmEvent) -> FsmEvent:
        """
        Axiom 1: FromHandle must be 'a' (for AtomicTNode).
        The triggering event is coming from the AtomicTNode, which always has the handle of "a"
        as a SpaceheatNode in the SCADA's hierarchical finite state machine.
        """
        if v.FromHandle != "a":
            raise ValueError(
                "Axiom 1 violated: FromHandle must be 'a' (for AtomicTNode)."
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        fsm.trigger.from.atn.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        fsm.trigger.from.atn.000 type. Unlike the standard python dict method,
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
        d["Trigger"] = self.Trigger.as_dict()
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the fsm.trigger.from.atn.000 representation.

        Instances in the class are python-native representations of fsm.trigger.from.atn.000
        objects, while the actual fsm.trigger.from.atn.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is FsmTriggerFromAtn.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class FsmTriggerFromAtn_Maker:
    type_name = "fsm.trigger.from.atn"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: FsmTriggerFromAtn) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> FsmTriggerFromAtn:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> FsmTriggerFromAtn:
        """
        Deserialize a dictionary representation of a fsm.trigger.from.atn.000 message object
        into a FsmTriggerFromAtn python object for internal use.

        This is the near-inverse of the FsmTriggerFromAtn.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a FsmTriggerFromAtn object.

        Returns:
            FsmTriggerFromAtn
        """
        d2 = dict(d)
        if "ToGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing ToGNodeAlias: <{d2}>")
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeAlias: <{d2}>")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict missing FromGNodeInstanceId: <{d2}>")
        if "Trigger" not in d2.keys():
            raise SchemaError(f"dict missing Trigger: <{d2}>")
        if not isinstance(d2["Trigger"], dict):
            raise SchemaError(f"Trigger <{d2['Trigger']}> must be a FsmEvent!")
        trigger = FsmEvent_Maker.dict_to_tuple(d2["Trigger"])
        d2["Trigger"] = trigger
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret fsm.trigger.from.atn version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return FsmTriggerFromAtn(**d2)


def check_is_left_right_dot(v: str) -> None:
    """Checks LeftRightDot Format

    LeftRightDot format: Lowercase alphanumeric words separated by periods, with
    the most significant word (on the left) starting with an alphabet character.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not LeftRightDot format
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
        if not word.isalnum():
            raise ValueError(f"words of <{v}> split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of <{v}> must be lowercase.")


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
