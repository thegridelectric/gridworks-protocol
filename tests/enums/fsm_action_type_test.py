"""
Tests for enum sh.fsm.action.type.000 from the GridWorks Type Registry.
"""

from gwproto.enums import FsmActionType


def test_fsm_action_type() -> None:
    assert set(FsmActionType.values()) == {
        "RelayPinSet",
        "Analog010VSignalSet",
        "Analog420maSignalSet",
    }

    assert FsmActionType.default() == FsmActionType.RelayPinSet
    assert FsmActionType.enum_name() == "sh.fsm.action.type"
    assert FsmActionType.enum_version() == "000"

    assert FsmActionType.version("RelayPinSet") == "000"
    assert FsmActionType.version("Analog010VSignalSet") == "000"
    assert FsmActionType.version("Analog420maSignalSet") == "000"
