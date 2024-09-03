"""Tests component.attribute.class.gt type, version 000"""

from typing import Any

from gwproto.enums.symbolized import SYMBOLIZE_ENV_VAR
from gwproto.types import ComponentAttributeClassGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_component_attribute_class_gt_load(monkeypatch: Any) -> None:  # noqa: ANN401
    monkeypatch.setenv(SYMBOLIZE_ENV_VAR, "1")
    d = {
        "ComponentAttributeClassId": "29c5257b-8a86-4dbe-a9d4-9c7330c3c4d0",
        "DisplayName": "Sample CAC",
        "MakeModelGtEnumSymbol": "00000000",
        "TypeName": "component.attribute.class.gt",
        "Version": "000",
    }
    assert_cac_load(
        [CacCase("ComponentAttributeClassGt", d, ComponentAttributeClassGt)]
    )
