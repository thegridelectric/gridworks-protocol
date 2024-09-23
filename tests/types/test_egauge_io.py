"""Tests egauge.io type, version 000"""

from gwproto.types import EgaugeIo


def test_egauge_io_generated() -> None:
    d = {
        "InputConfig": {
            "Address": 9004,
            "Name": "HP IDU Power",
            "Description": "",
            "Type": "f32",
            "Denominator": 1,
            "Unit": "W",
            "TypeName": "egauge.register.config",
            "Version": "000",
        },
        "OutputConfig": {
            "AboutNodeName": "hp-idu",
            "ReportOnChange": True,
            "SamplePeriodS": 60,
            "Exponent": 0,
            "AsyncReportThreshold": 0.05,
            "NameplateMaxValue": 4500,
            "TypeName": "telemetry.reporting.config",
            "Version": "001",
            "TelemetryName": "PowerW",
            "Unit": "W",
        },
        "TypeName": "egauge.io",
        "Version": "000",
    }
    assert EgaugeIo.model_validate(d).model_dump() == d
