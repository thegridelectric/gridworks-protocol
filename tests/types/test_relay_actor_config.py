"""Tests relay.actor.config type, version 000"""

import json

import pytest
from pydantic import ValidationError

from gwproto.enums import FsmEventType
from gwproto.enums import RelayWiringConfig
from gwproto.errors import SchemaError
from gwproto.types import RelayActorConfig
from gwproto.types import RelayActorConfig_Maker as Maker


def test_relay_actor_config_generated() -> None:
    t = RelayActorConfig(
        RelayIdx=18,
        ActorName="s.zone1-ctrl-relay",
        WiringConfig=RelayWiringConfig.NormallyOpen,
        EventType=FsmEventType.ChangeRelayState,
        DeEnergizingEvent="OpenRelay",
    )

    d = {
        "RelayIdx": 18,
        "ActorName": "s.zone1-ctrl-relay",
        "WiringConfigGtEnumSymbol": "63f5da41",
        "EventTypeGtEnumSymbol": "00000000",
        "DeEnergizingEvent": "OpenRelay",
        "TypeName": "relay.actor.config",
        "Version": "000",
    }

    assert t.as_dict() == d

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)
    assert gtuple == t

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RelayIdx"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ActorName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["WiringConfigGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["EventTypeGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["DeEnergizingEvent"]
    with pytest.raises(SchemaError):
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
    Maker.dict_to_tuple(d2).WiringConfig == RelayWiringConfig.NormallyClosed

    d2 = dict(d, EventTypeGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).EventType == FsmEventType.default()

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, RelayIdx=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ActorName="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # TODO: test Axiom 1
    ######################################
    """
    Axiom 1: EventType, DeEnergizingEvent consistency.
    a) The EventType must belong to one of the boolean choices for FsmEventType (for example,
    it is NOT SetAnalog010V):
        ChangeRelayState
        ChangeValveState
        ChangeStoreFlowDirection
        ChangeHeatcallSource
        ChangeAquastatControl
        ChangeHeatPumpControl
        ChangeLgOperatingMode

    b) The DeEnergizingEvent string must be one of the two choices for the EventType as an enum.
    For example, if the EventType is ChangeValveState then the  DeEnergizingEvent  must either
    be OpenValve or CloseValve.

    c) If the EventType is ChangeRelayState, then
        i) the WiringConfig cannot be DoubleThrow;
        ii) if the Wiring Config is NormallyOpen then the DeEnergizingEvent must be OpenRelay; and
        iii) if the WiringConfig is NormallyClosed then the DeEnergizingEvent must be CloseRelay.
    """

    # 1.c.ii: WiringConfig defaults to NormallyClosed, which is not consistent with DeEnergizingEvent OpenRelay:
    d2 = dict(d, WiringConfigGtEnumSymbol="unknown_symbol")
    with pytest.raises(ValueError):
        Maker.dict_to_tuple(d2)