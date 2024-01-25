"""Tests component.attribute.class.gt type, version 001"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import ComponentAttributeClassGt_Maker as Maker


def test_component_attribute_class_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": '29c5257b-8a86-4dbe-a9d4-9c7330c3c4d0',
        "MakeModelGtEnumSymbol": ,
        "DisplayName": "Sample CAC",
        "MinPollPeriodMs": ,
        "TypeName": "component.attribute.class.gt",
        "Version": "001",
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
        min_poll_period_ms=gtuple.MinPollPeriodMs,
        
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

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "MakeModel" in d2.keys():
        del d2["MakeModel"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "MinPollPeriodMs" in d2.keys():
        del d2["MinPollPeriodMs"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, MakeModelGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).MakeModel == MakeModel.default()

    d2 = dict(d, MinPollPeriodMs=".1")
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
