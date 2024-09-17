"""Tests electric.meter.cac.gt type, version 001"""

from gwproto.enums import MakeModel
from gwproto.types import ElectricMeterCacGt


def test_electric_meter_cac_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "6bcdc388-de10-40e6-979a-8d66bfcfe9ba",
        "MakeModel": "SCHNEIDERELECTRIC__IEM3455",
        "DisplayName": "Schneider Electric Iem3455 Power Meter",
        "TelemetryNameList": ["af39eec9"],
        "MinPollPeriodMs": 1000,
        "DefaultBaud": 9600,
        "TypeName": "electric.meter.cac.gt",
        "Version": "001",
    }

    t = ElectricMeterCacGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, MakeModel="unknown_enum_thing")
    assert ElectricMeterCacGt(**d2).make_model == MakeModel.default()
