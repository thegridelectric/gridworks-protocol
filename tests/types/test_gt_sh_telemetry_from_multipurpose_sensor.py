"""Tests gt.sh.telemetry.from.multipurpose.sensor type, version 100"""

from gwproto.types import GtShTelemetryFromMultipurposeSensor


def test_gt_sh_telemetry_from_multipurpose_sensor_generated() -> None:
    d = {
        "ScadaReadTimeUnixMs": 1656587343297,
        "AboutNodeAliasList": ["a.elt1"],
        "TelemetryNameList": ["PowerW"],
        "ValueList": [18000],
        "TypeName": "gt.sh.telemetry.from.multipurpose.sensor",
        "Version": "100",
    }
    assert GtShTelemetryFromMultipurposeSensor.model_validate(d).model_dump() == d
