"""Tests ads111x.based.cac.gt type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types.ads111x_based_cac_gt import Ads111xBasedCacGt_Maker as Maker
from gwproto.enums import TelemetryName
from gwproto.enums import MakeModel


def test_ads111x_based_cac_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "8a1a1538-ed2d-4829-9c03-f9be1c9f9c83",
        "MinPollPeriodMs": 880,
        "MakeModelGtEnumSymbol": "09185ae3",
        "AdsI2cAddressList": 12,
        "TotalTerminalBlocks": 12,
        "TelemetryNameList": ["22641963"],
        "DisplayName": "Simulated GridWorks high precision water temp sensor",
        "TypeName": "ads111x.based.cac.gt",
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
        component_attribute_class_id=gtuple.ComponentAttributeClassId,
        min_poll_period_ms=gtuple.MinPollPeriodMs,
        make_model=gtuple.MakeModel,
        ads_i2c_address_list=gtuple.AdsI2cAddressList,
        total_terminal_blocks=gtuple.TotalTerminalBlocks,
        telemetry_name_list=gtuple.TelemetryNameList,
        display_name=gtuple.DisplayName,
        
    ).tuple
    assert t == gtuple

    ######################################
    # Dataclass related tests
    ######################################

    dc = Maker.tuple_to_dc(gtuple)
    assert gtuple == Maker.dc_to_tuple(dc)
    assert Maker.type_to_dc(Maker.dc_to_type(dc)) == dc

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ComponentAttributeClassId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MinPollPeriodMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MakeModelGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TelemetryNameList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "AdsI2cAddressList" in d2.keys():
        del d2["AdsI2cAddressList"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "TotalTerminalBlocks" in d2.keys():
        del d2["TotalTerminalBlocks"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, MinPollPeriodMs="880.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, MakeModelGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).MakeModel == MakeModel.default()

    d2 = dict(d, TotalTerminalBlocks="12.1")
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

    d2 = dict(d, ComponentAttributeClassId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, MinPollPeriodMs=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TotalTerminalBlocks=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
