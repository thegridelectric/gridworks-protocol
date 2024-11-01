"""Type fsm.trigger.from.atn, version 000"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator

from gwproto.named_types.fsm_event import FsmEvent
from gwproto.property_format import (
    LeftRightDotStr,
    UUID4Str,
)


class FsmTriggerFromAtn(BaseModel):
    ToGNodeAlias: LeftRightDotStr
    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    Trigger: FsmEvent
    TypeName: Literal["fsm.trigger.from.atn"] = "fsm.trigger.from.atn"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow", use_enum_values=True)

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
