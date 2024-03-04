"""Tests fsm.atomic.report type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import FsmAtomicReport_Maker as Maker
from gwproto.enums import FsmActionType


def test_fsm_atomic_report_generated() -> None:
    d = {
        "FromHandle": ,
        "IsAction": ,
        "ActionTypeGtEnumSymbol": ,
        "Action": ,
        "UnixTimeMs": ,
        "TypeName": "fsm.atomic.report",
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
        is_action=gtuple.IsAction,
        action_type=gtuple.ActionType,
        action=gtuple.Action,
        unix_time_ms=gtuple.UnixTimeMs,
        
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
    del d2["FromHandle"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["IsAction"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["UnixTimeMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "ActionType" in d2.keys():
        del d2["ActionType"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "Action" in d2.keys():
        del d2["Action"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, IsAction="this is not a boolean")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ActionTypeGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).ActionType == FsmActionType.default()

    d2 = dict(d, UnixTimeMs=".1")
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

    d2 = dict(d, FromHandle="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, UnixTimeMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
