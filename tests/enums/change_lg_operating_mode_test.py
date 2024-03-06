"""
Tests for enum change.lg.operating.mode.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeLgOperatingMode


def test_change_lg_operating_mode() -> None:
    assert set(ChangeLgOperatingMode.values()) == {
        "",
        "",
    }

    assert ChangeLgOperatingMode.default() == ChangeLgOperatingMode.
    assert ChangeLgOperatingMode.enum_name() == "change.lg.operating.mode"
    assert ChangeLgOperatingMode.enum_version() == "000"

    assert ChangeLgOperatingMode.version("") == "000"
    assert ChangeLgOperatingMode.version("") == "000"

    for value in ChangeLgOperatingMode.values():
        symbol = ChangeLgOperatingMode.value_to_symbol(value)
        assert ChangeLgOperatingMode.symbol_to_value(symbol) == value
