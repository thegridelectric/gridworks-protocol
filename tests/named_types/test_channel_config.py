"""Tests channel.config type, version 000"""

from gwproto.enums import Unit
from gwproto.named_types import ChannelConfig


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

    d2 = ChannelConfig.from_dict(d).to_dict()

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["Unit"]) is str

    d2 = dict(d, Unit="unknown_enum_thing")
    assert ChannelConfig(**d2).unit == Unit.default()
