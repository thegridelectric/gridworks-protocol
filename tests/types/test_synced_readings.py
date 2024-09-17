"""Tests synced.readings type, version 000"""

from gwproto.types import SyncedReadings


def test_synced_readings_generated() -> None:
    d = {
        "ScadaReadTimeUnixMs": 1656587343297,
        "ChannelNameList": ["hp-ewt", "hp-lwt"],
        "ValueList": [32755, 38870],
        "TypeName": "synced.readings",
        "Version": "000",
    }

    t = SyncedReadings(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
