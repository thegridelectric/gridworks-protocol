"""
Tests for enum change.store.flow.direction.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ChangeStoreFlowDirection


def test_change_store_flow_direction() -> None:
    assert set(ChangeStoreFlowDirection.values()) == {
        "Discharge",
        "Charge",
    }

    assert ChangeStoreFlowDirection.default() == ChangeStoreFlowDirection.Discharge
    assert ChangeStoreFlowDirection.enum_name() == "change.store.flow.direction"
    assert ChangeStoreFlowDirection.enum_version() == "000"

    assert ChangeStoreFlowDirection.version("Discharge") == "000"
    assert ChangeStoreFlowDirection.version("Charge") == "000"

    for value in ChangeStoreFlowDirection.values():
        symbol = ChangeStoreFlowDirection.value_to_symbol(value)
        assert ChangeStoreFlowDirection.symbol_to_value(symbol) == value
