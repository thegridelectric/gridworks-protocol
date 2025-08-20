"""Tests dfr.component.gt type, version 000"""

from gwproto.named_types import DfrComponentGt


def test_dfr_component_gt_generated() -> None:
    d = {
        "ComponentId": "c6ec1ddb-5f51-4902-9807-a5ebc74d1102",
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "ConfigList": [],
        "DisplayName": "Dfr 010V For Beech",
        "HwUid": "NA",
        "I2cAddressList": [94, 95],
        "TypeName": "dfr.component.gt",
        "Version": "000",
    }

    d2 = DfrComponentGt.from_dict(d).to_dict()

    assert d2 == d
