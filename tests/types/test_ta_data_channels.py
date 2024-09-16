"""Tests ta.data.channels type, version 000"""

from gwproto.types import TaDataChannels


def test_ta_data_channels_generated() -> None:
    d = {
        "TerminalAssetGNodeAlias": "hw1.isone.me.versant.keene.oak.ta",
        "TerminalAssetGNodeId": "7e152072-c91b-49d2-9ebd-f4fe1b684d06",
        "TimeUnixS": 1704142951,
        "Author": "Jessica Millar",
        "Channels": [
            {
                "DisplayName": "BoostPower",
                "AboutName": "a.elt1",
                "CapturedByName": "a.m",
                "TelemetryName": "PowerW",
                "TypeName": "data.channel",
                "Version": "000",
            }
        ],
        "Identifier": "ba6558d8-2fe8-4174-ac16-c36f84367c50",
        "TypeName": "ta.data.channels",
        "Version": "000",
    }
    assert TaDataChannels.model_validate(d).model_dump() == d
