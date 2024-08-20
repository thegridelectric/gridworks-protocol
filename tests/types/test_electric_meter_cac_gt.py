"""Tests electric.meter.cac.gt type, version 000"""

import json

import pytest
from pydantic import ValidationError

from gwproto.enums import LocalCommInterface, MakeModel
from gwproto.errors import SchemaError
from gwproto.types import ElectricMeterCacGt_Maker as Maker


def test_electric_meter_cac_gt_generated() -> None:  # noqa: PLR0915
    d = {
        "ComponentAttributeClassId": "a3d298fb-a4ef-427a-939d-02cc9c9689c1",
        "MakeModelGtEnumSymbol": "d300635e",
        "DisplayName": "Schneider Electric Iem3455 Power Meter",
        "TelemetryNameList": ["af39eec9"],
        "PollPeriodMs": 1000,
        "InterfaceGtEnumSymbol": "a6a4ac9f",
        "DefaultBaud": 9600,
        "TypeName": "electric.meter.cac.gt",
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
        make_model=gtuple.MakeModel,
        display_name=gtuple.DisplayName,
        telemetry_name_list=gtuple.TelemetryNameList,
        poll_period_ms=gtuple.PollPeriodMs,
        interface=gtuple.Interface,
        default_baud=gtuple.DefaultBaud,
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
    del d2["MakeModelGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TelemetryNameList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["PollPeriodMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["InterfaceGtEnumSymbol"]
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
    if "DefaultBaud" in d2:
        del d2["DefaultBaud"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, MakeModelGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).MakeModel == MakeModel.default()

    d2 = dict(d, PollPeriodMs="1000.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, InterfaceGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).Interface == LocalCommInterface.default()

    d2 = dict(d, DefaultBaud="9600.1")
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

    # End of Test
