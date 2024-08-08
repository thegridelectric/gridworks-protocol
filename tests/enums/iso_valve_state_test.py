"""
Tests for enum iso.valve.state.000 from the GridWorks Type Registry.
"""

from gwproto.enums import IsoValveState


def test_iso_valve_state() -> None:
    assert set(IsoValveState.values()) == {
        "Open",
        "Closing",
        "Closed",
        "Opening",
    }

    assert IsoValveState.default() == IsoValveState.Open
    assert IsoValveState.enum_name() == "iso.valve.state"
