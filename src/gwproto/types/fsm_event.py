"""Type fsm.event, version 000"""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, model_validator
from typing_extensions import Self

from gwproto.enums import FsmEventType
from gwproto.property_format import (
    HandleName,
    UTCMilliseconds,
    UUID4Str,
)


class FsmEvent(BaseModel):
    FromHandle: HandleName
    ToHandle: HandleName
    EventType: FsmEventType
    EventName: str
    TriggerId: UUID4Str
    SendTimeUnixMs: UTCMilliseconds
    TypeName: Literal["fsm.event"] = "fsm.event"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: EventName must belong to the enum selected in the EventType.

        """
        # Implement check for axiom 1"
        return self

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["EventType"] = self.EventType.value
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "fsm.event"
