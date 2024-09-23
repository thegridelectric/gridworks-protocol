"""Tests component.gt type, version 001"""

from gwproto.data_classes.components import Component
from gwproto.types import ComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_component_gt_generated() -> None:
    d = {
        "ComponentId": "c6ec1ddb-5f51-4902-9807-a5ebc74d1102",
        "ComponentAttributeClassId": "432073b8-4d2b-4e36-9229-73893f33f846",
        "ConfigList": [
            {
                "ChannelName": "store-cold-pipe",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 60,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 30,
                "Exponent": 3,
                "Unit": "Celcius",
                "TypeName": "channel.config",
                "Version": "000",
            }
        ],
        "DisplayName": "MultiTemp",
        "HwUid": "000aaa",
        "TypeName": "component.gt",
        "Version": "001",
    }

    assert_component_load([ComponentCase("ComponentGt", d, ComponentGt, Component)])
    assert d == ComponentGt.model_validate(d).model_dump(exclude_none=True)
