"""Tests snapshot.spaceheat type, version 002"""

from gwproto.named_types import SnapshotSpaceheat


def test_snapshot_spaceheat_generated() -> None:
    d = {
        "FromGNodeAlias": "d1.isone.ct.newhaven.rose.scada",
        "FromGNodeInstanceId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "SnapshotTimeUnixMs": 1709915800472,
        "LatestReadingList": [],
        "LatestStateList": [],
        "TypeName": "snapshot.spaceheat",
        "Version": "002",
    }

    d2 = SnapshotSpaceheat.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
