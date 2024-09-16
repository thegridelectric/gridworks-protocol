"""Tests telemetry.reporting.config type, version 000"""

from gwproto.types import TelemetryReportingConfig


def test_telemetry_reporting_config_generated() -> None:
    d = {
        "TelemetryName": "PowerW",
        "AboutNodeName": "a.elt1",
        "ReportOnChange": True,
        "SamplePeriodS": 300,
        "Exponent": 6,
        "Unit": "W",
        "AsyncReportThreshold": 0.2,
        "NameplateMaxValue": 4000,
        "TypeName": "telemetry.reporting.config",
        "Version": "000",
    }
    assert TelemetryReportingConfig.model_validate(d).model_dump() == d
