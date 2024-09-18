"""Tests egauge.io type, version 001"""

from gwproto.types import EgaugeIo


def test_egauge_io_generated() -> None:
    d = {
        "ChannelName": "hp-idu-pwr",
        "InputConfig": {
            "Address": 9004,
            "Name": "Garage power",
            "Description": "",
            "Type": "f32",
            "Denominator": 1,
            "Unit": "W",
            "TypeName": "egauge.register.config",
            "Version": "000",
        },
        "TypeName": "egauge.io",
        "Version": "001",
    }

    d2 = EgaugeIo.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
