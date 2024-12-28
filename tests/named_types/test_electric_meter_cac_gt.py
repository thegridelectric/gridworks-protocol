"""Tests electric.meter.cac.gt type, version 000"""

import pytest
from pydantic import ValidationError

from gwproto.enums import MakeModel
from gwproto.named_types import ElectricMeterCacGt
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from tests.cac_load_utils import CacCase, assert_cac_load


def test_electric_meter_cac_load() -> None:
    d = {
        "ComponentAttributeClassId": "6bcdc388-de10-40e6-979a-8d66bfcfe9ba",
        "MinPollPeriodMs": 1000,
        "MakeModel": "SCHNEIDERELECTRIC__IEM3455",
        "DisplayName": "Schneider Electric Iem3455 Power Meter",
        "TelemetryNameList": ["PowerW"],
        "PollPeriodMs": 1000,
        "DefaultBaud": 9600,
        "TypeName": "electric.meter.cac.gt",
        "Version": "001",
    }
    assert_cac_load([CacCase("ElectricMeterCac", d, ElectricMeterCacGt)])

    d2 = ElectricMeterCacGt.model_validate(d).model_dump(exclude_none=True)
    assert type(d2["MakeModel"]) is str

    d2 = dict(
        d,
        MakeModel="unknown_enum_thing",
        ComponentAttributeClassId="c00ec7bd-332a-4647-b08a-b00705adee2d",
    )
    assert ElectricMeterCacGt(**d2).MakeModel == MakeModel.default()

    d2 = dict(d, ComponentAttributeClassId=CACS_BY_MAKE_MODEL[MakeModel.ADAFRUIT__642])

    with pytest.raises(ValidationError):
        ElectricMeterCacGt.model_validate(d2)
