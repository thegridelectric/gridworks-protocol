"""Tests async.btu.data type, version 000"""

from gwproto.named_types import AsyncBtuData


def test_async_btu_data_generated() -> None:
    d = {
        "HwUid": "pico_aaaaaa",
        "AboutNodeNameList": ["hp-lwt"],
        "MeasurementList": [6550],
        "UnitList": ["CelsiusTimes100"],
        "TypeName": "async.btu.data",
        "Version": "000",
    }

    d2 = AsyncBtuData.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
