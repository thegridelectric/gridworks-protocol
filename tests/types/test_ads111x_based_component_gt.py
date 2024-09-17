"""Tests ads111x.based.component.gt type, version 000"""

from gwproto.types.ads111x_based_component_gt import Ads111xBasedComponentGt


def test_ads111x_based_component_gt_generated() -> None:
    d = {
        "ComponentId": "02f600e3-8692-43f8-84f2-a03c09c197e7",
        "ComponentAttributeClassId": "432073b8-4d2b-4e36-9229-73893f33f846",
        "DisplayName": "4-channel Ads for Beachrose",
        "OpenVoltageByAds": [4.89, 4.95, 4.75],
        "ConfigList": ,
        "ThermistorConfigList": ,
        "HwUid": "1001",
        "TypeName": "ads111x.based.component.gt",
        "Version": "000",
    }

    t = Ads111xBasedComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
