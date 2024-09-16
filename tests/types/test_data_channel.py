"""Tests data.channel type, version 000"""

from gwproto.types import DataChannel


def test_data_channel_generated() -> None:
    d = {
        "DisplayName": "BoostPower",
        "AboutName": "a.elt1",
        "CapturedByName": "a.m",
        "TelemetryName": "PowerW",
        "TypeName": "data.channel",
        "Version": "000",
    }
    assert DataChannel.model_validate(d).model_dump() == d
