"""Tests fsm.event type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import FsmEvent_Maker as Maker


def test_fsm_event_generated() -> None:
    d = {
        "FromHandle": ,
        "ToHandle": ,
        "Name": ,
        "SendTimeUnixMs": ,
        "TypeName": "fsm.event",
        "Version": "000",
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
        from_handle=gtuple.FromHandle,
        to_handle=gtuple.ToHandle,
        name=gtuple.Name,
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

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "FromHandle" in d2.keys():
        del d2["FromHandle"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "ToHandle" in d2.keys():
        del d2["ToHandle"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "Name" in d2.keys():
        del d2["Name"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "SendTimeUnixMs" in d2.keys():
        del d2["SendTimeUnixMs"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
