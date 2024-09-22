"""Tests component.gt type, version 001"""

from gwproto.data_classes.components import Component
from gwproto.types import ComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_component_gt_generated() -> None:
    d = {
        "ComponentId": "c6ec1ddb-5f51-4902-9807-a5ebc74d1102",
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "DisplayName": "Demo eGauge Power Meter",
        "HwUid": "000aaa",
        "TypeName": "component.gt",
        "Version": "000",
    }

    assert_component_load([ComponentCase("ComponentGt", d, ComponentGt, Component)])
    assert d == ComponentGt.model_validate(d).model_dump(exclude_none=True)
