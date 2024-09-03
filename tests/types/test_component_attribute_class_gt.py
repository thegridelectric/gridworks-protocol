"""Tests component.attribute.class.gt type, version 000"""

from gwproto.types import ComponentAttributeClassGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_component_attribute_class_gt_load() -> None:
    d = {
        "ComponentAttributeClassId": "29c5257b-8a86-4dbe-a9d4-9c7330c3c4d0",
        "DisplayName": "Sample CAC",
        "MakeModel": "UNKNOWNMAKE__UNKNOWNMODEL",
        "TypeName": "component.attribute.class.gt",
        "Version": "000",
    }
    assert_cac_load(
        [CacCase("ComponentAttributeClassGt", d, ComponentAttributeClassGt)]
    )
