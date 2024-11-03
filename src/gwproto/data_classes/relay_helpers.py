from typing import Any, Optional, Tuple, Type

from pydantic import BaseModel

from gwproto.enums import (
    ChangeAquastatControl,
    ChangeHeatcallSource,
    ChangeHeatPumpControl,
    ChangePrimaryPumpControl,
    ChangeRelayPin,
    ChangeRelayState,
    ChangeStoreFlowDirection,
    FsmEventType,
    RelayWiringConfig,
)
from gwproto.enums.relay_event_base import RelayEventBase

#####################################################
# Relay related
#####################################################


class RelayEvent:
    allowed_events: Tuple[Type] = (
        ChangeAquastatControl,
        ChangeHeatPumpControl,
        ChangeHeatcallSource,
        ChangePrimaryPumpControl,
        ChangeRelayState,
        ChangeStoreFlowDirection,
    )

    def __init__(self, relay_config: RelayWiringConfig, action: RelayEventBase) -> None:
        if type(action) not in self.allowed_events:
            raise ValueError(f"Invalid action type: {type(action)}")
        self.relay_config = relay_config
        self.action = action

    def __eq__(self, other: "RelayEvent") -> None:
        return isinstance(other, RelayEvent) and self.__dict__ == other.__dict__

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self) -> str:
        return f"{self.relay_config}, {self.action}"

    def __repr__(self) -> str:
        return f"{self.relay_config}, {self.action}"


RELAY_INSTRUCTION = {
    RelayEvent(
        RelayWiringConfig.NormallyClosed, ChangeRelayState.CloseRelay
    ): ChangeRelayPin.DeEnergize,
    RelayEvent(
        RelayWiringConfig.NormallyClosed, ChangeRelayState.OpenRelay
    ): ChangeRelayPin.Energize,
    RelayEvent(
        RelayWiringConfig.NormallyOpen, ChangeRelayState.CloseRelay
    ): ChangeRelayPin.Energize,
    RelayEvent(
        RelayWiringConfig.NormallyOpen, ChangeRelayState.OpenRelay
    ): ChangeRelayPin.DeEnergize,
    RelayEvent(
        RelayWiringConfig.DoubleThrow, ChangeAquastatControl.SwitchToBoiler
    ): ChangeRelayPin.DeEnergize,
    RelayEvent(
        RelayWiringConfig.DoubleThrow, ChangeAquastatControl.SwitchToScada
    ): ChangeRelayPin.Energize,
    RelayEvent(
        RelayWiringConfig.DoubleThrow, ChangeHeatcallSource.SwitchToWallThermostat
    ): ChangeRelayPin.DeEnergize,
    RelayEvent(
        RelayWiringConfig.DoubleThrow, ChangeHeatcallSource.SwitchToScada
    ): ChangeRelayPin.Energize,
    RelayEvent(
        RelayWiringConfig.DoubleThrow, ChangeHeatPumpControl.SwitchToTankAquastat
    ): ChangeRelayPin.DeEnergize,
    RelayEvent(
        RelayWiringConfig.DoubleThrow, ChangeHeatPumpControl.SwitchToScada
    ): ChangeRelayPin.Energize,
    RelayEvent(
        RelayWiringConfig.NormallyOpen, ChangeStoreFlowDirection.Discharge
    ): ChangeRelayPin.DeEnergize,
    RelayEvent(
        RelayWiringConfig.NormallyOpen, ChangeStoreFlowDirection.Charge
    ): ChangeRelayPin.Energize,
    RelayEvent(
        RelayWiringConfig.DoubleThrow, ChangePrimaryPumpControl.SwitchToHeatPump
    ): ChangeRelayPin.DeEnergize,
    RelayEvent(
        RelayWiringConfig.DoubleThrow, ChangePrimaryPumpControl.SwitchToScada
    ): ChangeRelayPin.Energize,
}


class RelayChoice(BaseModel):
    display_name: str
    idx: int
    config: RelayWiringConfig
    control_type: FsmEventType
    de_energize_option: Any
    energize_option: Any
    current_state: Optional[Any]
