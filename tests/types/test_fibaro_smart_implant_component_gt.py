"""Tests fibaro.smart.implant.component.gt type, version 000"""

from gwproto.types.fibaro_smart_implant_component_gt import FibaroSmartImplantComponentGt


def test_fibaro_smart_implant_component_gt_generated() -> None:
    d = {
        "ComponentId": ,
        "ComponentAttributeClassId": ,
        "ZWaveDSK": ,
        "DisplayName": ,
        "HwUid": ,
        "TypeName": "fibaro.smart.implant.component.gt",
        "Version": "000",
    }

    t = FibaroSmartImplantComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
