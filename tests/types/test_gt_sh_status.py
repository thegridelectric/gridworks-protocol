"""Tests gt.sh.status type, version 110"""

from gwproto.types import GtShStatus


def test_gt_sh_status_generated() -> None:
    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "AboutGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta",
        "SlotStartUnixS": 1656945300,
        "ReportingPeriodS": 300,
        "SimpleTelemetryList": [],
        "MultipurposeTelemetryList": [
            {
                "AboutNodeAlias": "elt1",
                "ValueList": [18000],
                "ReadTimeUnixMsList": [1656945390152],
                "SensorNodeAlias": "power-meter",
                "TypeName": "gt.sh.multipurpose.telemetry.status",
                "Version": "101",
                "TelemetryName": "CurrentRmsMicroAmps",
            }
        ],
        "BooleanactuatorCmdList": [
            {
                "ShNodeAlias": "elt1",
                "RelayStateCommandList": [1],
                "CommandTimeUnixMsList": [1656945413464],
                "TypeName": "gt.sh.booleanactuator.cmd.status",
                "Version": "100",
            }
        ],
        "StatusUid": "dedc25c2-8276-4b25-abd6-f53edc79b62b",
        "TypeName": "gt.sh.status",
        "Version": "110",
    }
    assert GtShStatus.model_validate(d).model_dump() == d
