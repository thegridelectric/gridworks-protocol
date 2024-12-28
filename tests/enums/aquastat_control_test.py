"""
Tests for enum aquastat.control.state.000 from the GridWorks Type Registry.
"""

from gwproto.enums import AquastatControl


def test_aquastat_control() -> None:
    assert set(AquastatControl.values()) == {
        "Boiler",
        "Scada",
    }

    assert AquastatControl.default() == AquastatControl.Boiler
    assert AquastatControl.enum_name() == "aquastat.control.state"
    assert AquastatControl.enum_version() == "000"
