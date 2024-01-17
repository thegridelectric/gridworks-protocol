"""
Tests for enum spaceheat.make.model.001 from the GridWorks Type Registry.
"""
from gwproto.enums import MakeModel


def test_make_model() -> None:
    assert set(MakeModel.values()) == set(
        [
            "UNKNOWNMAKE__UNKNOWNMODEL",
            "EGAUGE__4030",
            "NCD__PR814SPST",
            "ADAFRUIT__642",
            "GRIDWORKS__TSNAP1",
            "GRIDWORKS__WATERTEMPHIGHPRECISION",
            "GRIDWORKS__SIMPM1",
            "SCHNEIDERELECTRIC__IEM3455",
            "GRIDWORKS__SIMBOOL30AMPRELAY",
            "OPENENERGY__EMONPI",
            "GRIDWORKS__SIMTSNAP1",
            "ATLAS__EZFLO",
            "HUBITAT__C7__LAN1",
            "GRIDWORKS__TANK_MODULE_1",
            "FIBARO__ANALOG_TEMP_SENSOR",
            "AMPHENOL__NTC_10K_THERMISTOR_MA100GG103BN",
            "YHDC__SCT013100",
            "MAGNELAB__SCT0300050",
            "GRIDWORKS__MULTITEMP1",
            "KRIDA__EMR16I2CV3",
        ]
    )

    assert MakeModel.default() == MakeModel.UNKNOWNMAKE__UNKNOWNMODEL
    assert MakeModel.enum_name() == "spaceheat.make.model"
    assert MakeModel.enum_version() == "001"

    assert MakeModel.version("UNKNOWNMAKE__UNKNOWNMODEL") == "000"
    assert MakeModel.version("EGAUGE__4030") == "000"
    assert MakeModel.version("NCD__PR814SPST") == "000"
    assert MakeModel.version("ADAFRUIT__642") == "000"
    assert MakeModel.version("GRIDWORKS__TSNAP1") == "000"
    assert MakeModel.version("GRIDWORKS__WATERTEMPHIGHPRECISION") == "000"
    assert MakeModel.version("GRIDWORKS__SIMPM1") == "000"
    assert MakeModel.version("SCHNEIDERELECTRIC__IEM3455") == "000"
    assert MakeModel.version("GRIDWORKS__SIMBOOL30AMPRELAY") == "000"
    assert MakeModel.version("OPENENERGY__EMONPI") == "000"
    assert MakeModel.version("GRIDWORKS__SIMTSNAP1") == "000"
    assert MakeModel.version("ATLAS__EZFLO") == "000"
    assert MakeModel.version("HUBITAT__C7__LAN1") == "001"
    assert MakeModel.version("GRIDWORKS__TANK_MODULE_1") == "001"
    assert MakeModel.version("FIBARO__ANALOG_TEMP_SENSOR") == "001"
    assert MakeModel.version("AMPHENOL__NTC_10K_THERMISTOR_MA100GG103BN") == "001"
    assert MakeModel.version("YHDC__SCT013100") == "001"
    assert MakeModel.version("MAGNELAB__SCT0300050") == "001"
    assert MakeModel.version("GRIDWORKS__MULTITEMP1") == "001"
    assert MakeModel.version("KRIDA__EMR16I2CV3") == "001"

    for value in MakeModel.values():
        symbol = MakeModel.value_to_symbol(value)
        assert MakeModel.symbol_to_value(symbol) == value
