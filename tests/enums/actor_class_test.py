"""
Tests for enum sh.actor.class.001 from the GridWorks Type Registry.
"""

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
        "HubitatTelemetryReader",
        "HubitatTankModule",
        "HubitatPoller",
        "Hubitat",
    }

    assert ActorClass.default() == ActorClass.NoActor
    assert ActorClass.enum_name() == "sh.actor.class"
    assert ActorClass.enum_version() == "001"

    assert ActorClass.version("NoActor") == "000"
    assert ActorClass.version("Scada") == "000"
    assert ActorClass.version("HomeAlone") == "000"
    assert ActorClass.version("BooleanActuator") == "000"
    assert ActorClass.version("PowerMeter") == "000"
    assert ActorClass.version("Atn") == "000"
    assert ActorClass.version("SimpleSensor") == "000"
    assert ActorClass.version("MultipurposeSensor") == "000"
    assert ActorClass.version("Thermostat") == "000"
    assert ActorClass.version("HubitatTelemetryReader") == "001"
    assert ActorClass.version("HubitatTankModule") == "001"
    assert ActorClass.version("HubitatPoller") == "001"

    for value in ActorClass.values():
        symbol = ActorClass.value_to_symbol(value)
        assert ActorClass.symbol_to_value(symbol) == value
