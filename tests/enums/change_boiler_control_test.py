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
    assert ChangeBoilerControl.enum_version() == "000"

    assert ChangeBoilerControl.version("SwitchToTankAquastat") == "000"
    assert ChangeBoilerControl.version("SwitchToScada") == "000"

    for value in ChangeBoilerControl.values():
        symbol = ChangeBoilerControl.value_to_symbol(value)
        assert ChangeBoilerControl.symbol_to_value(symbol) == value
