"""Tests spaceheat.node.gt type, version 100"""

import pytest
from gw.errors import GwTypeError

from gwproto.named_types import SpaceheatNodeGt


def test_spaceheat_node_gt_generated() -> None:
    d = {
        "ShNodeId": "41f2ae73-8782-406d-bda7-a95b5abe317e",
        "Name": "elt1",
        "ActorClass": "NoActor",
        "DisplayName": "First boost element",
        "ComponentId": "80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        "ReportingSamplePeriodS": 300,
        "InPowerMetering": False,
        "TypeName": "spaceheat.node.gt",
        "Version": "200",
    }
    d2 = SpaceheatNodeGt.from_dict(d).to_dict()
    assert d2 == d

    d2 = dict(
        d,
        InPowerMetering="True",
    )
    # testing axiom 1: If InPowerMetering exists and is true, then NameplatePowerW must exist
    with pytest.raises(GwTypeError):
        SpaceheatNodeGt.from_dict(d2)
