"""
Tests for enum change.store.flow.relay.000 from the GridWorks Type Registry.
"""

from gwproto.enums import ChangeStoreFlowRelay


def test_change_store_flow_relay() -> None:
    assert set(ChangeStoreFlowRelay.values()) == {
        "DischargeStore",
        "ChargeStore",
    }

    assert ChangeStoreFlowRelay.default() == ChangeStoreFlowRelay.DischargeStore
    assert ChangeStoreFlowRelay.enum_name() == "change.store.flow.relay"
    assert ChangeStoreFlowRelay.enum_version() == "000"
