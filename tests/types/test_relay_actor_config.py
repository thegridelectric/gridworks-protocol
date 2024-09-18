"""Tests relay.actor.config type, version 000"""

from gwproto.enums import RelayWiringConfig
from gwproto.types import RelayActorConfig


def test_relay_actor_config_generated() -> None:
    d = {
        "ActorName": "relay8",
        "DeEnergizingEvent": "SwitchToBoiler",
        "EventType": "ChangeAquastatControl",
        "RelayIdx": 6,
        "TypeName": "relay.actor.config",
        "Version": "000",
        "WiringConfig": "DoubleThrow",
    }

    d2 = RelayActorConfig.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["WiringConfig"]) is str

    d2 = dict(d, WiringConfig="unknown_enum_thing")
    assert RelayActorConfig(**d2).WiringConfig == RelayWiringConfig.default()

    assert type(d2["EventType"]) is str
