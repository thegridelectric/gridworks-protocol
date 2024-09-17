"""Tests data.channel.gt type, version 001"""

from gwproto.enums import TelemetryName
from gwproto.types import DataChannelGt


def test_data_channel_gt_generated() -> None:
    d = {
        "Name": "hp-idu-pwr",
        "DisplayName": "Hp IDU",
        "AboutNodeName": "hp-idu-pwr",
        "CapturedByNodeName": "power-meter",
        "TelemetryName": "PowerW",
        "TerminalAssetAlias": "hw1.isone.me.versant.keene.beech.ta",
        "InPowerMetering": True,
        "StartS": 1721405699,
        "Id": "50cf426b-ff3f-4a30-8415-8d3fba5e0ab7",
        "TypeName": "data.channel.gt",
        "Version": "001",
    }

    t = DataChannelGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, TelemetryName="unknown_enum_thing")
    assert DataChannelGt(**d2).telemetry_name == TelemetryName.default()
