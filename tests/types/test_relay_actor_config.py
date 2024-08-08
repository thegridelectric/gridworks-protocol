"""Tests relay.actor.config type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import FsmEventType, RelayWiringConfig
from gwproto.types import RelayActorConfig
from gwproto.types import RelayActorConfigMaker as Maker
from pydantic import ValidationError


def test_relay_actor_config_generated() -> None:
    t = RelayActorConfig(
        relay_idx=18,
        actor_name="zone1-ctrl-relay",
        wiring_config=RelayWiringConfig.NormallyOpen,
        event_type=FsmEventType.ChangeRelayState,
        de_energizing_event="OpenRelay",
    )

    d = {
        "RelayIdx": 18,
        "ActorName": "zone1-ctrl-relay",
        "WiringConfigGtEnumSymbol": "63f5da41",
        "EventTypeGtEnumSymbol": "00000000",
        "DeEnergizingEvent": "OpenRelay",
        "TypeName": "relay.actor.config",
        "Version": "000",
    }

    assert t.as_dict() == d

    d2 = d.copy()

    del d2["WiringConfigGtEnumSymbol"]
    d2["WiringConfig"] = RelayWiringConfig.NormallyOpen.value
    del d2["EventTypeGtEnumSymbol"]
    d2["EventType"] = FsmEventType.ChangeRelayState.value
    assert t == Maker.dict_to_tuple(d2)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple(d)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)
    assert gtuple == t

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # Axiom testing
    d2 = d.copy()
    d2["DeEnergizingEvent"] = "CloseRelay"
    # Axiom 1: if EventType is ChangeRelayState and Wiring Config is NormallyOpen then the DeEnergizingEvent must be OpenRelay
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # GwTypeError raised if missing a required attribute
    ######################################

    d2 = d.copy()
    del d2["TypeName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["RelayIdx"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ActorName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["WiringConfigGtEnumSymbol"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["EventTypeGtEnumSymbol"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["DeEnergizingEvent"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, RelayIdx="18.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(
        d, WiringConfigGtEnumSymbol="unknown_symbol", DeEnergizingEvent="CloseRelay"
    )
    assert Maker.dict_to_tuple(d2).wiring_config == RelayWiringConfig.default()

    d2 = dict(d, EventTypeGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).event_type == FsmEventType.default()

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, RelayIdx=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ActorName="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
