"""
Tests for enum heat.pump.control.000 from the GridWorks Type Registry.
"""

from gwproto.enums import HeatPumpControl


def test_heat_pump_control() -> None:
    assert set(HeatPumpControl.values()) == {
        "BufferTankAquastat",
        "Scada",
    }

    assert HeatPumpControl.default() == HeatPumpControl.BufferTankAquastat
    assert HeatPumpControl.enum_name() == "heat.pump.control"
    assert HeatPumpControl.enum_version() == "000"
