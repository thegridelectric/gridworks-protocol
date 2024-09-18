"""Type relay.actor.config, version 000"""

from typing import Any, Literal

from pydantic import BaseModel, PositiveInt, model_validator
from typing_extensions import Self

from gwproto.enums import FsmEventType, RelayWiringConfig
from gwproto.property_format import (
    SpaceheatName,
)


class RelayActorConfig(BaseModel):
    RelayIdx: PositiveInt
    ActorName: SpaceheatName
    WiringConfig: RelayWiringConfig
    EventType: FsmEventType
    DeEnergizingEvent: str
    TypeName: Literal["relay.actor.config"] = "relay.actor.config"
    Version: Literal["000"] = "000"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
                Axiom 1: EventType, DeEnergizingEvent consistency.
                a) The EventType must belong to one of the boolean choices for FsmEventType (for example, it is NOT SetAnalog010V):
            ChangeRelayState    ChangeValveState
            ChangeStoreFlowDirection
            ChangeHeatcallSource
            ChangeBoilerControl
            ChangeHeatPumpControl
            ChangeLgOperatingMode

        b) The DeEnergizingEvent string must be one of the two choices for the EventType as an enum. For example,  if the EventType is ChangeValveState then the  DeEnergizingEvent  must either be OpenValve or CloseValve.

        c) If the EventType is ChangeRelayState, then i) the WiringConfig cannot be DoubleThrow ii) if the Wiring Config is NormallyOpen then the DeEnergizingEvent must be OpenRelay and iii) if the WiringConfig is NormallyClosed then the DeEnergizingEvent must be CloseRelay.
        """
        # Implement check for axiom 1"
        return self

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["WiringConfig"] = self.WiringConfig.value
        d["EventType"] = self.EventType.value
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "relay.actor.config"
