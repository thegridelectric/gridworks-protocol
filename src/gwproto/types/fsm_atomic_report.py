"""Type fsm.atomic.report, version 000"""
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
from gwproto.enums import FsmActionType
from gwproto.errors import SchemaError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class FsmAtomicReport(BaseModel):
    """
    Reports of single Fsm Actions and Transitions. The actions is any side-effect, which is
    the way the StateMachine is supposed to cause things happen to the outside world (This could
    include, for example, actuating a relay.) Transitions are intended to be captured by changing
    the handle of the Spaceheat Node whose actor maintains that finite state machine.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    FromHandle: str = Field(
        title="From Name",
        description=(
            "The Name (as opposed to the handle) of the Spaceheat Node actor issuing the Finite "
            "State Machine report. The actor is meant to realize and be the authority on the "
            "FSM in question. Its handle reflects the state it is in."
        ),
    )
    IsAction: bool = Field(
        title="Is Action",
        description=(
            "An Action refers to some side effect of a state transition that results in a physical "
            "change to an underlying TerminalAsset."
        ),
    )
    ActionType: Optional[FsmActionType] = Field(
        title="Action Type",
        description="The FiniteState Machine Action taken",
        default=None,
    )
    Action: Optional[str] = Field(
        title="Action",
        description=(
            "Should belong to the associated enum element chosen in ActionType. For example, "
            "if ActionType is ChangeStoreFlowDirection, then Action should be either 'Discharge' "
            "or 'Charge.'"
        ),
        default=None,
    )
    UnixTimeMs: int = Field(
        title="Unix Time in Milliseconds",
    )
    TypeName: Literal["fsm.atomic.report"] = "fsm.atomic.report"
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

    @validator("UnixTimeMs")
    def _check_unix_time_ms(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_ms(v)
        except ValueError as e:
            raise ValueError(
                f"UnixTimeMs failed ReasonableUnixTimeMs format validation: {e}"
            )
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Action and ActionType exist iff IsAction.
        The Optional Attributes ActionType and Action exist if and only if IsAction is true.
        """
        # TODO: Implement check for axiom 1"
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        fsm.atomic.report.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        fsm.atomic.report.000 type. Unlike the standard python dict method,
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
        if "ActionType" in d.keys():
            del d["ActionType"]
            d["ActionTypeGtEnumSymbol"] = FsmActionType.value_to_symbol(self.ActionType)
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the fsm.atomic.report.000 representation.

        Instances in the class are python-native representations of fsm.atomic.report.000
        objects, while the actual fsm.atomic.report.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is FsmAtomicReport.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class FsmAtomicReport_Maker:
    type_name = "fsm.atomic.report"
    version = "000"

    def __init__(
        self,
        from_handle: str,
        is_action: bool,
        action_type: Optional[FsmActionType],
        action: Optional[str],
        unix_time_ms: int,
    ):
        self.tuple = FsmAtomicReport(
            FromHandle=from_handle,
            IsAction=is_action,
            ActionType=action_type,
            Action=action,
            UnixTimeMs=unix_time_ms,
        )

    @classmethod
    def tuple_to_type(cls, tuple: FsmAtomicReport) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> FsmAtomicReport:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> FsmAtomicReport:
        """
        Deserialize a dictionary representation of a fsm.atomic.report.000 message object
        into a FsmAtomicReport python object for internal use.

        This is the near-inverse of the FsmAtomicReport.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a FsmAtomicReport object.

        Returns:
            FsmAtomicReport
        """
        d2 = dict(d)
        if "FromHandle" not in d2.keys():
            raise SchemaError(f"dict missing FromHandle: <{d2}>")
        if "IsAction" not in d2.keys():
            raise SchemaError(f"dict missing IsAction: <{d2}>")
        if "ActionType" in d2.keys():
            value = FsmActionType.symbol_to_value(d2["ActionTypeGtEnumSymbol"])
            d2["ActionType"] = FsmActionType(value)
        if "UnixTimeMs" not in d2.keys():
            raise SchemaError(f"dict missing UnixTimeMs: <{d2}>")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret fsm.atomic.report version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return FsmAtomicReport(**d2)


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
            if not (char.isalnum() or char == '-'):
                raise ValueError(f"words of <{v}> split by by '.' must be alphanumeric or hyphen.")
    if not v.islower():
        raise ValueError(f"<{v}> must be lowercase.")
