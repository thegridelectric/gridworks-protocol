"""
Tests for enum store.flow.direction.state.000 from the GridWorks Type Registry.
"""
from gwproto.enums import StoreFlowDirection


def test_store_flow_direction() -> None:
    assert set(StoreFlowDirection.values()) == {
        "Discharging",
        "ValveMovingToCharging",
        "Charging",
        "ValveMovingToDischarging",
    }

    assert StoreFlowDirection.default() == StoreFlowDirection.Discharging
    assert StoreFlowDirection.enum_name() == "store.flow.direction.state"
