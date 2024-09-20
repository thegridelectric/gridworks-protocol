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

    d2 = DataChannelGt.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["TelemetryName"]) is str

    d2 = dict(d, TelemetryName="unknown_enum_thing")
    assert DataChannelGt(**d2).TelemetryName == TelemetryName.default().value
