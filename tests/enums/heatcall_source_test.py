"""
Tests for enum heatcall.source.000 from the GridWorks Type Registry.
"""

from gwproto.enums import HeatcallSource


def test_heatcall_source() -> None:
    assert set(HeatcallSource.values()) == {
        "WallThermostat",
        "Scada",
    }

    assert HeatcallSource.default() == HeatcallSource.WallThermostat
    assert HeatcallSource.enum_name() == "heatcall.source"
    assert HeatcallSource.enum_version() == "000"
