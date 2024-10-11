"""
Tests for enum spaceheat.unit.001 from the GridWorks Type Registry.
"""

from gwproto.enums import Unit


def test_unit() -> None:
    assert set(Unit.values()) == {
        "Unknown",
        "Unitless",
        "W",
        "Celcius",
        "Fahrenheit",
        "Gpm",
        "WattHours",
        "AmpsRms",
        "VoltsRms",
        "Gallons",
        "ThermostatStateEnum",
    }

    assert Unit.default() == Unit.Unknown
    assert Unit.enum_name() == "spaceheat.unit"
    assert Unit.enum_version() == "001"
