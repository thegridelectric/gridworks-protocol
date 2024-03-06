"""
Tests for enum relay.energization.state.000 from the GridWorks Type Registry.
"""
from gwproto.enums import RelayEnergizationState


def test_relay_energization_state() -> None:
    assert set(RelayEnergizationState.values()) == {
        "",
        "",
    }

    assert RelayEnergizationState.default() == RelayEnergizationState.
    assert RelayEnergizationState.enum_name() == "relay.energization.state"
    assert RelayEnergizationState.enum_version() == "000"

    assert RelayEnergizationState.version("") == "000"
    assert RelayEnergizationState.version("") == "000"

    for value in RelayEnergizationState.values():
        symbol = RelayEnergizationState.value_to_symbol(value)
        assert RelayEnergizationState.symbol_to_value(symbol) == value
