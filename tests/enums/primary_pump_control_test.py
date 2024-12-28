"""
Tests for enum primary.pump.control.000 from the GridWorks Type Registry.
"""

from gwproto.enums import PrimaryPumpControl


def test_primary_pump_control() -> None:
    assert set(PrimaryPumpControl.values()) == {
        "HeatPump",
        "Scada",
    }

    assert PrimaryPumpControl.default() == PrimaryPumpControl.HeatPump
    assert PrimaryPumpControl.enum_name() == "primary.pump.control"
    assert PrimaryPumpControl.enum_version() == "000"
