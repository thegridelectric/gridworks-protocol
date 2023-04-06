"""Tests for schema enum spaceheat.telemetry.name.000"""
from gwproto.enums import TelemetryName


def test_telemetry_name() -> None:
    assert set(TelemetryName.values()) == {
        "Unknown",
        "PowerW",
        "MilliWattHours",
        "FrequencyMicroHz",
        "AirTempCTimes1000",
        "AirTempFTimes1000",
        "RelayState",
        "WaterTempCTimes1000",
        "WaterTempFTimes1000",
        "GpmTimes100",
        "CurrentRmsMicroAmps",
        "GallonsTimes100",
        "VoltageRmsMilliVolts",
    }

    assert TelemetryName.default() == TelemetryName.Unknown
