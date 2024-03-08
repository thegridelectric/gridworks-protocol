"""Tests electric.meter.component.gt type, version 001"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types.electric_meter_component_gt import _Maker as Maker


def test_electric_meter_component_gt_generated() -> None:
    t = ElectricMeterComponentGt(
        ComponentId="04ceb282-d7e8-4293-80b5-72455e1a5db3",
        ComponentAttributeClassId='c1856e62-d8c0-4352-b79e-6ae05a5294c2',
        DisplayName="Main power meter for Little orange house garage space heat",
        ConfigList=[{'Channel': {'DisplayName':'Idu Power', 'AboutName': 'hp-idu-pwr', 'CapturedByName': 'pwr-meter', 'TelemetryNameGtEnumSymbol': 'af39eec9'}, 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 50, 'Exponent': 0, 'UnitGtEnumSymbol': 'f459a9c3', 'TypeName': 'channel.config', 'Version': '000'}, 'TypeName': 'egauge.io', 'Version': '001'}],
        HwUid="35941_308",
        ModbusHost="eGauge4922.local",
        ModbusPort=502,
        EgaugeIoList=[{'InputConfig': {'Address': 9006, 'Name': '', 'Description': 'change in value', 'Type': 'f32', 'Denominator': 1, 'Unit': 'W', 'TypeName': 'egauge.register.config', 'Version': '000'}, 'OutputConfig': {'Channel': {'DisplayName':'Idu Power', 'AboutName': 'hp-idu-pwr', 'CapturedByName': 'pwr-meter', 'TelemetryNameGtEnumSymbol': 'af39eec9'}, 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 50, 'Exponent': 0, 'UnitGtEnumSymbol': 'f459a9c3', 'TypeName': 'channel.config', 'Version': '000'}, 'TypeName': 'egauge.io', 'Version': '001'}],)

    d = {
        "ComponentId": "04ceb282-d7e8-4293-80b5-72455e1a5db3",
        "ComponentAttributeClassId": 'c1856e62-d8c0-4352-b79e-6ae05a5294c2',
        "DisplayName": "Main power meter for Little orange house garage space heat",
        "ConfigList": [{'Channel': {'DisplayName':'Idu Power', 'AboutName': 'hp-idu-pwr', 'CapturedByName': 'pwr-meter', 'TelemetryNameGtEnumSymbol': 'af39eec9'}, 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 50, 'Exponent': 0, 'UnitGtEnumSymbol': 'f459a9c3', 'TypeName': 'channel.config', 'Version': '000'}, 'TypeName': 'egauge.io', 'Version': '001'}],
        "HwUid": "35941_308",
        "ModbusHost": "eGauge4922.local",
        "ModbusPort": 502,
        "EgaugeIoList": [{'InputConfig': {'Address': 9006, 'Name': '', 'Description': 'change in value', 'Type': 'f32', 'Denominator': 1, 'Unit': 'W', 'TypeName': 'egauge.register.config', 'Version': '000'}, 'OutputConfig': {'Channel': {'DisplayName':'Idu Power', 'AboutName': 'hp-idu-pwr', 'CapturedByName': 'pwr-meter', 'TelemetryNameGtEnumSymbol': 'af39eec9'}, 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 50, 'Exponent': 0, 'UnitGtEnumSymbol': 'f459a9c3', 'TypeName': 'channel.config', 'Version': '000'}, 'TypeName': 'egauge.io', 'Version': '001'}],
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

    # test Maker init
    t = Maker(
        component_id=gtuple.ComponentId,
        component_attribute_class_id=gtuple.ComponentAttributeClassId,
        display_name=gtuple.DisplayName,
        config_list=gtuple.ConfigList,
        hw_uid=gtuple.HwUid,
        modbus_host=gtuple.ModbusHost,
        modbus_port=gtuple.ModbusPort,
        egauge_io_list=gtuple.EgaugeIoList,
        
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
    if "ModbusHost" in d2.keys():
        del d2["ModbusHost"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "ModbusPort" in d2.keys():
        del d2["ModbusPort"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2  = dict(d, ConfigList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, ConfigList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, ConfigList= [{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ModbusPort="502.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, EgaugeIoList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, EgaugeIoList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, EgaugeIoList= [{"Failed": "Not a GtSimpleSingleStatus"}])
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
