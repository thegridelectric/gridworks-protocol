"""Tests ticklist.hall.report type, version 000"""

from gwproto.named_types import TicklistHallReport


def test_ticklist_hall_report_generated() -> None:
    d = {
        "TerminalAssetAlias": "d1.isone.ct.newhaven.orange1.ta",
        "ChannelName": "store-flow",
        "ScadaReceivedUnixMs": 1730120522258,
        "Ticklist": {
            "HwUid": "pico_1fa376",
            "FirstTickTimestampNanoSecond": 1730120485296209000,
            "RelativeMicrosecondList": [1730120513626650],
            "PicoBeforePostTimestampNanoSecond": 1730120522058825000,
            "TypeName": "ticklist.hall",
            "Version": "101",
        },
        "TypeName": "ticklist.hall.report",
        "Version": "000",
    }

    d2 = TicklistHallReport.from_dict(d).to_dict()

    assert d2 == d
