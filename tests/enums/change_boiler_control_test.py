"""
Tests for enum change.boiler.control.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeBoilerControl


def test_change_boiler_control() -> None:
    assert set(ChangeBoilerControl.values()) == {
        "SwitchToTankAquastat",
        "SwitchToScada",
    }

    assert ChangeBoilerControl.default() == ChangeBoilerControl.SwitchToTankAquastat
    assert ChangeBoilerControl.enum_name() == "change.boiler.control"
