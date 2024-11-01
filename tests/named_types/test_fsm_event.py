"""Tests fsm.event type, version 000"""

from gwproto.enums import FsmEventType
from gwproto.named_types import FsmEvent


def test_fsm_event_generated() -> None:
    d = {
        "FromHandle": "h.s.admin",
        "ToHandle": "h.s.admin.iso-valve",
        "EventType": "ChangeValveState",
        "EventName": "OpenValve",
        "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
        "SendTimeUnixMs": 1709923791330,
        "TypeName": "fsm.event",
        "Version": "000",
    }

    d2 = FsmEvent.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["EventType"]) is str

    d2 = dict(d, EventType="unknown_enum_thing")
    assert FsmEvent(**d2).EventType == FsmEventType.default()
