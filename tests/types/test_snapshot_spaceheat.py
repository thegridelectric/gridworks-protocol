"""Tests snapshot.spaceheat type, version 001"""

from gwproto.types import SnapshotSpaceheat


def test_snapshot_spaceheat_generated() -> None:
    d = {
        "FromGNodeAlias": "d1.isone.ct.newhaven.rose.scada",
        "FromGNodeInstanceId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "SnapshotTimeUnixMs": 1726636445320,
        "LatestReadingList": [
            {
                "ScadaReadTimeUnixMs": 1726636440150,
                "ChannelName": "hw-ewt",
                "Value": 54000,
                "TypeName": "single.reading",
                "Version": "000",
            },
            {
                "ScadaReadTimeUnixMs": 1726636440243,
                "ChannelName": "hw-ewt",
                "Value": 65232,
                "TypeName": "single.reading",
                "Version": "000",
            },
        ],
        "TypeName": "snapshot.spaceheat",
        "Version": "001",
    }
    d2 = SnapshotSpaceheat.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
