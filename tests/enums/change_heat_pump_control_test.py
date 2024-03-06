"""
Tests for enum change.heat.pump.control.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeHeatPumpControl


def test_change_heat_pump_control() -> None:
    assert set(ChangeHeatPumpControl.values()) == {
        "",
        "",
    }

    assert ChangeHeatPumpControl.default() == ChangeHeatPumpControl.
    assert ChangeHeatPumpControl.enum_name() == "change.heat.pump.control"
    assert ChangeHeatPumpControl.enum_version() == "000"

    assert ChangeHeatPumpControl.version("") == "000"
    assert ChangeHeatPumpControl.version("") == "000"

    for value in ChangeHeatPumpControl.values():
        symbol = ChangeHeatPumpControl.value_to_symbol(value)
        assert ChangeHeatPumpControl.symbol_to_value(symbol) == value
