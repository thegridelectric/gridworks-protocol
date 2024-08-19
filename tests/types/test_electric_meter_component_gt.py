"""Tests electric.meter.component.gt type, version 000"""

import json

import pytest
from gwproto.errors import SchemaError
from gwproto.types.electric_meter_component_gt import (
    ElectricMeterComponentGt_Maker as Maker,
)
from pydantic import ValidationError


def test_electric_meter_component_gt_generated() -> None:
    d = {
        "ComponentId": "2dfb0cb6-6015-4273-b02b-bd446cc785d7",
        "ComponentAttributeClassId": "204832ef-0c88-408b-9640-264d2ee74914",
        "DisplayName": "EGauge Power Meter",
        "ConfigList": [
            {
                "AboutNodeName": "a.m.hp.outdoor.power",
                "ReportOnChange": True,
                "SamplePeriodS": 300,
                "Exponent": 0,
                "AsyncReportThreshold": 0.02,
                "NameplateMaxValue": 3500,
                "TypeName": "telemetry.reporting.config",
                "Version": "000",
                "TelemetryNameGtEnumSymbol": "af39eec9",
                "UnitGtEnumSymbol": "f459a9c3",
            }
        ],
        "HwUid": "BP01349",
        "ModbusHost": "eGauge6069.local",
        "ModbusPort": 502,
        "EgaugeIoList": [
            {
                "InputConfig": {
                    "Address": 9006,
                    "Name": "",
                    "Description": "change in value",
                    "Type": "f32",
                    "Denominator": 1,
                    "Unit": "W",
                    "TypeName": "egauge.register.config",
                    "Version": "000",
                },
                "OutputConfig": {
                    "AboutNodeName": "a.m.hp.outdoor.power",
                    "ReportOnChange": True,
                    "SamplePeriodS": 300,
                    "Exponent": 0,
                    "AsyncReportThreshold": 0.02,
                    "NameplateMaxValue": 3500,
                    "TypeName": "telemetry.reporting.config",
                    "Version": "000",
                    "TelemetryNameGtEnumSymbol": "af39eec9",
                    "UnitGtEnumSymbol": "f459a9c3",
                },
                "TypeName": "egauge.io",
                "Version": "000",
            }
        ],
        "TypeName": "electric.meter.component.gt",
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
    if "DisplayName" in d2:
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "HwUid" in d2:
        del d2["HwUid"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    # Axiom 2: If EgaugeIoList has non-zero length then ModbusHost must exist!
    del d2["ModbusHost"]
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2["ConfigList"] = []
    # Axiom 2 part 2: If EgaugeIoList has non-zero length then it has the same length as ConfigList
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2["EgaugeIoList"] = []
    Maker.dict_to_tuple(d2)

    if "ModbusPort" in d2:
        del d2["ModbusPort"]
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

    # End of Test
