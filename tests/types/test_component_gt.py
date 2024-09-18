"""Tests component.gt type, version 001"""

from gwproto.types import ComponentGt


def test_component_gt_generated() -> None:
    d = {
        "ComponentId": "c6ec1ddb-5f51-4902-9807-a5ebc74d1102",
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "ConfigList": [],
        "DisplayName": "Demo eGauge Power Meter",
        "HwUid": "000aaa",
        "TypeName": "component.gt",
        "Version": "001",
    }

    d2 = ComponentGt.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
