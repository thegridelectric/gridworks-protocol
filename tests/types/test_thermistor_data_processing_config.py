"""Tests thermistor.data.processing.config type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import ThermistorDataProcessingConfig_Maker as Maker
from gwproto.enums import 


def test_thermistor_data_processing_config_generated() -> None:
    d = {
        "TerminalBlockIdx": ,
        "ReportingConfig": ,
        "DataProcessingMethodGtEnumSymbol": ,
        "DataProcessingDescription": ,
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
        terminal_block_idx=gtuple.TerminalBlockIdx,
        reporting_config=gtuple.ReportingConfig,
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
    del d2["TerminalBlockIdx"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ReportingConfig"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

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

    d2 = dict(d, TerminalBlockIdx=".1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, DataProcessingMethodGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).DataProcessingMethod == .default()

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
