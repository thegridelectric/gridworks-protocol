"""Tests spaceheat.node.gt type, version 100"""

import pytest
from pydantic import ValidationError

from gwproto.types import SpaceheatNodeGt


def test_spaceheat_node_gt_generated() -> None:
    d = {
        "ShNodeId": "41f2ae73-8782-406d-bda7-a95b5abe317e",
        "Alias": "elt1",
        "ActorClass": "NoActor",
        "Role": "BoostElement",
        "DisplayName": "First boost element",
        "ComponentId": "80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        "ReportingSamplePeriodS": 300,
        "InPowerMetering": False,
        "TypeName": "spaceheat.node.gt",
        "Version": "120",
    }
    assert SpaceheatNodeGt.model_validate(d).model_dump(exclude_none=True) == d

    d2 = dict(
        d,
        InPowerMetering="True",
    )
    # testing axiom 1: If InPowerMetering exists and is true, then NameplatePowerW must exist
    with pytest.raises(ValidationError):
        SpaceheatNodeGt.model_validate(d2)
