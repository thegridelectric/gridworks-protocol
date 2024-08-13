from gwproto.enums import (
    ChangeAquastatControl,
    ChangeHeatcallSource,
    ChangeHeatPumpControl,
    ChangeLgOperatingMode,
    ChangePrimaryPumpControl,
    ChangePrimaryPumpState,
    ChangeRelayPin,
    ChangeRelayState,
    ChangeStoreFlowDirection,
    ChangeValveState,
    FsmEventType,
)

EVENT_ENUM_BY_NAME = {
    FsmEventType.ChangeRelayState.value: ChangeRelayState,
    FsmEventType.ChangeValveState.value: ChangeValveState,
    FsmEventType.ChangeStoreFlowDirection.value: ChangeStoreFlowDirection,
    FsmEventType.ChangeHeatcallSource.value: ChangeHeatcallSource,
    FsmEventType.ChangeAquastatControl.value: ChangeAquastatControl,
    FsmEventType.ChangeHeatPumpControl.value: ChangeHeatPumpControl,
    FsmEventType.ChangeLgOperatingMode.value: ChangeLgOperatingMode,
    FsmEventType.ChangePrimaryPumpControl.value: ChangePrimaryPumpControl,
    FsmEventType.ChangePrimaryPumpState.value: ChangePrimaryPumpState,
    FsmEventType.ChangeRelayPin.value: ChangeRelayPin
}
