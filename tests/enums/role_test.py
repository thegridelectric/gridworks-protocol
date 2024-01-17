"""
Tests for enum sh.node.role.000 from the GridWorks Type Registry.
"""
from gwproto.enums import Role


def test_role() -> None:
    assert set(Role.values()) == set(
        [
            "Unknown",
            "Scada",
            "HomeAlone",
            "Atn",
            "PowerMeter",
            "BoostElement",
            "BooleanActuator",
            "DedicatedThermalStore",
            "TankWaterTempSensor",
            "PipeTempSensor",
            "RoomTempSensor",
            "OutdoorTempSensor",
            "PipeFlowMeter",
            "HeatedSpace",
            "HydronicPipe",
            "BaseboardRadiator",
            "RadiatorFan",
            "CirculatorPump",
            "MultiChannelAnalogTempSensor",
            "Outdoors",
        ]
    )

    assert Role.default() == Role.Unknown
    assert Role.enum_name() == "sh.node.role"
    assert Role.enum_version() == "000"

    assert Role.version("Unknown") == "000"
    assert Role.version("Scada") == "000"
    assert Role.version("HomeAlone") == "000"
    assert Role.version("Atn") == "000"
    assert Role.version("PowerMeter") == "000"
    assert Role.version("BoostElement") == "000"
    assert Role.version("BooleanActuator") == "000"
    assert Role.version("DedicatedThermalStore") == "000"
    assert Role.version("TankWaterTempSensor") == "000"
    assert Role.version("PipeTempSensor") == "000"
    assert Role.version("RoomTempSensor") == "000"
    assert Role.version("OutdoorTempSensor") == "000"
    assert Role.version("PipeFlowMeter") == "000"
    assert Role.version("HeatedSpace") == "000"
    assert Role.version("HydronicPipe") == "000"
    assert Role.version("BaseboardRadiator") == "000"
    assert Role.version("RadiatorFan") == "000"
    assert Role.version("CirculatorPump") == "000"
    assert Role.version("MultiChannelAnalogTempSensor") == "000"
    assert Role.version("Outdoors") == "000"

    for value in Role.values():
        symbol = Role.value_to_symbol(value)
        assert Role.symbol_to_value(symbol) == value
