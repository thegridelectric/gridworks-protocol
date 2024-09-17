"""Tests relay.actor.config type, version 000"""

from gwproto.enums import FsmEventType, RelayWiringConfig
from gwproto.types import RelayActorConfig


def test_relay_actor_config_generated() -> None:
    d = {
        "RelayIdx": 18,
        "ActorName": "zone1-ctrl-relay",
        "WiringConfig": "NormallyOpen",
        "EventType": "ChangeRelayState",
        "DeEnergizingEvent": "OpenRelay",
        "TypeName": "relay.actor.config",
        "Version": "000",
    }

    t = RelayActorConfig(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, WiringConfig="unknown_enum_thing")
    assert RelayActorConfig(**d2).wiring_config == RelayWiringConfig.default()

    d2 = dict(d, EventType="unknown_enum_thing")
    assert RelayActorConfig(**d2).event_type == FsmEventType.default()
