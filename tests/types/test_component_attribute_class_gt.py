"""Tests component.attribute.class.gt type, version 001"""

import pytest
from pydantic import ValidationError

from gwproto.enums import MakeModel
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
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

    d2 = ComponentAttributeClassGt.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["MakeModel"]) is str

    d2 = dict(
        d,
        MakeModel="unknown_enum_thing",
        ComponentAttributeClassId="b06c5c03-ed08-4dec-82a3-b43d6f9b02e3",
    )
    assert ComponentAttributeClassGt(**d2).MakeModel == MakeModel.default()

    random_uuid = "91567108-98ea-45af-aca5-f0026df3e131"
    d2 = {
        "ComponentAttributeClassId": random_uuid,
        "MakeModel": "EKM__HOTSPWM075HD",
        "DisplayName": "EKM Hot-Spwm-075-HD Flow Meter",
        "MinPollPeriodMs": 1000,
        "TypeName": "component.attribute.class.gt",
        "Version": "001",
    }

    with pytest.raises(ValidationError):
        ComponentAttributeClassGt.model_validate(d2)

    d2 = {
        "ComponentAttributeClassId": CACS_BY_MAKE_MODEL[MakeModel.ADAFRUIT__642],
        "MakeModel": "EKM__HOTSPWM075HD",
        "DisplayName": "EKM Hot-Spwm-075-HD Flow Meter",
        "MinPollPeriodMs": 1000,
        "TypeName": "component.attribute.class.gt",
        "Version": "001",
    }

    with pytest.raises(ValidationError):
        ComponentAttributeClassGt.model_validate(d2)
