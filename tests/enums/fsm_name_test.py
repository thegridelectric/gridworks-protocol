"""
Tests for enum sh.fsm.name.000 from the GridWorks Type Registry.
"""

from gwproto.enums import FsmName


def test_fsm_name() -> None:
    assert set(FsmName.values()) == {
        "Unknown",
        "StoreFlowDirection",
        "RelayState",
        "RelayPinState",
    }

    assert FsmName.default() == FsmName.StoreFlowDirection
    assert FsmName.enum_name() == "sh.fsm.name"
    assert FsmName.enum_version() == "000"
