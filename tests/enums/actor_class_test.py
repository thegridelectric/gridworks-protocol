"""Tests for schema enum sh.actor.class.000"""
from gwproto.enums import ActorClass


def test_actor_class() -> None:
    assert set(ActorClass.values()) == {
        "NoActor",
        "Scada",
        "HomeAlone",
        "BooleanActuator",
        "PowerMeter",
        "Atn",
        "SimpleSensor",
        "MultipurposeSensor",
        "Thermostat",
        "HubitatTankModule",
        "HubitatTelemetryReader",
        "HubitatPoller",
    }

    assert ActorClass.default() == ActorClass.NoActor
