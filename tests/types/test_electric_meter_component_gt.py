"""Tests electric.meter.component.gt type, version 001"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import MakeModel, Unit
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import ChannelConfig, EgaugeIo, EgaugeRegisterConfig
from gwproto.types import ComponentAttributeClassGt as CacGt
from gwproto.types import ComponentAttributeClassGtMaker as CacMaker
from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGt
from gwproto.types.electric_meter_component_gt import (
    ElectricMeterComponentGtMaker as Maker,
)
from pydantic import ValidationError

from tests.utils import flush_all


def test_electric_meter_component_gt_generated() -> None:
    flush_all()
    cac_gt = CacGt(
        component_attribute_class_id=CACS_BY_MAKE_MODEL[MakeModel.EGAUGE__4030],
        make_model=MakeModel.EGAUGE__4030,
        display_name="Egauge 4030",
    )
    CacMaker.tuple_to_dc(cac_gt)
    t = ElectricMeterComponentGt(
        component_id="04ceb282-d7e8-4293-80b5-72455e1a5db3",
        component_attribute_class_id="739a6e32-bb9c-43bc-a28d-fb61be665522",
        display_name="Main power meter for Little orange house garage space heat",
        config_list=[
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
        hw_uid="35941_308",
        modbus_host="eGauge4922.local",
        modbus_port=502,
        egauge_io_list=[
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
        "DisplayName": "Main power meter for Little orange house garage space heat",
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
    del d2["ConfigList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["EgaugeIoList"]
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

    d2 = d.copy()
    if "ModbusHost" in d2.keys():
        del d2["ModbusHost"]
        del d2["ModbusPort"]
        d2["EgaugeIoList"] = []
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

    d2 = dict(d, ModbusPort="502.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EgaugeIoList="Not a list.")
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EgaugeIoList=["Not a list of dicts"])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, EgaugeIoList=[{"Failed": "Not a GtSimpleSingleStatus"}])
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

    d2 = dict(d, ModbusPort=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
