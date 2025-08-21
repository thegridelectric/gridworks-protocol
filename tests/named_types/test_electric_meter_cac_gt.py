"""Tests electric.meter.cac.gt type, version 001"""

from gwproto.named_types import ElectricMeterCacGt


def test_electric_meter_cac_load() -> None:
    d = {
        "ComponentAttributeClassId": "6bcdc388-de10-40e6-979a-8d66bfcfe9ba",
        "MinPollPeriodMs": 1000,
        "MakeModel": "SCHNEIDERELECTRIC__IEM3455",
        "DisplayName": "Schneider Electric Iem3455 Power Meter",
        "TelemetryNameList": ["PowerW"],
        "DefaultBaud": 9600,
        "TypeName": "electric.meter.cac.gt",
        "Version": "001",
    }

    d2 = ElectricMeterCacGt.from_dict(d).to_dict()
    assert d2 == d
    assert type(d2["MakeModel"]) is str
