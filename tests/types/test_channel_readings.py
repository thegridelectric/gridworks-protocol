"""Tests channel.readings type, version 000"""

from gwproto.types import ChannelReadings


def test_channel_readings_generated() -> None:
    d = {
        "Name": "hp-ewt",
        "DisplayName": "HP EST",
        "AboutNodeName": "hp-ewt",
        "CapturedByNodeName": "analog-temp",
        "TelemetryName": "WaterTempCTimes1000",
        "TerminalAssetAlias": "a.b",
        "Id": "1f5cab3f-05c9-4fcd-bc92-c51fc0d570df",
        "ValueList": [4559],
        "ScadaReadTimeUnixMsList": [1656443705023],
        "TypeName": "channel.readings",
        "Version": "001",
    }

    d2 = ChannelReadings.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
