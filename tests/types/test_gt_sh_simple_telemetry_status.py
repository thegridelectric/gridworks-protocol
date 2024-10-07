"""Tests gt.sh.simple.telemetry.status type, version 100"""

from gwproto.types import GtShSimpleTelemetryStatus


def test_gt_sh_simple_telemetry_status_generated() -> None:
    d = {
        "ShNodeAlias": "a.elt1.relay",
        "TelemetryName": "CurrentRmsMicroAmps",
        "ValueList": [0],
        "ReadTimeUnixMsList": [1656443705023],
        "TypeName": "gt.sh.simple.telemetry.status",
        "Version": "100",
    }
    assert GtShSimpleTelemetryStatus.model_validate(d).model_dump() == d
