"""
Tests for enum sh.fsm.name.000 from the GridWorks Type Registry.
"""

from gwproto.enums import FsmName


def test_fsm_name() -> None:
    assert set(FsmName.values()) == {
        "Unknown",
        "IsoValve",
        "StoreFlowDirection",
        "RelayState",
    }

    assert FsmName.default() == FsmName.IsoValve
    assert FsmName.enum_name() == "sh.fsm.name"
    assert FsmName.enum_version() == "000"

    assert FsmName.version("Unknown") == "000"
    assert FsmName.version("IsoValve") == "000"
    assert FsmName.version("StoreFlowDirection") == "000"
    assert FsmName.version("RelayState") == "000"

    for value in FsmName.values():
        symbol = FsmName.value_to_symbol(value)
        assert FsmName.symbol_to_value(symbol) == value
