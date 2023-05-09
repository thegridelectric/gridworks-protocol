"""Tests gt.telemetry type, version 110"""
import json

import pytest
from pydantic import ValidationError

from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
from gwproto.types import GtTelemetry_Maker as Maker


def test_gt_telemetry_generated() -> None:
    d = {
        "ScadaReadTimeUnixMs": 1656513094288,
        "Value": 63430,
        "NameGtEnumSymbol": "c89d0ba1",
        "Exponent": 3,
        "TypeName": "gt.telemetry",
        "Version": "110",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # test Maker init
    t = Maker(
        scada_read_time_unix_ms=gtuple.ScadaReadTimeUnixMs,
        value=gtuple.Value,
        name=gtuple.Name,
        exponent=gtuple.Exponent,
    ).tuple
    assert t == gtuple

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ScadaReadTimeUnixMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Value"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["NameGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Exponent"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, ScadaReadTimeUnixMs="1656513094288.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Value="63430.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, NameGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).Name = TelemetryName.default()

    d2 = dict(d, Exponent="3.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ScadaReadTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
