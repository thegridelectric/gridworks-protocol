"""Tests gt.telemetry type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
from gwproto.messages import GtTelemetry
from gwproto.messages import GtTelemetry_Maker as Maker


def test_gt_telemetry_generated():

    d = {
        "ScadaReadTimeUnixMs": 1656513094288,
        "Value": 63430,
        "Exponent": 3,
        "NameGtEnumSymbol": "c89d0ba1",
        "TypeAlias": "gt.telemetry",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gw_type = json.dumps(d)
    gw_tuple = Maker.type_to_tuple(gw_type)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple

    # test Maker init
    payload = Maker(
        scada_read_time_unix_ms=gw_tuple.ScadaReadTimeUnixMs,
        value=gw_tuple.Value,
        name=gw_tuple.Name,
        exponent=gw_tuple.Exponent,
        #
    ).tuple
    assert payload == gw_tuple

    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeAlias"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**d2)

    d2 = dict(d)
    del d2["ScadaReadTimeUnixMs"]
    with pytest.raises(ValidationError):
        GtTelemetry(**d2)

    d2 = dict(d)
    del d2["Value"]
    with pytest.raises(ValidationError):
        GtTelemetry(**d2)

    d2 = dict(d)
    del d2["NameGtEnumSymbol"]
    with pytest.raises(ValidationError):
        GtTelemetry(**d2)

    d2 = dict(d)
    del d2["Exponent"]
    with pytest.raises(ValidationError):
        GtTelemetry(**d2)

    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, ScadaReadTimeUnixMs="1656513094288.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ScadaReadTimeUnixMs="1656513094288")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, ScadaReadTimeUnixMs=1656513094288.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, Value="63430.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Value="63430")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, Value=63430.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, NameGtEnumSymbol="Unrecognized enum symbol")
    assert Maker.dict_to_tuple(d2).Name == TelemetryName.UNKNOWN

    d2 = dict(d, Exponent="3.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Exponent="3")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, Exponent=3.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeAlias="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ScadaReadTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
