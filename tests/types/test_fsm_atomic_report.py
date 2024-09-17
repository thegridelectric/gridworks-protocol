"""Tests fsm.atomic.report type, version 000"""

from gwproto.enums import FsmReportType
from gwproto.enums import FsmActionType
from gwproto.enums import FsmEventType
from gwproto.enums import FsmName
from gwproto.types import FsmAtomicReport


def test_fsm_atomic_report_generated() -> None:
    d = {
        "FromHandle": "h.s.admin.iso-valve.relay",
        "AboutFsm": "IsoValve",
        "ReportType": "Action",
        "ActionType": "RelayPinSet",
        "Action": 0,
        "EventType": "",
        "Event": ,
        "FromState": ,
        "ToState": ,
        "UnixTimeMs": 1709923792000,
        "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
        "TypeName": "fsm.atomic.report",
        "Version": "000",
    }

    t = FsmAtomicReport(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, AboutFsm="unknown_enum_thing")
    assert FsmAtomicReport(**d2).about_fsm == FsmName.default()

    d2 = dict(d, ReportType="unknown_enum_thing")
    assert FsmAtomicReport(**d2).report_type == FsmReportType.default()

    d2 = dict(d, ActionType="unknown_enum_thing")
    assert FsmAtomicReport(**d2).action_type == FsmActionType.default()

    d2 = dict(d, EventType="unknown_enum_thing")
    assert FsmAtomicReport(**d2).event_type == FsmEventType.default()
