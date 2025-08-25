"""Type fsm.atomic.report, version 000"""

from typing import Literal, Optional

from gw.named_types import GwBase
from pydantic import ConfigDict, StrictInt, model_validator
from typing_extensions import Self

from gwproto.enums import FsmActionType, FsmReportType
from gwproto.property_format import (
    HandleName,
    LeftRightDotStr,
    UTCMilliseconds,
    UUID4Str,
)


class FsmAtomicReport(GwBase):
    """ASL schema of record [fsm.atomic.report v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/fsm.atomic.report.000.yaml)"""

    machine_handle: HandleName
    state_enum: LeftRightDotStr
    report_type: FsmReportType
    action_type: Optional[FsmActionType] = None
    action: Optional[StrictInt] = None
    event_enum: Optional[LeftRightDotStr] = None
    event: Optional[str] = None
    from_state: Optional[str] = None
    to_state: Optional[str] = None
    unix_time_ms: UTCMilliseconds
    trigger_id: UUID4Str
    type_name: Literal["fsm.atomic.report"] = "fsm.atomic.report"
    version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Action and ActionType exist iff  ReportType is Action.
        The Optional Attributes ActionType and Action exist if and only if IsAction is true.
        """
        # Implement check for axiom 1""
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: If Action exists, then it belongs to the un-versioned enum selected in the ActionType.

        """
        # Implement check for axiom 2""
        return self

    @model_validator(mode="after")
    def check_axiom_3(self) -> Self:
        """
        Axiom 3: EventType, Event, FromState, ToState exist iff ReportType is Event.

        """
        # Implement check for axiom 3""
        return self
