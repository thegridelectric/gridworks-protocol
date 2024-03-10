"""Tests i2c.flow.totalizer.component.gt type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.enums import MakeModel
from gwproto.enums import Unit
from gwproto.errors import SchemaError
from gwproto.types import ChannelConfig
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import ComponentAttributeClassGt as CacGt, ComponentAttributeClassGt_Maker as Cac_Maker
from gwproto.types.i2c_flow_totalizer_component_gt import I2cFlowTotalizerComponentGt
from gwproto.types.i2c_flow_totalizer_component_gt import (
    I2cFlowTotalizerComponentGt_Maker as Maker,
)
from tests.utils import flush_all

def test_i2c_flow_totalizer_component_gt_generated() -> None:
    flush_all()
    cac_gt = CacGt(ComponentAttributeClassId=CACS_BY_MAKE_MODEL[MakeModel.ATLAS__EZFLO],
                   MakeModel=MakeModel.ATLAS__EZFLO,
                   DisplayName="Atlas EZ Flo Totalizer")
    Cac_Maker.tuple_to_dc(cac_gt)

    t = I2cFlowTotalizerComponentGt(
        ComponentId="dd5ac673-91a8-40e2-a233-b67479cec709",
        ComponentAttributeClassId="13d916dc-8764-4b16-b85d-b8ead3e2fc80",
        I2cAddress=100,
        ConfigList=[
            ChannelConfig(
                ChannelName="dist-volume",
                PollPeriodMs=300,
                CapturePeriodS=30,
                AsyncCapture=True,
                AsyncCaptureDelta=5,
                Exponent=2,
                Unit=Unit.Gallons,
            ),
            ChannelConfig(
                ChannelName="dist-flow",
                PollPeriodMs=300,
                CapturePeriodS=30,
                AsyncCapture=True,
                AsyncCaptureDelta=20,
                Exponent=2,
                Unit=Unit.Gpm,
            ),
        ],
        PulseFlowMeterMakeModel=MakeModel.EKM__HOTSPWM075HD,
        ConversionFactor=0.1,
        DisplayName="Dist EZ FLow (i2c 0x64, or 100)",
    )
    d = {
        "ComponentId": "dd5ac673-91a8-40e2-a233-b67479cec709",
        "ComponentAttributeClassId": "13d916dc-8764-4b16-b85d-b8ead3e2fc80",
        "I2cAddress": 100,
        "ConfigList": [
            {
                "ChannelName": "dist-volume",
                "PollPeriodMs": 300,
                "CapturePeriodS": 30,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 5,
                "Exponent": 2,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "8e123a26",
            },
            {
                "ChannelName": "dist-flow",
                "PollPeriodMs": 300,
                "CapturePeriodS": 30,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 20,
                "Exponent": 2,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "b4580361",
            },
        ],
        "ConversionFactor": 0.1,
        "DisplayName": "Dist EZ FLow (i2c 0x64, or 100)",
        "TypeName": "i2c.flow.totalizer.component.gt",
        "Version": "000",
        "PulseFlowMeterMakeModelGtEnumSymbol": "208f827f",
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
    del d2["ComponentId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ComponentAttributeClassId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["I2cAddress"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ConfigList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["PulseFlowMeterMakeModelGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ConversionFactor"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "HwUid" in d2.keys():
        del d2["HwUid"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, I2cAddress="100.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, PulseFlowMeterMakeModelGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).PulseFlowMeterMakeModel == MakeModel.default()

    d2 = dict(d, ConversionFactor="this is not a float")
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

    d2 = dict(d, ComponentId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Axiom 1: PulseFlowMeterMakeModel, ConversionFactor Consistency
    ######################################
    d2 = dict(d, ConversionFactor=3)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
    flush_all()