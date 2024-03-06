"""
Tests for enum lg.operating.mode.000 from the GridWorks Type Registry.
"""
from gwproto.enums import LgOperatingMode


def test_lg_operating_mode() -> None:
    assert set(LgOperatingMode.values()) == {
        "",
        "",
    }

    assert LgOperatingMode.default() == LgOperatingMode.
    assert LgOperatingMode.enum_name() == "lg.operating.mode"
    assert LgOperatingMode.enum_version() == "000"

    assert LgOperatingMode.version("") == "000"
    assert LgOperatingMode.version("") == "000"

    for value in LgOperatingMode.values():
        symbol = LgOperatingMode.value_to_symbol(value)
        assert LgOperatingMode.symbol_to_value(symbol) == value
