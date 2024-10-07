"""Tests gt.sh.multipurpose.telemetry.status type, version 100"""

from gwproto.types import GtShMultipurposeTelemetryStatus


def test_gt_sh_multipurpose_telemetry_status_generated() -> None:
    d = {
        "AboutNodeAlias": "elt1",
        "SensorNodeAlias": "power-meter",
        "TelemetryName": "PowerW",
        "ValueList": [4559],
        "ReadTimeUnixMsList": [1656443705023],
        "TypeName": "gt.sh.multipurpose.telemetry.status",
        "Version": "101",
    }
    assert GtShMultipurposeTelemetryStatus.model_validate(d).model_dump() == d
