"""Tests gt.dispatch.boolean type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.errors import SchemaError
from gwproto.messages import GtDispatchBoolean


def test_pydantic_dispatch_boolean():
    args = {
        "AboutNodeAlias": "a.elt1.relay",
        "ToGNodeAlias": "dw1.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeAlias": "dw1.isone.ct.newhaven.orange1",
        "FromGNodeId": "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32",
        "RelayState": 0,
        "SendTimeUnixMs": 1657024737661,
        "TypeAlias": "gt.dispatch.boolean",
    }

    GtDispatchBoolean(**args)

    args2 = dict(args)
    del args2["AboutNodeAlias"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**args2)

    args2 = dict(args, RelayState=0.1)
    payload = GtDispatchBoolean(**args2)
    assert payload.RelayState == 0

    args2 = dict(args, RelayState="0")
    payload = GtDispatchBoolean(**args2)
    assert payload.RelayState == 0

    args2 = dict(args)
    args2["RelayState"] = "0.1"
    with pytest.raises(ValidationError):
        payload = GtDispatchBoolean(**args2)

    args2 = dict(args, AboutNodeAlias={})
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**args2)

    args2 = dict(args)
    args2["SendTimeUnixMs"] = 1657024737661.1
    payload = GtDispatchBoolean(**args2)
    assert payload.SendTimeUnixMs == 1657024737661

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    args2 = dict(args, AboutNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**args2)

    d["AboutNodeAlias"] = "a.b-h"
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["AboutNodeAlias"] = "a.elt1.relay"

    d["ToGNodeAlias"] = "a.b-h"
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["ToGNodeAlias"] = "dwtest.isone.ct.newhaven.orange1.ta.scada"

    d["FromGNodeAlias"] = "a.b-h"
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["FromGNodeAlias"] = "dwtest.isone.ct.newhaven.orange1"

    d["FromGNodeId"] = "d4be12d5-33ba-4f1f-b9e5"
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["FromGNodeId"] = "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32"

    d["RelayState"] = 2
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["RelayState"] = 0

    d["SendTimeUnixMs"] = 1656245000
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["SendTimeUnixMs"] = 1657024737661

    # End of Test
