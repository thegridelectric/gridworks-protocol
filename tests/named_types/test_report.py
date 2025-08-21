"""Tests report type, version 002"""

from gwproto.named_types import Report


def test_report_generated() -> None:
    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeInstanceId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "AboutGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta",
        "SlotStartUnixS": 1656945300,
        "SlotDurationS": 300,
        "ChannelReadingList": [
            {
                "ChannelName": "hp-odu-pwr",
                "ValueList": [26, 96, 196],
                "ScadaReadTimeUnixMsList": [
                    1708518800235,
                    1708518808236,
                    1708518809232,
                ],
                "TypeName": "channel.readings",
                "Version": "002",
            },
            {
                "ChannelName": "dist-pump-pwr",
                "ValueList": [14],
                "ScadaReadTimeUnixMsList": [1708518800235],
                "TypeName": "channel.readings",
                "Version": "002",
            },
        ],
        "StateList": [],
        "FsmReportList": [],
        "MessageCreatedMs": 1656945600044,
        "Id": "4dab57dd-8b4e-4ea4-90a3-d63df9eeb061",
        "TypeName": "report",
        "Version": "002",
    }

    d2 = Report.from_dict(d).to_dict()
    assert d2 == d
