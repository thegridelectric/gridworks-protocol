"""Tests ticklist.reed type, version 101"""

from gwproto.named_types import TicklistReed


def test_ticklist_reed_generated() -> None:
    d = {
        "HwUid": "pico_1fa376",
        "FirstTickTimestampNanoSecond": 1730120485296209000,
        "RelativeMillisecondList": [1730120513626],
        "PicoBeforePostTimestampNanoSecond": 1730120522058825000,
        "TypeName": "ticklist.reed",
        "Version": "101",
    }

    d2 = TicklistReed.from_dict(d).to_dict()

    assert d2 == d
