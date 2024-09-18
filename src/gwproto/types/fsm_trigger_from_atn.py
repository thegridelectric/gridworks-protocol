"""Type fsm.trigger.from.atn, version 000"""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, field_validator

from gwproto.property_format import (
    LeftRightDotStr,
    UUID4Str,
)
from gwproto.types.fsm_event import FsmEvent


class FsmTriggerFromAtn(BaseModel):
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

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["Trigger"] = self.Trigger.model_dump(**kwargs)
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "fsm.trigger.from.atn"
