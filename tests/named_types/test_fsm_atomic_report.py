"""Tests fsm.atomic.report type, version 000"""

import json

from gwproto.enums import FsmReportType
from gwproto.named_types import FsmAtomicReport


def test_fsm_atomic_report_generated() -> None:
    d = {
        "MachineHandle": "h.pico-cycler.relay1",
        "StateEnum": "relay.closed.or.open",
        "ReportType": "Event",
        "EventEnum": "change.relay.state",
        "Event": "CloseRelay",
        "FromState": "RelayOpen",
        "ToState": "RelayClosed",
        "UnixTimeMs": 1709923792000,
        "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
        "TypeName": "fsm.atomic.report",
        "Version": "000",
    }

    t = FsmAtomicReport.model_validate(d).model_dump_json(exclude_none=True)
    d2 = json.loads(t)
    assert d == d2

    ######################################
    # Enum related
    ######################################

    assert type(d2["ReportType"]) is str

    d2 = dict(d, ReportType="unknown_enum_thing")
    assert FsmAtomicReport(**d2).ReportType == FsmReportType.default()
