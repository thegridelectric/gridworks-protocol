"""Tests electric.meter.component.gt type, version 001"""

import json

import pytest
from pydantic import ValidationError

from gwproto.enums import MakeModel
from gwproto.enums import Unit
from gwproto.errors import SchemaError
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import ChannelConfig
from gwproto.types import ComponentAttributeClassGt as CacGt
from gwproto.types import ComponentAttributeClassGt_Maker as Cac_Maker
from gwproto.types import EgaugeIo
from gwproto.types import EgaugeRegisterConfig
from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGt
from gwproto.types.electric_meter_component_gt import (
    ElectricMeterComponentGt_Maker as Maker,
)
from tests.utils import flush_all


def test_electric_meter_component_gt_generated() -> None:
    flush_all()
    cac_gt = CacGt(
        ComponentAttributeClassId=CACS_BY_MAKE_MODEL[MakeModel.EGAUGE__4030],
        MakeModel=MakeModel.EGAUGE__4030,
        DisplayName="Egauge 4030",
    )
    Cac_Maker.tuple_to_dc(cac_gt)

    t = ElectricMeterComponentGt(
        ComponentId="04ceb282-d7e8-4293-80b5-72455e1a5db3",
        ComponentAttributeClassId=CACS_BY_MAKE_MODEL[MakeModel.EGAUGE__4030],
        DisplayName="eGauge4922.local",
        ConfigList=[
            ChannelConfig(
                ChannelName="hp-idu-pwr",
                PollPeriodMs=1000,
                CapturePeriodS=60,
                AsyncCapture=True,
                AsyncCaptureDelta=20,
                Exponent=1,
                Unit=Unit.W,
            )
        ],
        HwUid="35941_308",
        ModbusHost="eGauge4922.local",
        ModbusPort=502,
        EgaugeIoList=[
            EgaugeIo(
                ChannelName="hp-idu-pwr",
                InputConfig=EgaugeRegisterConfig(
                    Address=9000,
                    Name="",
                    Description="change in value",
                    Denominator=1,
                    Type="f32",
                    Unit=Unit.W,
                ),
            )
        ],
    )

    d = {
        "ComponentId": "04ceb282-d7e8-4293-80b5-72455e1a5db3",
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "DisplayName": "eGauge4922.local",
        "ConfigList": [
            {
                "ChannelName": "hp-idu-pwr",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 60,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 20,
                "Exponent": 1,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "f459a9c3",
            }
        ],
        "HwUid": "35941_308",
        "ModbusHost": "eGauge4922.local",
        "ModbusPort": 502,
        "EgaugeIoList": [
            {
                "ChannelName": "hp-idu-pwr",
                "InputConfig": {
                    "Address": 9000,
                    "Name": "",
                    "Description": "change in value",
                    "Type": "f32",
                    "Denominator": 1,
                    "Unit": "W",
                    "TypeName": "egauge.register.config",
                    "Version": "000",
                },
                "TypeName": "egauge.io",
                "Version": "001",
            }
        ],
        "TypeName": "electric.meter.component.gt",
        "Version": "001",
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
    del d2["ConfigList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["EgaugeIoList"]
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

    d2 = dict(d)
    del d2["ModbusHost"]
    # Axiom 1: If the EgaugeIoList has non-zero length, then the ModbusHost is not None  (type=value_error)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # Axiom 1: ModbusHost is None if and only if ModbusPort is Non
    d2 = dict(d)
    del d2["ModbusPort"]
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, ConfigList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ModbusPort="502.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EgaugeIoList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EgaugeIoList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EgaugeIoList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
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

    d2 = dict(d, ModbusPort=-1)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
    flush_all()
