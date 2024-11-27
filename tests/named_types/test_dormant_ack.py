"""Tests dormant.ack type, version 000"""

from gwproto.named_types import DormantAck


def test_dormant_ack_generated() -> None:
    d = {
        "FromName": "pico-cycler",
        "ToName": "auto",
        "TriggerId": "dc6c6689-e1b1-4e60-adf9-94db59c7f96a",
        "TypeName": "dormant.ack",
        "Version": "000",
    }

    d2 = DormantAck.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
