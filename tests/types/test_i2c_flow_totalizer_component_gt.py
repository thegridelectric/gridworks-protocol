"""Tests i2c.flow.totalizer.component.gt type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import MakeModel, Unit
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import ChannelConfig
from gwproto.types import ComponentAttributeClassGt as CacGt
from gwproto.types import ComponentAttributeClassGtMaker as CacMaker
from gwproto.types.i2c_flow_totalizer_component_gt import I2cFlowTotalizerComponentGt
from gwproto.types.i2c_flow_totalizer_component_gt import (
    I2cFlowTotalizerComponentGtMaker as Maker,
)
from pydantic import ValidationError

from tests.utils import flush_all


def test_i2c_flow_totalizer_component_gt_generated() -> None:
    flush_all()
    cac_gt = CacGt(
        component_attribute_class_id=CACS_BY_MAKE_MODEL[MakeModel.ATLAS__EZFLO],
        make_model=MakeModel.ATLAS__EZFLO,
        DisplayName="Atlas EZ FLO",
    )
    CacMaker.tuple_to_dc(cac_gt)
    t = I2cFlowTotalizerComponentGt(
        component_id="dd5ac673-91a8-40e2-a233-b67479cec709",
        component_attribute_class_id="13d916dc-8764-4b16-b85d-b8ead3e2fc80",
        i2c_address_list=[100],
        config_list=[
            ChannelConfig(
                channel_name="dist-volume",
                poll_period_ms=300,
                capture_period_s=30,
                async_capture=True,
                async_capture_delta=5,
                exponent=2,
                unit=Unit.Gallons,
            ),
            ChannelConfig(
                channel_name="dist-flow",
                poll_period_ms=300,
                capture_period_s=30,
                async_capture=True,
                async_capture_delta=20,
                exponent=2,
                unit=Unit.Gpm,
            ),
        ],
        pulse_flow_meter_make_model_list=[MakeModel.EKM__HOTSPWM075HD],
        conversion_factor_list=[0.08322],
        display_name="Flow meter on pipe out of tank",
        hw_uid="1234",
    )

    d = {
        "ComponentId": "dd5ac673-91a8-40e2-a233-b67479cec709",
        "ComponentAttributeClassId": "13d916dc-8764-4b16-b85d-b8ead3e2fc80",
        "I2cAddressList": [100],
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
        "ConversionFactorList": [0.08322],
        "DisplayName": "Flow meter on pipe out of tank",
        "HwUid": "1234",
        "TypeName": "i2c.flow.totalizer.component.gt",
        "Version": "000",
        "PulseFlowMeterMakeModelList": ["208f827f"],
    }

    assert t.as_dict() == d

    d2 = d.copy()

    d2["PulseFlowMeterMakeModelList"] = [MakeModel.EKM__HOTSPWM075HD.value]
    assert t == Maker.dict_to_tuple(d2)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple(d)

    with pytest.raises(GwTypeError):
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
    # GwTypeError raised if missing a required attribute
    ######################################

    d2 = d.copy()
    del d2["TypeName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ComponentId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ComponentAttributeClassId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["I2cAddressList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ConfigList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["PulseFlowMeterMakeModelList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ConversionFactorList"]
    with pytest.raises(GwTypeError):
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

    d2 = dict(d, ConfigList="Not a list.")
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=["Not a list of dicts"])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ComponentId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
