"""
Tests for enum change.heatcall.source.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeHeatcallSource


def test_change_heatcall_source() -> None:
    assert set(ChangeHeatcallSource.values()) == {
        "",
        "",
    }

    assert ChangeHeatcallSource.default() == ChangeHeatcallSource.
    assert ChangeHeatcallSource.enum_name() == "change.heatcall.source"
    assert ChangeHeatcallSource.enum_version() == "000"

    assert ChangeHeatcallSource.version("") == "000"
    assert ChangeHeatcallSource.version("") == "000"

    for value in ChangeHeatcallSource.values():
        symbol = ChangeHeatcallSource.value_to_symbol(value)
        assert ChangeHeatcallSource.symbol_to_value(symbol) == value
