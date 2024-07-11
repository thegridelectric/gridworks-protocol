"""
Tests for enum change.primary.pump.state.000 from the GridWorks Type Registry.
"""

from gwproto.enums import ChangePrimaryPumpState


def test_change_primary_pump_state() -> None:
    assert set(ChangePrimaryPumpState.values()) == {
        "TurnPumpOn",
        "TurnPumpOff",
    }

    assert ChangePrimaryPumpState.default() == ChangePrimaryPumpState.TurnPumpOn
    assert ChangePrimaryPumpState.enum_name() == "change.primary.pump.state"
