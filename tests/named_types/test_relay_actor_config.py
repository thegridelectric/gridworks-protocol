"""Tests relay.actor.config type, version 000"""

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
        "StateType": "relay.open.or.closed",
        "DeEnergizingEvent": "OpenRelay",
        "EnergizingEvent": "CloseRelay",
        "DeEnergizedState": "RelayOpen",
        "EnergizedState": "RelayClosed",
        "TypeName": "relay.actor.config",
        "Version": "002",
    }

    d2 = RelayActorConfig.from_dict(d).to_dict()
    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["WiringConfig"]) is str

    d2 = dict(d, WiringConfig="unknown_enum_thing")
    assert RelayActorConfig.from_dict(d2).wiring_config == RelayWiringConfig.default()
