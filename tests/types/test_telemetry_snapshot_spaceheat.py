"""Tests telemetry.snapshot.spaceheat type, version 000"""

from gwproto.types import TelemetrySnapshotSpaceheat


def test_telemetry_snapshot_spaceheat_generated() -> None:
    d = {
        "ReportTimeUnixMs": 1656363448000,
        "AboutNodeAliasList": ["a-elt1-relay", "a-tank-temp0"],
        "ValueList": [1, 66086],
        "TelemetryNameList": ["RelayState", "WaterTempCTimes1000"],
        "TypeName": "telemetry.snapshot.spaceheat",
        "Version": "000",
    }
    assert TelemetrySnapshotSpaceheat.model_validate(d).model_dump() == d
