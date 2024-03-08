"""
Tests for enum relay.closed.or.open.000 from the GridWorks Type Registry.
"""
from gwproto.enums import RelayClosedOrOpen


def test_relay_closed_or_open() -> None:
    assert set(RelayClosedOrOpen.values()) == {
        "",
        "",
    }

    assert RelayClosedOrOpen.default() == RelayClosedOrOpen.
    assert RelayClosedOrOpen.enum_name() == "relay.closed.or.open"
    assert RelayClosedOrOpen.enum_version() == "000"

    assert RelayClosedOrOpen.version("") == "000"
    assert RelayClosedOrOpen.version("") == "000"

    for value in RelayClosedOrOpen.values():
        symbol = RelayClosedOrOpen.value_to_symbol(value)
        assert RelayClosedOrOpen.symbol_to_value(symbol) == value
