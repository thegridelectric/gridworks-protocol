"""Tests hubitat.tank.component.gt type, version 000"""

from gwproto.types.hubitat_tank_component_gt import HubitatTankComponentGt


def test_hubitat_tank_component_gt_generated() -> None:
    d = {
        "ComponentId": ,
        "ComponentAttributeClassId": ,
        "Tank": ,
        "DisplayName": ,
        "HwUid": ,
        "TypeName": "hubitat.tank.component.gt",
        "Version": "000",
    }

    t = HubitatTankComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
