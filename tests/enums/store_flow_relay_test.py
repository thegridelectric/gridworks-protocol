"""
Tests for enum store.flow.relay.000 from the GridWorks Type Registry.
"""

from gwproto.enums import StoreFlowRelay


def test_store_flow_relay() -> None:
    assert set(StoreFlowRelay.values()) == {
        "DischargingStore",
        "ChargingStore",
    }

    assert StoreFlowRelay.default() == StoreFlowRelay.DischargingStore
    assert StoreFlowRelay.enum_name() == "store.flow.relay"
    assert StoreFlowRelay.enum_version() == "000"
