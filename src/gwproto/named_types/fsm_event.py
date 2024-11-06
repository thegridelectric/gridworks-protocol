"""Type fsm.event, version 000"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, model_validator
from typing_extensions import Self

from gwproto.enums import (
    ChangeAquastatControl,
    ChangeHeatcallSource,
    ChangeHeatPumpControl,
    ChangePrimaryPumpControl,
    ChangeRelayPin,
    ChangeRelayState,
    ChangeStoreFlowDirection,
    FsmEventType,
)
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

    model_config = ConfigDict(extra="allow", use_enum_values=True)

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: EventName must belong to the enum selected in the EventType.

        """
        if (
            self.EventType == "ChangeAquastatControl"
            and self.EventName not in ChangeAquastatControl.values()
        ):
            raise ValueError(
                f"EventName {self.EventName} must belong to EventType ChangeAquastatControl values {ChangeAquastatControl.values()}"
            )
        if (
            self.EventType == "ChangeHeatcallSource"
            and self.EventName not in ChangeHeatcallSource.values()
        ):
            raise ValueError(
                f"EventName {self.EventName} must belong to EventType ChangeHeatcallSource values {ChangeHeatcallSource.values()}"
            )
        if (
            self.EventType == "ChangeHeatPumpControl"
            and self.EventName not in ChangeHeatPumpControl.values()
        ):
            raise ValueError(
                f"EventName {self.EventName} must belong to EventType ChangeHeatPumpControl values {ChangeHeatPumpControl.values()}"
            )
        if (
            self.EventType == "ChangePrimaryPumpControl"
            and self.EventName not in ChangePrimaryPumpControl.values()
        ):
            raise ValueError(
                f"EventName {self.EventName} must belong to EventType ChangePrimaryPumpControl values {ChangePrimaryPumpControl.values()}"
            )
        if (
            self.EventType == "ChangeRelayPin"
            and self.EventName not in ChangeRelayPin.values()
        ):
            raise ValueError(
                f"EventName {self.EventName} must belong to EventType ChangeRelayPin values {ChangeRelayPin.values()}"
            )
        if (
            self.EventType == "ChangeRelayState"
            and self.EventName not in ChangeRelayState.values()
        ):
            raise ValueError(
                f"EventName {self.EventName} must belong to EventType ChangeRelayState values {ChangeRelayState.values()}"
            )
        if (
            self.EventType == "ChangeStoreFlowDirection"
            and self.EventName not in ChangeStoreFlowDirection.values()
        ):
            raise ValueError(
                f"EventName {self.EventName} must belong to EventType ChangeStoreFlowDirection values {ChangeStoreFlowDirection.values()}"
            )
        if (
            self.EventType == "ChangeStoreFlowDirection"
            and self.EventName not in ChangeStoreFlowDirection.values()
        ):
            raise ValueError(
                f"EventName {self.EventName} must belong to EventType ChangeStoreFlowDirection values {ChangeStoreFlowDirection.values()}"
            )
        if self.EventType not in [
            "ChangeAquastatControl",
            "ChangeHeatcallSource",
            "ChangeHeatPumpControl",
            "ChangePrimaryPumpControl",
            "ChangeRelayPin",
            "ChangeRelayState",
            "ChangeStoreFlowDirection",
        ]:
            raise ValueError(f"Unrecognized event type {self.EventType}!")
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: FromHandle must be the immediate boss of ToHandle, unless
        ToHandle is 'relay-multiplexer'

        """
        if self.ToHandle == "relay-multiplexer":
            return self
        immediate_boss = ".".join(self.ToHandle.split(".")[:-1])
        if immediate_boss != self.FromHandle:
            raise ValueError(
                f"FromHandle {self.FromHandle} must be immediate boss of ToHandle {immediate_boss}"
            )
        return self
