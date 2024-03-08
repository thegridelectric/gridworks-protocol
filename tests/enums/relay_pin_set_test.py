"""
Tests for enum relay.pin.set.000 from the GridWorks Type Registry.
"""
from gwproto.enums import RelayPinSet


def test_relay_pin_set() -> None:
    assert set(RelayPinSet.values()) == {
        "",
        "",
    }

    assert RelayPinSet.default() == RelayPinSet.
    assert RelayPinSet.enum_name() == "relay.pin.set"
    assert RelayPinSet.enum_version() == "000"

    assert RelayPinSet.version("") == "000"
    assert RelayPinSet.version("") == "000"

    for value in RelayPinSet.values():
        symbol = RelayPinSet.value_to_symbol(value)
        assert RelayPinSet.symbol_to_value(symbol) == value
