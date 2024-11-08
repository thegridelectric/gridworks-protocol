"""
Tests for enum sh.fsm.event.type.001 from the GridWorks Type Registry.
"""

from gwproto.enums import FsmEventType


def test_fsm_event_type() -> None:
    assert set(FsmEventType.values()) == {
        "PicoCyclerEvent",
        "ChangeRelayPin",
        "ChangeRelayState",
        "SetAnalog010V",
        "SetAnalog420mA",
        "ChangeValveState",
        "ChangeStoreFlowDirection",
        "ChangeHeatcallSource",
        "ChangeAquastatControl",
        "ChangeHeatPumpControl",
        "ChangeLgOperatingMode",
        "TimerFinished",
        "ChangePrimaryPumpState",
        "ChangePrimaryPumpControl",
    }

    assert FsmEventType.default() == FsmEventType.ChangeRelayState
    assert FsmEventType.enum_name() == "sh.fsm.event.type"
    assert FsmEventType.enum_version() == "001"
