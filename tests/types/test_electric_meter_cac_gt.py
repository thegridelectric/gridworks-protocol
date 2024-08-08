"""Tests electric.meter.cac.gt type, version 001"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import MakeModel, TelemetryName
from gwproto.types import ElectricMeterCacGt
from gwproto.types import ElectricMeterCacGtMaker as Maker
from pydantic import ValidationError


def test_electric_meter_cac_gt_generated() -> None:
    t = ElectricMeterCacGt(
        component_attribute_class_id="6bcdc388-de10-40e6-979a-8d66bfcfe9ba",
        make_model=MakeModel.SCHNEIDERELECTRIC__IEM3455,
        display_name="Schneider Electric Iem3455 Power Meter",
        telemetry_name_list=[TelemetryName.PowerW],
        min_poll_period_ms=1000,
        default_baud=9600,
    )

    d = {
        "ComponentAttributeClassId": "6bcdc388-de10-40e6-979a-8d66bfcfe9ba",
        "MakeModelGtEnumSymbol": "d300635e",
        "DisplayName": "Schneider Electric Iem3455 Power Meter",
        "TelemetryNameList": ["af39eec9"],
        "MinPollPeriodMs": 1000,
        "DefaultBaud": 9600,
        "TypeName": "electric.meter.cac.gt",
        "Version": "001",
    }

    assert t.as_dict() == d

    d2 = d.copy()

    del d2["MakeModelGtEnumSymbol"]
    d2["MakeModel"] = MakeModel.SCHNEIDERELECTRIC__IEM3455.value
    d2["TelemetryNameList"] = [TelemetryName.PowerW]
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
    del d2["ComponentAttributeClassId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MakeModelGtEnumSymbol"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["TelemetryNameList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["MinPollPeriodMs"]
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
    if "DefaultBaud" in d2.keys():
        del d2["DefaultBaud"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, MakeModelGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).make_model == MakeModel.default()

    d2 = dict(d, MinPollPeriodMs="1000.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, DefaultBaud="9600.1")
    with pytest.raises(ValidationError):
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

    d2 = dict(d, ComponentAttributeClassId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
