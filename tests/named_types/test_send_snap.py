"""Tests send.snap type, version 000"""

from gwproto.named_types import SendSnap


def test_send_snap_generated() -> None:
    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1",
        "TypeName": "send.snap",
        "Version": "000",
    }

    d2 = SendSnap.from_dict(d).to_dict()
    assert d2 == d
