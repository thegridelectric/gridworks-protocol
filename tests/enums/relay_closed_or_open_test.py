"""
Tests for enum relay.closed.or.open.000 from the GridWorks Type Registry.
"""
from gwproto.enums import RelayClosedOrOpen


def test_relay_closed_or_open() -> None:
    assert set(RelayClosedOrOpen.values()) == {
        "RelayClosed",
        "RelayOpen",
    }

    assert RelayClosedOrOpen.default() == RelayClosedOrOpen.RelayClosed
    assert RelayClosedOrOpen.enum_name() == "relay.closed.or.open"
