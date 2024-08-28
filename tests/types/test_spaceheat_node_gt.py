"""Tests spaceheat.node.gt type, version 200"""

import json

import pytest
from gw.errors import GwTypeError
from pydantic import ValidationError

from gwproto.enums import ActorClass
from gwproto.types import SpaceheatNodeGt
from gwproto.types import SpaceheatNodeGtMaker as Maker


def test_spaceheat_node_gt_generated() -> None:
    t = SpaceheatNodeGt(
        name="aquastat-ctrl-relay",
        actor_hierarchy_name="pi2.aquastat-ctrl-relay",
        handle="admin.aquastat-ctrl-relay",
        actor_class=ActorClass.Relay,
        display_name="Aquastat Control Relay",
        component_id="80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        sh_node_id="92091523-4fa7-4a3e-820b-fddee089222f",
    )

    d = {
        "Name": "aquastat-ctrl-relay",
        "ActorHierarchyName": "pi2.aquastat-ctrl-relay",
        "Handle": "admin.aquastat-ctrl-relay",
        "ActorClassGtEnumSymbol": "49951f59",
        "DisplayName": "Aquastat Control Relay",
        "ComponentId": "80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        "ShNodeId": "92091523-4fa7-4a3e-820b-fddee089222f",
        "TypeName": "spaceheat.node.gt",
        "Version": "200",
    }

    assert t.as_dict() == d

    d2 = d.copy()

    del d2["ActorClassGtEnumSymbol"]
    d2["ActorClass"] = ActorClass.Relay.value
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
    del d2["Name"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ActorClassGtEnumSymbol"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ShNodeId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "ActorHierarchyName" in d2.keys():
        del d2["ActorHierarchyName"]
    Maker.dict_to_tuple(d2)

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
    if "NameplatePowerW" in d2.keys():
        del d2["NameplatePowerW"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "InPowerMetering" in d2.keys():
        del d2["InPowerMetering"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, ActorClassGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).actor_class == ActorClass.default()

    d2 = dict(d, NameplatePowerW=".1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, InPowerMetering="this is not a boolean")
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

    d2 = dict(d, Name="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ShNodeId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
