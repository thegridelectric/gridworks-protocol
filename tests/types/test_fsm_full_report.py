"""Tests fsm.full.report type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from pydantic import ValidationError

from gwproto.enums import (
    FsmActionType,
    FsmEventType,
    FsmName,
    FsmReportType,
    RelayPinSet,
)
from gwproto.types import FsmAtomicReport, FsmFullReport
from gwproto.types import FsmFullReportMaker as Maker


def test_fsm_full_report_generated() -> None:
    t = FsmFullReport(
        from_name="admin",
        trigger_id="12da4269-63c3-44f4-ab65-3ee5e29329fe",
        atomic_list=[
            FsmAtomicReport(
                from_handle="admin.iso-valve",
                about_fsm=FsmName.IsoValve,
                report_type=FsmReportType.Event,
                event_type=FsmEventType.ChangeValveState,
                event="OpenValve",
                from_state="Closed",
                to_state="Opening",
                unix_time_ms=1710158001595,
                trigger_id="12da4269-63c3-44f4-ab65-3ee5e29329fe",
            ),
            FsmAtomicReport(
                from_handle="admin.iso-valve.relay",
                about_fsm=FsmName.RelayState,
                report_type=FsmReportType.Event,
                event_type=FsmEventType.ChangeRelayState,
                event="OpenRelay",
                from_state="Closed",
                to_state="Open",
                unix_time_ms=1710158001610,
                trigger_id="12da4269-63c3-44f4-ab65-3ee5e29329fe",
            ),
            FsmAtomicReport(
                from_handle="admin.iso-valve.relay",
                about_fsm=FsmName.RelayState,
                report_type=FsmReportType.Action,
                ActionType=FsmActionType.RelayPinSet,
                Action=RelayPinSet.DeEnergized.value,
                unix_time_ms=1710158001624,
                trigger_id="12da4269-63c3-44f4-ab65-3ee5e29329fe",
            ),
            FsmAtomicReport(
                from_handle="admin.iso-valve",
                about_fsm=FsmName.IsoValve,
                report_type=FsmReportType.Event,
                event_type=FsmEventType.TimerFinished,
                Event="Belimo BallValve232VS 45 second opening timer",
                from_state="Opening",
                ToState="Open",
                unix_time_ms=1710158046849,
                trigger_id="12da4269-63c3-44f4-ab65-3ee5e29329fe",
            ),
        ],
    )

    d = {
        "FromName": "admin",
        "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
        "AtomicList": [
            {
                "FromHandle": "admin.iso-valve",
                "Event": "OpenValve",
                "FromState": "Closed",
                "ToState": "Opening",
                "UnixTimeMs": 1710158001595,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
                "AboutFsmGtEnumSymbol": "0cce8d12",
                "ReportTypeGtEnumSymbol": "6fe49bc1",
                "EventTypeGtEnumSymbol": "c234ee7a",
            },
            {
                "FromHandle": "admin.iso-valve.relay",
                "Event": "OpenRelay",
                "FromState": "Closed",
                "ToState": "Open",
                "UnixTimeMs": 1710158001610,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
                "AboutFsmGtEnumSymbol": "1f560b73",
                "ReportTypeGtEnumSymbol": "6fe49bc1",
                "EventTypeGtEnumSymbol": "00000000",
            },
            {
                "FromHandle": "admin.iso-valve.relay",
                "Action": 0,
                "UnixTimeMs": 1710158001624,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
                "AboutFsmGtEnumSymbol": "1f560b73",
                "ReportTypeGtEnumSymbol": "490d4e1d",
                "ActionTypeGtEnumSymbol": "00000000",
            },
            {
                "FromHandle": "admin.iso-valve",
                "Event": "Belimo BallValve232VS 45 second opening timer",
                "FromState": "Opening",
                "ToState": "Open",
                "UnixTimeMs": 1710158046849,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
                "AboutFsmGtEnumSymbol": "0cce8d12",
                "ReportTypeGtEnumSymbol": "6fe49bc1",
                "EventTypeGtEnumSymbol": "9e44ab43",
            },
        ],
        "TypeName": "fsm.full.report",
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
    del d2["FromName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["TriggerId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["AtomicList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, AtomicList="Not a list.")
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AtomicList=["Not a list of dicts"])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AtomicList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, FromName="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TriggerId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
