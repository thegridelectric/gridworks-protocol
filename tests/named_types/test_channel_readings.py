"""Tests channel.readings type, version 002"""

from gwproto.named_types import ChannelReadings


def test_channel_readings_generated() -> None:
    d = {
        "ChannelName": "hp-odu-pwr",
        "ValueList": [4559],
        "ScadaReadTimeUnixMsList": [1656443705023],
        "TypeName": "channel.readings",
        "Version": "002",
    }

    d2 = ChannelReadings.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
