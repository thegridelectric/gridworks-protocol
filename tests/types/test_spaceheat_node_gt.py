"""Tests spaceheat.node.gt type, version 200"""

from gwproto.enums import ActorClass
from gwproto.types import SpaceheatNodeGt


def test_spaceheat_node_gt_generated() -> None:
    d = {
        "Name": "relay8",
        "Handle": "admin.aquastat-ctrl.relay8",
        "ActorClass": "Relay",
        "DisplayName": "Aquastat Control Relay",
        "ComponentId": "80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        "ShNodeId": "92091523-4fa7-4a3e-820b-fddee089222f",
        "TypeName": "spaceheat.node.gt",
        "Version": "200",
    }

    d2 = SpaceheatNodeGt.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["ActorClass"]) is str

    d2 = dict(d, ActorClass="unknown_enum_thing")
    assert SpaceheatNodeGt(**d2).ActorClass == ActorClass.default()
