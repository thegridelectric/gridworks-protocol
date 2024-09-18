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

    assert Unit.version("Unknown") == "000"
    assert Unit.version("Unitless") == "000"
    assert Unit.version("W") == "000"
    assert Unit.version("Celcius") == "000"
    assert Unit.version("Fahrenheit") == "000"
    assert Unit.version("Gpm") == "000"
    assert Unit.version("WattHours") == "000"
    assert Unit.version("AmpsRms") == "000"
    assert Unit.version("VoltsRms") == "000"
    assert Unit.version("Gallons") == "000"
    assert Unit.version("ThermostatStateEnum") == "001"
