"""Tests fsm.full.report type, version 000"""

from gwproto.types import FsmFullReport


def test_fsm_full_report_generated() -> None:
    d = {
        "FromName": "admin",
        "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
        "AtomicList": ,
        "TypeName": "fsm.full.report",
        "Version": "000",
    }

    t = FsmFullReport(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
