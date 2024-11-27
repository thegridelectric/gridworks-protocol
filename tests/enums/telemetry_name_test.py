"""
Tests for enum spaceheat.telemetry.name.002 from the GridWorks Type Registry.
"""

from gwproto.enums import TelemetryName


def test_telemetry_name() -> None:
    assert set(TelemetryName.values()) == {
        "Unknown",
        "PowerW",
        "RelayState",
        "WaterTempCTimes1000",
        "WaterTempFTimes1000",
        "GpmTimes100",
        "CurrentRmsMicroAmps",
        "GallonsTimes100",
        "VoltageRmsMilliVolts",
        "MilliWattHours",
        "MicroHz",
        "AirTempCTimes1000",
        "AirTempFTimes1000",
        "ThermostatState",
        "MicroVolts",
        "VoltsTimesTen",
    }

    assert TelemetryName.default() == TelemetryName.Unknown
    assert TelemetryName.enum_name() == "spaceheat.telemetry.name"
    assert TelemetryName.enum_version() == "002"
