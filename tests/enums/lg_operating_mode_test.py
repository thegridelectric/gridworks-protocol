"""
Tests for enum lg.operating.mode.000 from the GridWorks Type Registry.
"""
from gwproto.enums import LgOperatingMode


def test_lg_operating_mode() -> None:
    assert set(LgOperatingMode.values()) == {
        "Dhw",
        "Heat",
    }

    assert LgOperatingMode.default() == LgOperatingMode.Heat
    assert LgOperatingMode.enum_name() == "lg.operating.mode"
    assert LgOperatingMode.enum_version() == "000"

    assert LgOperatingMode.version("Dhw") == "000"
    assert LgOperatingMode.version("Heat") == "000"

    for value in LgOperatingMode.values():
        symbol = LgOperatingMode.value_to_symbol(value)
        assert LgOperatingMode.symbol_to_value(symbol) == value
