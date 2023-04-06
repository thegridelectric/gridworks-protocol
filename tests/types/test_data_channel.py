"""Tests data.channel type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.enums import TelemetryName
from gwproto.errors import MpSchemaError
from gwproto.types import DataChannel_Maker as Maker


def test_data_channel_generated() -> None:
    d = {
        "DisplayName": "BoostPower",
        "AboutName": "a.elt1",
        "FromName": "a.m",
        "TelemetryNameGtEnumSymbol": "af39eec9",
        "ExpectedMaxValue": 3000,
        "ExpectedMinValue": 0,
        "TypeName": "data.channel",
        "Version": "000",
    }

    with pytest.raises(MpSchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(MpSchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # test Maker init
    t = Maker(
        display_name=gtuple.DisplayName,
        about_name=gtuple.AboutName,
        from_name=gtuple.FromName,
        telemetry_name=gtuple.TelemetryName,
        expected_max_value=gtuple.ExpectedMaxValue,
        expected_min_value=gtuple.ExpectedMinValue,
    ).tuple
    assert t == gtuple

    ######################################
    # MpSchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["DisplayName"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AboutName"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FromName"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TelemetryNameGtEnumSymbol"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "ExpectedMaxValue" in d2.keys():
        del d2["ExpectedMaxValue"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "ExpectedMinValue" in d2.keys():
        del d2["ExpectedMinValue"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TelemetryNameGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).TelemetryName = TelemetryName.default()

    d2 = dict(d, ExpectedMaxValue=".1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ExpectedMinValue=".1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # MpSchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # MpSchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, AboutName="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromName="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
