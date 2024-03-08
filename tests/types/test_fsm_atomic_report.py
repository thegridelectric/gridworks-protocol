"""Tests fsm.atomic.report type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import FsmAtomicReport
from gwproto.types import FsmAtomicReport_Maker as Maker
from gwproto.enums import FsmActionType


def test_fsm_atomic_report_generated() -> None:
    t = FsmAtomicReport(
        FromHandle="h.s.admin.iso-valve",
        IsEvent=True,
        EventType="c234ee7a",
        Event="OpenValve",
        UnixTimeMs=1709923792000,
        TriggerId="12da4269-63c3-44f4-ab65-3ee5e29329fe",)

    d = {
        "FromHandle": "h.s.admin.iso-valve",
        "IsEvent": True,
        "EventTypeGtEnumSymbol": "c234ee7a",
        "Event": "OpenValve",
        "UnixTimeMs": 1709923792000,
        "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
        "TypeName": "fsm.atomic.report",
        "Version": "000",
    }

    assert t.as_dict() == d

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)
    assert gtuple == t

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # test Maker init
    t = Maker(
        from_handle=gtuple.FromHandle,
        is_event=gtuple.IsEvent,
        event_type=gtuple.EventType,
        event=gtuple.Event,
        unix_time_ms=gtuple.UnixTimeMs,
        trigger_id=gtuple.TriggerId,
        
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
    del d2["IsEvent"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["UnixTimeMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TriggerId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "EventType" in d2.keys():
        del d2["EventTypeGtEnumSymbol"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "EventType" in d2.keys():
        del d2["EventType"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "Event" in d2.keys():
        del d2["Event"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, IsEvent="this is not a boolean")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EventTypeGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).EventType == FsmActionType.default()

    d2 = dict(d, UnixTimeMs="1709923792000.1")
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

    d2 = dict(d, TriggerId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
