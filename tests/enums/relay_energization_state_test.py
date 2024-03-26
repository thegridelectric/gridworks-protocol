"""
Tests for enum relay.energization.state.000 from the GridWorks Type Registry.
"""

from gwproto.enums import RelayEnergizationState


def test_relay_energization_state() -> None:
    assert set(RelayEnergizationState.values()) == {
        0,
        1,
    }

    assert RelayEnergizationState.default() == RelayEnergizationState.DeEnergized
    assert RelayEnergizationState.enum_name() == "relay.energization.state"
