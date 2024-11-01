"""Tests fsm.full.report type, version 000"""

from gwproto.named_types import FsmFullReport


def test_fsm_full_report_generated() -> None:
    d = {
        "FromName": "admin",
        "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
        "AtomicList": [
            {
                "FromHandle": "h.admin.store-charge-discharge",
                "AboutFsm": "StoreFlowDirection",
                "ReportType": "Event",
                "EventType": "ChangeStoreFlowDirection",
                "Event": "Discharge",
                "FromState": "ValvedtoChargeStore",
                "ToState": "ValvesMovingToDischarging",
                "UnixTimeMs": 1710158001595,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
            },
            {
                "FromHandle": "h.admin.store-charge-discharge.relay3",
                "AboutFsm": "RelayState",
                "ReportType": "Event",
                "EventType": "ChangeRelayState",
                "Event": "OpenRelay",
                "FromState": "RelayClosed",
                "ToState": "RelayOpen",
                "UnixTimeMs": 1710158001610,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
            },
            {
                "FromHandle": "h.admin.store-charge-discharge.relay3",
                "AboutFsm": "RelayState",
                "ReportType": "Action",
                "ActionType": "RelayPinSet",
                "Action": 0,
                "UnixTimeMs": 1710158001624,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
            },
            {
                "FromHandle": "h.admin.store-charge-discharge",
                "AboutFsm": "StoreFlowDirection",
                "ReportType": "Event",
                "EventType": "TimerFinished",
                "Event": "Belimo BallValve232VS 45 second opening timer",
                "FromState": "ValvesMovingToDischarging",
                "ToState": "ValvedtoDischargeStore",
                "UnixTimeMs": 1710158046849,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
            },
        ],
        "TypeName": "fsm.full.report",
        "Version": "000",
    }

    d2 = FsmFullReport.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
