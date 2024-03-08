"""Tests thermistor.data.processing.config type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.enums import MakeModel
from gwproto.enums import ThermistorDataMethod
from gwproto.errors import SchemaError
from gwproto.types import ThermistorDataProcessingConfig
from gwproto.types import ThermistorDataProcessingConfig_Maker as Maker


def test_thermistor_data_processing_config_generated() -> None:
    t = ThermistorDataProcessingConfig(
        ChannelName="hp-ewt",
        TerminalBlockIdx=4,
        ThermistorMakeModel="652abfd6",
        DataProcessingMethod="00000000",
        DataProcessingDescription="using a beta of 3977.",
    )

    d = {
        "ChannelName": "hp-ewt",
        "TerminalBlockIdx": 4,
        "ThermistorMakeModelGtEnumSymbol": "652abfd6",
        "DataProcessingMethodGtEnumSymbol": "00000000",
        "DataProcessingDescription": "using a beta of 3977.",
        "TypeName": "thermistor.data.processing.config",
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

    d2 = dict(d, ChannelName="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TerminalBlockIdx=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
