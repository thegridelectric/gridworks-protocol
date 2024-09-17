"""Tests channel.config type, version 000"""

from gwproto.enums import Unit
from gwproto.types import ChannelConfig


def test_channel_config_generated() -> None:
    d = {
        "ChannelName": "hp-idu-pwr",
        "PollPeriodMs": 300,
        "CapturePeriodS": 60,
        "AsyncCapture": True,
        "AsyncCaptureDelta": 30,
        "Exponent": 6,
        "Unit": "W",
        "TypeName": "channel.config",
        "Version": "000",
    }

    t = ChannelConfig(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, Unit="unknown_enum_thing")
    assert ChannelConfig(**d2).unit == Unit.default()
