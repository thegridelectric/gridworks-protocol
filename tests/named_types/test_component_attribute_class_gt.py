"""Tests component.attribute.class.gt type, version 001"""

import pytest
from gw.errors import GwTypeError

from gwproto.enums import MakeModel
from gwproto.named_types import ComponentAttributeClassGt
from gwproto.type_helpers import CACS_BY_MAKE_MODEL


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

    d2 = dict(
        d,
        MakeModel="unknown_enum_thing",
        ComponentAttributeClassId="c00ec7bd-332a-4647-b08a-b00705adee2d",
    )
    assert ComponentAttributeClassGt.from_dict(d2).make_model == MakeModel.default()

    d2 = dict(d, ComponentAttributeClassId=CACS_BY_MAKE_MODEL[MakeModel.ADAFRUIT__642])

    with pytest.raises(GwTypeError):
        ComponentAttributeClassGt.from_dict(d2)
