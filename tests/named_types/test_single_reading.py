"""Tests single.reading type, version 000"""

from gwproto.named_types import SingleReading


def test_single_reading_generated() -> None:
    d = {
        "ScadaReadTimeUnixMs": 1656513094288,
        "ChannelName": "hp-ewt",
        "Value": 63430,
        "TypeName": "single.reading",
        "Version": "000",
    }

    d2 = SingleReading.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
