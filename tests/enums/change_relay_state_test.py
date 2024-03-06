"""
Tests for enum change.relay.state.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeRelayState


def test_change_relay_state() -> None:
    assert set(ChangeRelayState.values()) == {
        "",
        "",
    }

    assert ChangeRelayState.default() == ChangeRelayState.
    assert ChangeRelayState.enum_name() == "change.relay.state"
    assert ChangeRelayState.enum_version() == "000"

    assert ChangeRelayState.version("") == "000"
    assert ChangeRelayState.version("") == "000"

    for value in ChangeRelayState.values():
        symbol = ChangeRelayState.value_to_symbol(value)
        assert ChangeRelayState.symbol_to_value(symbol) == value
