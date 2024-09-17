"""Tests spaceheat.node.gt type, version 200"""

from gwproto.enums import ActorClass
from gwproto.types import SpaceheatNodeGt


def test_spaceheat_node_gt_generated() -> None:
    d = {
        "Name": "aquastat-ctrl-relay",
        "ActorHierarchyName": "pi2.aquastat-ctrl-relay",
        "Handle": "admin.aquastat-ctrl-relay",
        "ActorClass": "Relay",
        "DisplayName": "Aquastat Control Relay",
        "ComponentId": "80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        "NameplatePowerW": None,
        "InPowerMetering": None,
        "ShNodeId": "92091523-4fa7-4a3e-820b-fddee089222f",
        "TypeName": "spaceheat.node.gt",
        "Version": "200",
    }

    t = SpaceheatNodeGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, ActorClass="unknown_enum_thing")
    assert SpaceheatNodeGt(**d2).actor_class == ActorClass.default()
