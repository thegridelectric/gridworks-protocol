"""Tests fsm.trigger.from.atn type, version 000"""

from gwproto.types import FsmTriggerFromAtn


def test_fsm_trigger_from_atn_generated() -> None:
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

    t = FsmTriggerFromAtn(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
