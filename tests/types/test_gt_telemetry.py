"""Tests gt.telemetry type, version 110"""

from gwproto.types import GtTelemetry


def test_gt_telemetry_generated() -> None:
    d = {
        "ScadaReadTimeUnixMs": 1656513094288,
        "Value": 63430,
        "Name": "WaterTempCTimes1000",
        "Exponent": 3,
        "TypeName": "gt.telemetry",
        "Version": "110",
    }
    assert GtTelemetry.model_validate(d).model_dump() == d
