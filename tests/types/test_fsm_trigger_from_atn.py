"""Tests fsm.trigger.from.atn type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import FsmEventType
from gwproto.types import FsmEvent, FsmTriggerFromAtn
from gwproto.types import FsmTriggerFromAtnMaker as Maker
from pydantic import ValidationError


def test_fsm_trigger_from_atn_generated() -> None:
    t = FsmTriggerFromAtn(
        ToGNodeAlias="d1.isone.ct.newhaven.rose.scada",
        FromGNodeAlias="d1.isone.ct.newhaven.rose",
        FromGNodeInstanceId="645cb8d9-36c2-42e5-8d8b-7877019955c6",
        Trigger=FsmEvent(
            FromHandle="a",
            ToHandle="a.iso-valve",
            EventType=FsmEventType.ChangeValveState,
            EventName="OpenValve",
            TriggerId="12da4269-63c3-44f4-ab65-3ee5e29329fe",
            SendTimeUnixMs=1709923791330,
        ),
    )

    d = {
        "ToGNodeAlias": "d1.isone.ct.newhaven.rose.scada",
        "FromGNodeAlias": "d1.isone.ct.newhaven.rose",
        "FromGNodeInstanceId": "645cb8d9-36c2-42e5-8d8b-7877019955c6",
        "Trigger": {
            "FromHandle": "a",
            "ToHandle": "a.iso-valve",
            "EventTypeGtEnumSymbol": "c234ee7a",
            "EventName": "OpenValve",
            "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
            "SendTimeUnixMs": 1709923791330,
            "TypeName": "fsm.event",
            "Version": "000",
        },
        "TypeName": "fsm.trigger.from.atn",
        "Version": "000",
    }
    assert t.as_dict() == d

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple(d)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)
    assert gtuple == t

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    ######################################
    # GwTypeError raised if missing a required attribute
    ######################################

    d2 = d.copy()
    del d2["TypeName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ToGNodeAlias"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["FromGNodeAlias"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["FromGNodeInstanceId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["Trigger"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
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
