"""Tests relay.actor.config type, version 000"""

import json

from gwproto.enums import RelayWiringConfig
from gwproto.named_types import RelayActorConfig


def test_relay_actor_config_generated() -> None:
    d = {
        "ChannelName": "zone1-relay-state",
        "PollPeriodMs": 300,
        "CapturePeriodS": 60,
        "AsyncCapture": True,
        "AsyncCaptureDelta": 1,
        "Exponent": 0,
        "Unit": "Unitless",
        "RelayIdx": 18,
        "ActorName": "zone1-ctrl-relay",
        "WiringConfig": "NormallyOpen",
        "EventType": "change.relay.state",
        "DeEnergizingEvent": "OpenRelay",
        "EnergizingEvent": "CloseRelay",
        "TypeName": "relay.actor.config",
        "Version": "001",
    }

    t = RelayActorConfig.model_validate(d).model_dump_json(exclude_none=True)
    d2 = json.loads(t)
    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["WiringConfig"]) is str

    d2 = dict(d, WiringConfig="unknown_enum_thing")
    assert RelayActorConfig(**d2).WiringConfig == RelayWiringConfig.default()
