"""Tests relay.component.gt type, version 000"""

import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import RelayComponentGt_Maker as Maker


def test_relay_component_gt_generated() -> None:
    d = {
        "ComponentId": "798fe14a-4073-41eb-bce2-075906aee6bb",
        "ComponentAttributeClassId": "69f101fc-22e4-4caa-8103-50b8aeb66028",
        "DisplayName": "relay for first elt in tank",
        "Gpio": 0,
        "HwUid": "abc123",
        "NormallyOpen": True,
        "TypeName": "relay.component.gt",
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
        gpio=gtuple.Gpio,
        hw_uid=gtuple.HwUid,
        normally_open=gtuple.NormallyOpen,
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
    del d2["NormallyOpen"]
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
    if "Gpio" in d2.keys():
        del d2["Gpio"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "HwUid" in d2.keys():
        del d2["HwUid"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, Gpio="0.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, NormallyOpen="this is not a boolean")
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

    d2 = dict(d, ComponentId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
