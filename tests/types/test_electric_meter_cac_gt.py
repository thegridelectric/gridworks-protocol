"""Tests electric.meter.cac.gt type, version 001"""

import pytest
from pydantic import ValidationError

from gwproto.enums import MakeModel
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import ElectricMeterCacGt


def test_electric_meter_cac_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "DefaultBaud": 9600,
        "DisplayName": "EGauge 4030",
        "MakeModel": "EGAUGE__4030",
        "MinPollPeriodMs": 1000,
        "TelemetryNameList": [
            "PowerW",
            "MilliWattHours",
            "VoltageRmsMilliVolts",
            "CurrentRmsMicroAmps",
            "FrequencyMicroHz",
        ],
        "TypeName": "electric.meter.cac.gt",
        "Version": "001",
    }

    d2 = ElectricMeterCacGt.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

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
