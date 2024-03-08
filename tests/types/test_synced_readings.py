"""Tests synced.readings type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import SyncedReadings
from gwproto.types import SyncedReadings_Maker as Maker
from gwproto.enums import TelemetryName


def test_synced_readings_generated() -> None:
    t = SyncedReadings(
        ScadaReadTimeUnixMs=1656587343297,
        ChannelNameList=,
        ValueList=[18000],)

    d = {
        "ScadaReadTimeUnixMs": 1656587343297,
        "ChannelNameList": ,
        "ValueList": [18000],
        "TypeName": "synced.readings",
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

    # test Maker init
    t = Maker(
        scada_read_time_unix_ms=gtuple.ScadaReadTimeUnixMs,
        channel_name_list=gtuple.ChannelNameList,
        value_list=gtuple.ValueList,
        
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
    del d2["ChannelNameList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ValueList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, ScadaReadTimeUnixMs="1656587343297.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ScadaReadTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ChannelNameList=["A.hot-stuff"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
