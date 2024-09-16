"""Tests gt.sh.status type, version 110"""

from gwproto.types import GtShStatus


def test_gt_sh_status_generated() -> None:
    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "AboutGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta",
        "SlotStartUnixS": 1656945300,
        "ReportingPeriodS": 300,
        "SimpleTelemetryList": [
            {
                "ValueList": [0, 1],
                "ReadTimeUnixMsList": [1656945400527, 1656945414270],
                "ShNodeAlias": "a.elt1.relay",
                "TypeName": "gt.sh.simple.telemetry.status",
                "Version": "100",
                "TelemetryName": "RelayState",
            }
        ],
        "MultipurposeTelemetryList": [
            {
                "AboutNodeAlias": "a.elt1",
                "ValueList": [18000],
                "ReadTimeUnixMsList": [1656945390152],
                "SensorNodeAlias": "a.m",
                "TypeName": "gt.sh.multipurpose.telemetry.status",
                "Version": "100",
                "TelemetryName": "CurrentRmsMicroAmps",
            }
        ],
        "BooleanactuatorCmdList": [
            {
                "ShNodeAlias": "a.elt1.relay",
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
