"""Tests egauge.register.config type, version 000"""

from gwproto.named_types import EgaugeRegisterConfig


def test_egauge_register_config_generated() -> None:
    d = {
        "Address": 9004,
        "Name": "Garage power",
        "Description": "",
        "Type": "f32",
        "Denominator": 1,
        "Unit": "W",
        "TypeName": "egauge.register.config",
        "Version": "000",
    }
    assert EgaugeRegisterConfig.model_validate(d).model_dump() == d
