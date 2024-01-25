"""Tests gt.dispatch.boolean type, version 111"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import GtDispatchBoolean_Maker as Maker


def test_gt_dispatch_boolean_generated() -> None:
    d = {
        "ToGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1",
        "FromGNodeInstanceId": "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32",
        "AboutNodeName": "a.elt1.relay",
        "RelayState": 0,
        "SendTimeUnixMs": 1657024737661,
        "TypeName": "gt.dispatch.boolean",
        "Version": "111",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # test Maker init
    t = Maker(
        to_g_node_alias=gtuple.ToGNodeAlias,
        from_g_node_alias=gtuple.FromGNodeAlias,
        from_g_node_instance_id=gtuple.FromGNodeInstanceId,
        about_node_name=gtuple.AboutNodeName,
        relay_state=gtuple.RelayState,
        send_time_unix_ms=gtuple.SendTimeUnixMs,
    ).tuple
    assert t == gtuple

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ToGNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FromGNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FromGNodeInstanceId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AboutNodeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RelayState"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SendTimeUnixMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, RelayState="0.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SendTimeUnixMs="1657024737661.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ToGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeInstanceId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AboutNodeName="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayState=2)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SendTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
