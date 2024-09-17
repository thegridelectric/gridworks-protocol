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

    t = EgaugeIo(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
