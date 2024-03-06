"""Tests egauge.io type, version 001"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import EgaugeIo_Maker as Maker


def test_egauge_io_generated() -> None:
    d = {
        "ChannelName": 'hp-idu-pwr',
        "InputConfig": {'Address': 9004, 'Name': 'Garage power', 'Description': '', 'Type': 'f32', 'Denominator': 1, 'Unit': 'W', 'TypeName': 'egauge.register.config', 'Version': '000'},
        "TypeName": "egauge.io",
        "Version": "001",
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
        channel_name=gtuple.ChannelName,
        input_config=gtuple.InputConfig,
        
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
    del d2["ChannelName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["InputConfig"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ChannelName="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
