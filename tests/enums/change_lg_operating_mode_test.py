"""
Tests for enum change.lg.operating.mode.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeLgOperatingMode


def test_change_lg_operating_mode() -> None:
    assert set(ChangeLgOperatingMode.values()) == {
        "SwitchToDhw",
        "SwitchToHeat",
    }

    assert ChangeLgOperatingMode.default() == ChangeLgOperatingMode.SwitchToDhw
    assert ChangeLgOperatingMode.enum_name() == "change.lg.operating.mode"
    assert ChangeLgOperatingMode.enum_version() == "000"

    assert ChangeLgOperatingMode.version("SwitchToDhw") == "000"
    assert ChangeLgOperatingMode.version("SwitchToHeat") == "000"

    for value in ChangeLgOperatingMode.values():
        symbol = ChangeLgOperatingMode.value_to_symbol(value)
        assert ChangeLgOperatingMode.symbol_to_value(symbol) == value
