"""Tests component.attribute.class.gt type, version 001"""

from gwproto.enums import MakeModel
from gwproto.named_types import ComponentAttributeClassGt


def test_component_attribute_class_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "e52cb571-913a-4614-90f4-5cc81f8e7fe5",
        "MakeModel": "EKM__HOTSPWM075HD",
        "DisplayName": "EKM Hot-Spwm-075-HD Flow Meter",
        "MinPollPeriodMs": 1000,
        "TypeName": "component.attribute.class.gt",
        "Version": "001",
    }

    d2 = ComponentAttributeClassGt.from_dict(d).to_dict()

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["MakeModel"]) is str

    d2 = dict(d, MakeModel="unknown_enum_thing")
    assert ComponentAttributeClassGt(**d2).make_model == MakeModel.default()
