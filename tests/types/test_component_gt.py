"""Tests component.gt type, version 001"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import ComponentGt
from gwproto.types import ComponentGt_Maker as Maker


def test_component_gt_generated() -> None:
    t = ComponentGt(
        ComponentId="c6ec1ddb-5f51-4902-9807-a5ebc74d1102",
        ComponentAttributeClassId="739a6e32-bb9c-43bc-a28d-fb61be665522",
        ConfigList=[],
        DisplayName="Demo eGauge Power Meter",
        HwUid="000aaa",
    )

    d = {
        "ComponentId": "c6ec1ddb-5f51-4902-9807-a5ebc74d1102",
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "ConfigList": [],
        "DisplayName": "Demo eGauge Power Meter",
        "HwUid": "000aaa",
        "TypeName": "component.gt",
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
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
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
