"""Tests thermistor.data.processing.config type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import ThermistorDataProcessingConfig_Maker as Maker
from gwproto.enums import ThermistorDataMethod


def test_thermistor_data_processing_config_generated() -> None:
    d = {
        "ChannelName": 'hp-ewt',
        "TerminalBlockIdx": 4,
        "ThermistorMakeModelGtEnumSymbol": '46f21cd5',
        "DataProcessingMethodGtEnumSymbol": '00000000',
        "DataProcessingDescription": 'using a beta of SPLAT.',
        "TypeName": "thermistor.data.processing.config",
        "Version": "000",
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
        terminal_block_idx=gtuple.TerminalBlockIdx,
        thermistor_make_model=gtuple.ThermistorMakeModel,
        data_processing_method=gtuple.DataProcessingMethod,
        data_processing_description=gtuple.DataProcessingDescription,
        
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
    del d2["TerminalBlockIdx"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ThermistorMakeModelGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "DataProcessingMethod" in d2.keys():
        del d2["DataProcessingMethodGtEnumSymbol"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "DataProcessingMethod" in d2.keys():
        del d2["DataProcessingMethod"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "DataProcessingDescription" in d2.keys():
        del d2["DataProcessingDescription"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TerminalBlockIdx="4.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ThermistorMakeModelGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).ThermistorMakeModel == MakeModel.default()

    d2 = dict(d, DataProcessingMethodGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).DataProcessingMethod == ThermistorDataMethod.default()

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, TerminalBlockIdx=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
