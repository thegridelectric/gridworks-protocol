"""Tests heartbeat.b type, version 001"""

from gwproto.named_types import HeartbeatB


def test_heartbeat_b_generated() -> None:
    d = {
        "FromGNodeAlias": "d1.isone.ver.keene.holly",
        "FromGNodeInstanceId": "97eba574-bd20-45b5-bf82-9ba2f492d8f6",
        "MyHex": "a",
        "YourLastHex": "2",
        "LastReceivedTimeUnixMs": 1673635764282,
        "SendTimeUnixMs": 1673635765317,
        "StartingOver": False,
        "TypeName": "heartbeat.b",
        "Version": "001",
    }
    assert HeartbeatB.model_validate(d).model_dump() == d
