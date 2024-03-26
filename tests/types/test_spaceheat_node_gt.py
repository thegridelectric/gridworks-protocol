"""Tests spaceheat.node.gt type, version 200"""

import json

import pytest
from pydantic import ValidationError

from gwproto.enums import ActorClass
from gwproto.errors import SchemaError
from gwproto.types import SpaceheatNodeGt
from gwproto.types import SpaceheatNodeGt_Maker as Maker


def test_spaceheat_node_gt_generated() -> None:
    t = SpaceheatNodeGt(
        ShNodeId="92091523-4fa7-4a3e-820b-fddee089222f",
        Name="s.pwr-meter",
        Handle="pwr-meter",
        ActorClass=ActorClass.PowerMeter,
        DisplayName="Primary Power Meter",
        ComponentId="80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        InPowerMetering=False,
    )

    d = {
        "ShNodeId": "92091523-4fa7-4a3e-820b-fddee089222f",
        "Name": "s.pwr-meter",
        "Handle": "pwr-meter",
        "ActorClassGtEnumSymbol": "2ea112b9",
        "DisplayName": "Primary Power Meter",
        "ComponentId": "80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        "InPowerMetering": False,
        "TypeName": "spaceheat.node.gt",
        "Version": "200",
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
    del d2["ShNodeId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Name"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ActorClassGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "Handle" in d2.keys():
        del d2["Handle"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "ComponentId" in d2.keys():
        del d2["ComponentId"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "InPowerMetering" in d2.keys():
        del d2["InPowerMetering"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, ActorClassGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).ActorClass == ActorClass.default()

    d2 = dict(d, InPowerMetering="this is not a boolean")
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

    d2 = dict(d, ShNodeId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Name="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Handle="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
