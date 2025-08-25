"""Tests fsm.full.report type, version 000"""

from gwproto.named_types import FsmFullReport


def test_fsm_full_report_generated() -> None:
    d = {
        "FromName": "admin",
        "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
        "AtomicList": [
            {
                "MachineHandle": "h.admin.store-charge-discharge",
                "StateEnum": "store.flow.relay",
                "ReportType": "Event",
                "EventType": "change.store.flow.relay",
                "Event": "DischargeStore",
                "FromState": "ChargingStore",
                "ToState": "DischargingStore",
                "UnixTimeMs": 1710158001595,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
            },
            {
                "MachineHandle": "h.admin.store-charge-discharge.relay3",
                "StateEnum": "relay.closed.or.open",
                "ReportType": "Event",
                "EventType": "change.relay.state",
                "Event": "OpenRelay",
                "FromState": "RelayClosed",
                "ToState": "RelayOpen",
                "UnixTimeMs": 1710158001610,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
            },
            {
                "MachineHandle": "h.admin.store-charge-discharge.relay3",
                "StateEnum": "relay.closed.or.open",
                "ReportType": "Action",
                "ActionType": "RelayPinSet",
                "Action": 0,
                "UnixTimeMs": 1710158001624,
                "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
                "TypeName": "fsm.atomic.report",
                "Version": "000",
            },
            {
                "MachineHandle": "h.admin.store-charge-discharge",
                "StateEnum": "store.flow",
                "ReportType": "Event",
                "EventType": "timer.finished",
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

    d2 = FsmFullReport.from_dict(d).to_dict()
    assert d2 == d
