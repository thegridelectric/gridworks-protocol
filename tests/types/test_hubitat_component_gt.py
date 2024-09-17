"""Tests hubitat.component.gt type, version 000"""

from gwproto.types.hubitat_component_gt import HubitatComponentGt


def test_hubitat_component_gt_generated() -> None:
    d = {
        "ComponentId": ,
        "ComponentAttributeClassId": ,
        "Hubitat": ,
        "DisplayName": ,
        "HwUid": ,
        "TypeName": "hubitat.component.gt",
        "Version": "000",
    }

    t = HubitatComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
