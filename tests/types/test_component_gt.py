"""Tests component.gt type, version 001"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import ComponentGt_Maker as Maker


def test_component_gt_generated() -> None:
    d = {
        "": ,
        "ComponentId": ,
        "ComponentAttributeClassId": '0a2fed00-8ff9-4391-a6d8-4b08ab94dfe1',
        "DisplayName": "Sample Component",
        "HwUid": "000aaa",
        "TypeName": "component.gt",
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
        =gtuple.,
        component_id=gtuple.ComponentId,
        component_attribute_class_id=gtuple.ComponentAttributeClassId,
        display_name=gtuple.DisplayName,
        hw_uid=gtuple.HwUid,
        
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
    if "" in d2.keys():
        del d2[""]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "ComponentId" in d2.keys():
        del d2["ComponentId"]
    Maker.dict_to_tuple(d2)

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

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
