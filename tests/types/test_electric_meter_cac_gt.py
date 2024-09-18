"""Tests electric.meter.cac.gt type, version 001"""

from gwproto.enums import MakeModel
from gwproto.types import ElectricMeterCacGt


def test_electric_meter_cac_gt_generated() -> None:
    d = {
      "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
      "DefaultBaud": 9600,
      "DisplayName": "EGauge 4030",
      "MakeModel": "EGAUGE__4030",
      "MinPollPeriodMs": 1000,
      "PollPeriodMs": 1000,
      "TelemetryNameList": [
        "PowerW",
        "MilliWattHours",
        "VoltageRmsMilliVolts",
        "CurrentRmsMicroAmps",
        "FrequencyMicroHz"
      ],
      "TypeName": "electric.meter.cac.gt",
      "Version": "001"
    }

    t = ElectricMeterCacGt(**d)

    assert t.model_dump(exclude_none=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, MakeModel="unknown_enum_thing", ComponentAttributeClassId="9f4317e7-0fb4-4ee6-8900-4e56c5b8e322")
    assert ElectricMeterCacGt(**d2).MakeModel == MakeModel.default()
