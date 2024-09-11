"""Tests component.gt type, version 000"""

from gwproto.data_classes.components import Component
from gwproto.types import ComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_component_gt_generated() -> None:
    d = {
        "ComponentId": "987e0a5f-9036-411e-ba30-bac1075114ba",
        "ComponentAttributeClassId": "cec0cb71-77bf-48a6-b644-2dcf124ac9fa",
        "DisplayName": "Sample Component",
        "HwUid": "000aaa",
        "TypeName": "component.gt",
        "Version": "000",
    }
    assert_component_load([ComponentCase("ComponentGt", d, ComponentGt, Component)])
