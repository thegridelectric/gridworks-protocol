"""Tests channel.readings type, version 001"""

from gwproto.types import ChannelReadings


def test_channel_readings_generated() -> None:
    d = {
        "ChannelName": "hp-odu-pwr",
        "ChannelId": "e601041c-8cb4-4e6f-9163-e6ad2edb1b72",
        "ValueList": [4559],
        "ScadaReadTimeUnixMsList": [1656443705023],
        "TypeName": "channel.readings",
        "Version": "001",
    }

    d2 = ChannelReadings.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
