"""Tests single.reading type, version 000"""

from gwproto.types import SingleReading


def test_single_reading_generated() -> None:
    d = {
        "ScadaReadTimeUnixMs": 1656513094288,
        "ChannelName": "hp-ewt",
        "Value": 63430,
        "TypeName": "single.reading",
        "Version": "000",
    }

    t = SingleReading(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
