"""Type fsm.trigger.from.atn, version 000"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator

from gwproto.property_format import (
    LeftRightDotStr,
    UUID4Str,
)
from gwproto.types.fsm_event import FsmEvent


class FsmTriggerFromAtn(BaseModel):
    """
    This is an FSM Event sent from the AtomicTNode to its Scada. We use the word "trigger" to
    refer to an event that BEGINS a cause-and-effect chain of events in the hierarchical finite
    state machine.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    ToGNodeAlias: LeftRightDotStr
    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    Trigger: FsmEvent
    TypeName: Literal["fsm.trigger.from.atn"] = "fsm.trigger.from.atn"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @field_validator("Trigger")
    @classmethod
    def check_trigger(cls, v: FsmEvent) -> FsmEvent:
        """
            Axiom 1: FromHandle must be 'a' (for AtomicTNode).
            The triggering event is coming from the AtomicTNode, which always has the handle of "a"
        as a SpaceheatNode in the SCADA's hierarchical finite state machine.
        """
        # Implement Axiom(s)
        return v

    @classmethod
    def type_name_value(cls) -> str:
        return "fsm.trigger.from.atn"
