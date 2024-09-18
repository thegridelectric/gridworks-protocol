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

    d2 = ChannelConfig.model_validate(d).model_dump(exclude_none=True)

    assert type(d2["Unit"]) is str
    assert d2 == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, Unit="unknown_enum_thing")
    assert ChannelConfig(**d2).Unit == Unit.default()
