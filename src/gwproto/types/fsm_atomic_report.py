"""Type fsm.atomic.report, version 000"""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, model_validator
from typing_extensions import Self

from gwproto.enums import FsmActionType, FsmEventType, FsmName, FsmReportType
from gwproto.property_format import (
    HandleName,
    ReallyAnInt,
    UTCMilliseconds,
    UUID4Str,
)


class FsmAtomicReport(BaseModel):
    """
    Reports of single Fsm Actions and Transitions. The actions is any side-effect, which is
    the way the StateMachine is supposed to cause things happen to the outside world (This could
    include, for example, actuating a relay.) Transitions are intended to be captured by changing
    the handle of the Spaceheat Node whose actor maintains that finite state machine.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    FromHandle: HandleName
    AboutFsm: FsmName
    ReportType: FsmReportType
    ActionType: Optional[FsmActionType] = None
    Action: Optional[ReallyAnInt] = None
    EventType: Optional[FsmEventType] = None
    Event: Optional[str] = None
    FromState: Optional[str] = None
    ToState: Optional[str] = None
    UnixTimeMs: UTCMilliseconds
    TriggerId: UUID4Str
    TypeName: Literal["fsm.atomic.report"] = "fsm.atomic.report"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Action and ActionType exist iff  ReportType is Action.
        The Optional Attributes ActionType and Action exist if and only if IsAction is true.
        """
        # Implement check for axiom 1"
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: If Action exists, then it belongs to the un-versioned enum selected in the ActionType.

        """
        # Implement check for axiom 2"
        return self

    @model_validator(mode="after")
    def check_axiom_3(self) -> Self:
        """
        Axiom 3: EventType, Event, FromState, ToState exist iff ReportType is Event.

        """
        # Implement check for axiom 3"
        return self

    @classmethod
    def type_name_value(cls) -> str:
        return "fsm.atomic.report"
