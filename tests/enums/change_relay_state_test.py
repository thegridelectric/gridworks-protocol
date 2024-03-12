"""
Tests for enum change.relay.state.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeRelayState


def test_change_relay_state() -> None:
    assert set(ChangeRelayState.values()) == {
        "CloseRelay",
        "OpenRelay",
    }

    assert ChangeRelayState.default() == ChangeRelayState.OpenRelay
    assert ChangeRelayState.enum_name() == "change.relay.state"
