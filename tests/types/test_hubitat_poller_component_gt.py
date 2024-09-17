"""Tests hubitat.poller.component.gt type, version 000"""

from gwproto.types.hubitat_poller_component_gt import HubitatPollerComponentGt


def test_hubitat_poller_component_gt_generated() -> None:
    d = {
        "ComponentId": ,
        "ComponentAttributeClassId": ,
        "DisplayName": ,
        "HwUid": ,
        "Poller": ,
        "TypeName": "hubitat.poller.component.gt",
        "Version": "000",
    }

    t = HubitatPollerComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
