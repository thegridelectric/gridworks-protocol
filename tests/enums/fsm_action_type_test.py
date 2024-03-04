"""
Tests for enum sh.fsm.action.type.000 from the GridWorks Type Registry.
"""
from gwproto.enums import FsmActionType


def test_fsm_action_type() -> None:
    assert set(FsmActionType.values()) == {
        "ChangeRelayState",
        "Analog010V",
        "Analog420mA",
        "ChangeValveState",
        "ChangeStoreFlowDirection",
        "ChangeHeatcallSource",
        "ChangeBoilerControl",
        "ChangeHeatPumpControl",
        "ChangeLgOperatingMode",
    }

    assert FsmActionType.default() == FsmActionType.ChangeRelayState
    assert FsmActionType.enum_name() == "sh.fsm.action.type"
    assert FsmActionType.enum_version() == "000"

    assert FsmActionType.version("ChangeRelayState") == "000"
    assert FsmActionType.version("Analog010V") == "000"
    assert FsmActionType.version("Analog420mA") == "000"
    assert FsmActionType.version("ChangeValveState") == "000"
    assert FsmActionType.version("ChangeStoreFlowDirection") == "000"
    assert FsmActionType.version("ChangeHeatcallSource") == "000"
    assert FsmActionType.version("ChangeBoilerControl") == "000"
    assert FsmActionType.version("ChangeHeatPumpControl") == "000"
    assert FsmActionType.version("ChangeLgOperatingMode") == "000"

    for value in FsmActionType.values():
        symbol = FsmActionType.value_to_symbol(value)
        assert FsmActionType.symbol_to_value(symbol) == value
