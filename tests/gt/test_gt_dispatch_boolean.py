"""Tests gt.dispatch.boolean type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.errors import SchemaError
from gwproto.messages import GtDispatchBoolean
from gwproto.messages import GtDispatchBoolean_Maker as Maker


def test_gt_dispatch_boolean_generated():

    d = {
        "AboutNodeAlias": "a.elt1.relay",
        "ToGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1",
        "FromGNodeId": "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32",
        "RelayState": 0,
        "SendTimeUnixMs": 1657024737661,
        "TypeAlias": "gt.dispatch.boolean",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gw_type = json.dumps(d)
    gw_tuple = Maker.type_to_tuple(gw_type)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple

    # test Maker init
    payload = Maker(
        about_node_alias=gw_tuple.AboutNodeAlias,
        to_g_node_alias=gw_tuple.ToGNodeAlias,
        from_g_node_alias=gw_tuple.FromGNodeAlias,
        from_g_node_id=gw_tuple.FromGNodeId,
        relay_state=gw_tuple.RelayState,
        send_time_unix_ms=gw_tuple.SendTimeUnixMs,
        #
    ).tuple
    assert payload == gw_tuple

    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["AboutNodeAlias"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**d2)

    d2 = dict(d)
    del d2["ToGNodeAlias"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**d2)

    d2 = dict(d)
    del d2["FromGNodeAlias"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**d2)

    d2 = dict(d)
    del d2["FromGNodeId"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**d2)

    d2 = dict(d)
    del d2["RelayState"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**d2)

    d2 = dict(d)
    del d2["SendTimeUnixMs"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**d2)

    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, AboutNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ToGNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeId={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayState="0.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayState="0")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, RelayState=0.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, SendTimeUnixMs="1657024737661.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SendTimeUnixMs="1657024737661")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, SendTimeUnixMs=1657024737661.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeAlias="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, AboutNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ToGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayState=2)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SendTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
