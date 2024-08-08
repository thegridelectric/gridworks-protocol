"""Tests component.attribute.class.gt type, version 001"""

import json
import uuid

import pytest
from gw.errors import GwTypeError
from gwproto.enums import MakeModel
from gwproto.types import ComponentAttributeClassGt
from gwproto.types import ComponentAttributeClassGtMaker as Maker
from pydantic import ValidationError


def test_component_attribute_class_gt_generated() -> None:
    t = ComponentAttributeClassGt(
        component_attribute_class_id="e52cb571-913a-4614-90f4-5cc81f8e7fe5",
        make_model=MakeModel.EKM__HOTSPWM075HD,
        display_name="EKM Hot-Spwm-075-HD Flow Meter",
        min_poll_period_ms=1000,
    )

    d = {
        "ComponentAttributeClassId": "e52cb571-913a-4614-90f4-5cc81f8e7fe5",
        "MakeModelGtEnumSymbol": "208f827f",
        "DisplayName": "EKM Hot-Spwm-075-HD Flow Meter",
        "MinPollPeriodMs": 1000,
        "TypeName": "component.attribute.class.gt",
        "Version": "001",
    }

    assert t.as_dict() == d

    d2 = d.copy()

    del d2["MakeModelGtEnumSymbol"]
    d2["MakeModel"] = MakeModel.EKM__HOTSPWM075HD.value
    assert t == Maker.dict_to_tuple(d2)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple(d)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple('"not a dict"')

    # Checking axiom

    d2["ComponentAttributeClassId"] = str(uuid.uuid4())
    # Axiom 1: (MakeModel, ComponentAttributeClassId)  must be a key, value pair in CACS_BY_MAKE_MODEL
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

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

    ######################################
    # Optional attributes can be removed from type
    ######################################

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
    assert Maker.dict_to_tuple(d2).make_model == MakeModel.default()

    d2 = dict(d, MinPollPeriodMs="1000.1")
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

    d2 = dict(d, MinPollPeriodMs=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Check dataclass conversion
    ######################################

    dc = Maker.tuple_to_dc(t)
    assert t == Maker.dc_to_tuple(dc)
