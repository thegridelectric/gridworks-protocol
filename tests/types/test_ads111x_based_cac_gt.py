"""Tests ads111x.based.cac.gt type, version 000"""
import json
import uuid

import pytest
from pydantic import ValidationError

from gwproto.enums import MakeModel
from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
from gwproto.types import Ads111xBasedCacGt
from gwproto.types import Ads111xBasedCacGt_Maker as Maker


def test_ads111x_based_cac_gt_generated() -> None:
    t = Ads111xBasedCacGt(
        ComponentAttributeClassId="432073b8-4d2b-4e36-9229-73893f33f846",
        MinPollPeriodMs=200,
        MakeModel=MakeModel.GRIDWORKS__MULTITEMP1,
        AdsI2cAddressList=["0x4b", "0x48", "0x49"],
        TotalTerminalBlocks=12,
        TelemetryNameList=[
            TelemetryName.WaterTempCTimes1000,
            TelemetryName.AirTempCTimes1000,
        ],
        DisplayName="Gridworks 12-channel MultiTemp Ads Sensor",
    )

    d = {
        "ComponentAttributeClassId": "432073b8-4d2b-4e36-9229-73893f33f846",
        "MinPollPeriodMs": 200,
        "MakeModelGtEnumSymbol": "bb31d136",
        "AdsI2cAddressList": ["0x4b", "0x48", "0x49"],
        "TotalTerminalBlocks": 12,
        "TelemetryNameList": ["c89d0ba1", "0f627faa"],
        "DisplayName": "Gridworks 12-channel MultiTemp Ads Sensor",
        "TypeName": "ads111x.based.cac.gt",
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
    del d2["AdsI2cAddressList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TotalTerminalBlocks"]
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
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, MinPollPeriodMs="200.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, MakeModelGtEnumSymbol="unknown_symbol")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(
        d, MakeModelGtEnumSymbol="00000000", ComponentAttributeClassId=str(uuid.uuid4())
    )
    assert Maker.dict_to_tuple(d2).MakeModel == MakeModel.UNKNOWNMAKE__UNKNOWNMODEL

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
