"""Tests gt.dispatch.boolean.local type, version 110"""

from gwproto.types import GtDispatchBooleanLocal


def test_gt_dispatch_boolean_local_generated() -> None:
    d = {
        "RelayState": 1,
        "AboutNodeName": "a.elt1.relay",
        "FromNodeName": "a.s",
        "SendTimeUnixMs": 1657025211851,
        "TypeName": "gt.dispatch.boolean.local",
        "Version": "110",
    }
    payload = GtDispatchBooleanLocal.model_validate(d)
    assert payload.model_dump() == d
