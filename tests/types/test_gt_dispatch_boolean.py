"""Tests gt.dispatch.boolean type, version 110"""

from gwproto.types import GtDispatchBoolean


def test_gt_dispatch_boolean_generated() -> None:
    d = {
        "AboutNodeName": "a.elt1.relay",
        "ToGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1",
        "FromGNodeInstanceId": "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32",
        "RelayState": 0,
        "SendTimeUnixMs": 1657024737661,
        "TypeName": "gt.dispatch.boolean",
        "Version": "110",
    }
    payload = GtDispatchBoolean.model_validate(d)
    assert payload.model_dump() == d
