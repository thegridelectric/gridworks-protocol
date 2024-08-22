"""Type fsm.trigger.from.atn, version 000"""

import json
import logging
import os
from typing import Any, Dict, Literal

import dotenv
from gw.errors import GwTypeError
from gw.utils import is_pascal_case, pascal_to_snake, snake_to_pascal
from pydantic import BaseModel, ConfigDict, Field, field_validator

from gwproto.types.fsm_event import FsmEvent, FsmEventMaker

dotenv.load_dotenv()

ENCODE_ENUMS = int(os.getenv("ENUM_ENCODE", "1"))

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

    to_g_node_alias: str = Field(
        title="GNodeAlias of the receiving SCADA",
    )
    from_g_node_alias: str = Field(
        title="GNodeAlias of the sending AtomicTNode",
    )
    from_g_node_instance_id: str = Field(
        title="GNodeInstance of the sending AtomicTNode",
    )
    trigger: FsmEvent = Field(
        title="Trigger",
        description=(
            "This remote event will triggers a cascade of local events, transitions and actions "
            "in the Spaceheat Nodes of the SCADA. This comes from the language of Finite State "
            "Machines"
            "[More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)"
        ),
    )
    type_name: Literal["fsm.trigger.from.atn"] = "fsm.trigger.from.atn"
    version: Literal["000"] = "000"
    model_config = ConfigDict(
        extra="allow", populate_by_name=True, alias_generator=snake_to_pascal
    )

    @field_validator("to_g_node_alias")
    @classmethod
    def _check_to_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"ToGNodeAlias failed LeftRightDot format validation: {e}"
            ) from e
        return v

    @field_validator("from_g_node_alias")
    @classmethod
    def _check_from_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeAlias failed LeftRightDot format validation: {e}",
            ) from e
        return v

    @field_validator("from_g_node_instance_id")
    @classmethod
    def _check_from_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeInstanceId failed UuidCanonicalTextual format validation: {e}",
            ) from e
        return v

    @field_validator("trigger")
    @classmethod
    def check_trigger(cls, v: FsmEvent) -> FsmEvent:
        """
            Axiom 1: FromHandle must be 'a' (for AtomicTNode).
            The triggering event is coming from the AtomicTNode, which always has the handle of "a"
        as a SpaceheatNode in the SCADA's hierarchical finite state machine.
        """
        if v.from_handle != "a":
            raise ValueError(
                "Axiom 1 violated: FromHandle must be 'a' (for AtomicTNode)."
            )
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
        d["Trigger"] = self.trigger.as_dict()
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
        d["Trigger"] = self.trigger.as_dict()
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the fsm.trigger.from.atn.000 representation designed to send in a message.

        Recursively encodes enums as hard-to-remember 8-digit random hex symbols
        unless settings.encode_enums is set to 0.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class FsmTriggerFromAtnMaker:
    type_name = "fsm.trigger.from.atn"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tuple: FsmTriggerFromAtn) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, b: bytes) -> FsmTriggerFromAtn:
        """
        Given the bytes in a message, returns the corresponding class object.

        Args:
            b (bytes): candidate type instance

        Raises:
           GwTypeError: if the bytes are not a fsm.trigger.from.atn.000 type

        Returns:
            FsmTriggerFromAtn instance
        """
        try:
            d = json.loads(b)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        if not isinstance(d, dict):
            raise GwTypeError(f"Deserializing  must result in dict!\n <{b}>")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> FsmTriggerFromAtn:
        """
        Translates a dict representation of a fsm.trigger.from.atn.000 message object
        into the Python class object.
        """
        for key in d.keys():
            if not is_pascal_case(key):
                raise GwTypeError(f"Key '{key}' is not PascalCase")
        d2 = dict(d)
        if "ToGNodeAlias" not in d2.keys():
            raise GwTypeError(f"dict missing ToGNodeAlias: <{d2}>")
        if "FromGNodeAlias" not in d2.keys():
            raise GwTypeError(f"dict missing FromGNodeAlias: <{d2}>")
        if "FromGNodeInstanceId" not in d2.keys():
            raise GwTypeError(f"dict missing FromGNodeInstanceId: <{d2}>")
        if "Trigger" not in d2.keys():
            raise GwTypeError(f"dict missing Trigger: <{d2}>")
        if not isinstance(d2["Trigger"], dict):
            raise GwTypeError(f"Trigger <{d2['Trigger']}> must be a FsmEvent!")
        trigger = FsmEventMaker.dict_to_tuple(d2["Trigger"])
        d2["Trigger"] = trigger
        if "TypeName" not in d2.keys():
            raise GwTypeError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise GwTypeError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret fsm.trigger.from.atn version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        d3 = {pascal_to_snake(key): value for key, value in d2.items()}
        return FsmTriggerFromAtn(**d3)


def check_is_left_right_dot(v: str) -> None:
    """Checks LeftRightDot Format

    LeftRightDot format: Lowercase alphanumeric words separated by periods, with
    the most significant word (on the left) starting with an alphabet character.

    Args:
        v (str): the candidate

    Raises:
        ValueError: if v is not LeftRightDot format
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
    phi_fun_check_it_out = 5
    two_cubed_too_cute = 8
    bachets_fun_four = 4
    the_sublime_twelve = 12
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}") from e
    if len(x) != phi_fun_check_it_out:
        raise ValueError(f"<{v}> split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError as e:
            raise ValueError(f"Words of <{v}> are not all hex") from e
    if len(x[0]) != two_cubed_too_cute:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[1]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[2]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[3]) != bachets_fun_four:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
    if len(x[4]) != the_sublime_twelve:
        raise ValueError(f"<{v}> word lengths not 8-4-4-4-12")
