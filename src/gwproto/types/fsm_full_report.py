"""Type fsm.full.report, version 000"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import validator
from gwproto.types.fsm_event import FsmEvent
from gwproto.types.fsm_event import FsmEvent_Maker
from gwproto.types.fsm_event import FsmEvent
from gwproto.types.fsm_event import FsmEvent_Maker
from gwproto.errors import SchemaError

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class FsmFullReport(BaseModel):
    """
    There will be cascading events, actions and transitions that will naturally follow a single
    high-level event. This message is designed to encapsulate all of those.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    FromName: str = Field(
        title="From Name",
        description=(
            "The name (not the handle, so immutable) of the Node issuing the report. This will "
            "typically be the scada node itself."
        ),
    )
    Trigger: FsmEvent = Field(
        title="Trigger",
        description=(
            "The event that triggered the collected list of actions, transitions and further "
            "events."
        ),
    )
    AtomicList: FsmEvent = Field(
        title="Atomic List",
        description=(
            "The list of cascading events, transitions and actions triggered by a single high-level "
            "event in a hierarchical finite state machine."
        ),
    )
    TypeName: Literal["fsm.full.report"] = "fsm.full.report"
    Version: Literal["000"] = "000"

    class Config:
        extra = Extra.allow

    @validator("FromName")
    def _check_from_name(cls, v: str) -> str:
        try:
            check_is_spaceheat_name(v)
        except ValueError as e:
            raise ValueError(f"FromName failed SpaceheatName format validation: {e}")
        return v

    def as_dict(self) -> Dict[str, Any]:
        """
        Translate the object into a dictionary representation that can be serialized into a
        fsm.full.report.000 object.

        This method prepares the object for serialization by the as_type method, creating a
        dictionary with key-value pairs that follow the requirements for an instance of the
        fsm.full.report.000 type. Unlike the standard python dict method,
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
        d["AtomicList"] = self.AtomicList.as_dict()
        return d

    def as_type(self) -> bytes:
        """
        Serialize to the fsm.full.report.000 representation.

        Instances in the class are python-native representations of fsm.full.report.000
        objects, while the actual fsm.full.report.000 object is the serialized UTF-8 byte
        string designed for sending in a message.

        This method calls the as_dict() method, which differs from the native python dict()
        in the following key ways:
        - Enum Values: Translates between the values used locally by the actor to the symbol
        sent in messages.
        - - Removes any key-value pairs where the value is None for a clearer message, especially
        in cases with many optional attributes.

        It also applies these changes recursively to sub-types.

        Its near-inverse is FsmFullReport.type_to_tuple(). If the type (or any sub-types)
        includes an enum, then the type_to_tuple will map an unrecognized symbol to the
        default enum value. This is why these two methods are only 'near' inverses.
        """
        json_string = json.dumps(self.as_dict())
        return json_string.encode("utf-8")

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class FsmFullReport_Maker:
    type_name = "fsm.full.report"
    version = "000"

    def __init__(
        self,
        from_name: str,
        trigger: FsmEvent,
        atomic_list: FsmEvent,
    ):
        self.tuple = FsmFullReport(
            FromName=from_name,
            Trigger=trigger,
            AtomicList=atomic_list,
        )

    @classmethod
    def tuple_to_type(cls, tuple: FsmFullReport) -> bytes:
        """
        Given a Python class object, returns the serialized JSON type object.
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: bytes) -> FsmFullReport:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> FsmFullReport:
        """
        Deserialize a dictionary representation of a fsm.full.report.000 message object
        into a FsmFullReport python object for internal use.

        This is the near-inverse of the FsmFullReport.as_dict() method:
          - Enums: translates between the symbols sent in messages between actors and
        the values used by the actors internally once they've deserialized the messages.
          - Types: recursively validates and deserializes sub-types.

        Note that if a required attribute with a default value is missing in a dict, this method will
        raise a SchemaError. This differs from the pydantic BaseModel practice of auto-completing
        missing attributes with default values when they exist.

        Args:
            d (dict): the dictionary resulting from json.loads(t) for a serialized JSON type object t.

        Raises:
           SchemaError: if the dict cannot be turned into a FsmFullReport object.

        Returns:
            FsmFullReport
        """
        d2 = dict(d)
        if "FromName" not in d2.keys():
            raise SchemaError(f"dict missing FromName: <{d2}>")
        if "Trigger" not in d2.keys():
            raise SchemaError(f"dict missing Trigger: <{d2}>")
        if not isinstance(d2["Trigger"], dict):
            raise SchemaError(f"Trigger <{d2['Trigger']}> must be a FsmEvent!")
        trigger = FsmEvent_Maker.dict_to_tuple(d2["Trigger"])
        d2["Trigger"] = trigger
        if "AtomicList" not in d2.keys():
            raise SchemaError(f"dict missing AtomicList: <{d2}>")
        if not isinstance(d2["AtomicList"], dict):
            raise SchemaError(f"AtomicList <{d2['AtomicList']}> must be a FsmEvent!")
        atomic_list = FsmEvent_Maker.dict_to_tuple(d2["AtomicList"])
        d2["AtomicList"] = atomic_list
        if "TypeName" not in d2.keys():
            raise SchemaError(f"TypeName missing from dict <{d2}>")
        if "Version" not in d2.keys():
            raise SchemaError(f"Version missing from dict <{d2}>")
        if d2["Version"] != "000":
            LOGGER.debug(
                f"Attempting to interpret fsm.full.report version {d2['Version']} as version 000"
            )
            d2["Version"] = "000"
        return FsmFullReport(**d2)


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
