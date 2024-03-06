"""
Tests for enum change.valve.state.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeValveState


def test_change_valve_state() -> None:
    assert set(ChangeValveState.values()) == {
        "",
        "",
    }

    assert ChangeValveState.default() == ChangeValveState.
    assert ChangeValveState.enum_name() == "change.valve.state"
    assert ChangeValveState.enum_version() == "000"

    assert ChangeValveState.version("") == "000"
    assert ChangeValveState.version("") == "000"

    for value in ChangeValveState.values():
        symbol = ChangeValveState.value_to_symbol(value)
        assert ChangeValveState.symbol_to_value(symbol) == value
