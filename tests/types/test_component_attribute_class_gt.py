"""Tests component.attribute.class.gt type, version 001"""

from gwproto.enums import MakeModel
from gwproto.types import ComponentAttributeClassGt


def test_component_attribute_class_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "e52cb571-913a-4614-90f4-5cc81f8e7fe5",
        "MakeModel": "EKM__HOTSPWM075HD",
        "DisplayName": "EKM Hot-Spwm-075-HD Flow Meter",
        "MinPollPeriodMs": 1000,
        "TypeName": "component.attribute.class.gt",
        "Version": "001",
    }

    t = ComponentAttributeClassGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, MakeModel="unknown_enum_thing")
    assert ComponentAttributeClassGt(**d2).make_model == MakeModel.default()
