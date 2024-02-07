"""
Tests for enum control.signal.type.000 from the GridWorks Type Registry.
"""
from gwproto.enums import ControlSignalType


def test_control_signal_type() -> None:
    assert set(ControlSignalType.values()) == {
        "ChangeRelayState",
        "Analog010V",
        "Analog420mA",
        "ChangeValveState",
        "ChangeStoreFlowDirection",
        "ChangeHeatcallSource",
        "ChangeBoilerControl",
        "ChangeLgOperatingMode",
    }

    assert ControlSignalType.default() == ControlSignalType.ChangeRelayState
    assert ControlSignalType.enum_name() == "control.signal.type"
    assert ControlSignalType.enum_version() == "000"

    assert ControlSignalType.version("ChangeRelayState") == "000"
    assert ControlSignalType.version("Analog010V") == "000"
    assert ControlSignalType.version("Analog420mA") == "000"
    assert ControlSignalType.version("ChangeValveState") == "000"
    assert ControlSignalType.version("ChangeStoreFlowDirection") == "000"
    assert ControlSignalType.version("ChangeHeatcallSource") == "000"
    assert ControlSignalType.version("ChangeBoilerControl") == "000"
    assert ControlSignalType.version("ChangeLgOperatingMode") == "000"

    for value in ControlSignalType.values():
        symbol = ControlSignalType.value_to_symbol(value)
        assert ControlSignalType.symbol_to_value(symbol) == value
