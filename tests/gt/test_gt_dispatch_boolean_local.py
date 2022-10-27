"""Tests gt.dispatch.boolean.local type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.errors import SchemaError
from gwproto.messages import GtDispatchBooleanLocal
from gwproto.messages import GtDispatchBooleanLocal_Maker as Maker


def test_gt_dispatch_boolean_local_generated():

    d = {
        "SendTimeUnixMs": 1657025211851,
        "FromNodeAlias": "a.s",
        "AboutNodeAlias": "a.elt1.relay",
        "RelayState": 1,
        "TypeAlias": "gt.dispatch.boolean.local",
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
        send_time_unix_ms=gw_tuple.SendTimeUnixMs,
        from_node_alias=gw_tuple.FromNodeAlias,
        about_node_alias=gw_tuple.AboutNodeAlias,
        relay_state=gw_tuple.RelayState,
        #
    ).tuple
    assert payload == gw_tuple

    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["SendTimeUnixMs"]
    with pytest.raises(ValidationError):
        GtDispatchBooleanLocal(**d2)

    d2 = dict(d)
    del d2["FromNodeAlias"]
    with pytest.raises(ValidationError):
        GtDispatchBooleanLocal(**d2)

    d2 = dict(d)
    del d2["AboutNodeAlias"]
    with pytest.raises(ValidationError):
        GtDispatchBooleanLocal(**d2)

    d2 = dict(d)
    del d2["RelayState"]
    with pytest.raises(ValidationError):
        GtDispatchBooleanLocal(**d2)

    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, SendTimeUnixMs="1657025211851.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SendTimeUnixMs="1657025211851")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, SendTimeUnixMs=1657025211851.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, FromNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AboutNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayState="1.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayState="1")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, RelayState=1.1)
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

    d2 = dict(d, SendTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AboutNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayState=2)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
