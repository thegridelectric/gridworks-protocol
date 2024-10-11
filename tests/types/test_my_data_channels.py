"""Tests my.data.channels type, version 000"""

from gwproto.types import MyDataChannels


def test_my_data_channels_generated() -> None:
    d = {
        "FromGNodeAlias": "hw1.isone.me.versant.keene.beech.scada",
        "FromGNodeInstanceId": "98542a17-3180-4f2a-a929-6023f0e7a106",
        "MessageCreatedMs": 1728651445746,
        "ChannelList": [
            {
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
        ],
        "TypeName": "my.data.channels",
        "Version": "000",
    }

    d2 = MyDataChannels.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
