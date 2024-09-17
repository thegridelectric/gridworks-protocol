"""Tests egauge.register.config type, version 000"""

from gwproto.types import EgaugeRegisterConfig


def test_egauge_register_config_generated() -> None:
    d = {
        "Address": 9004,
        "Name": "Garage power",
        "Description": "some description",
        "Type": "f32",
        "Denominator": 1,
        "Unit": "W",
        "TypeName": "egauge.register.config",
        "Version": "000",
    }

    t = EgaugeRegisterConfig(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
