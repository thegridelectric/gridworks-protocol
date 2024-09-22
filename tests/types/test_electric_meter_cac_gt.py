"""Tests electric.meter.cac.gt type, version 000"""

from gwproto.types import ElectricMeterCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_electric_meter_cac_load() -> None:
    d = {
        "ComponentAttributeClassId": "6bcdc388-de10-40e6-979a-8d66bfcfe9ba",
        "MakeModel": "SCHNEIDERELECTRIC__IEM3455",
        "DisplayName": "Schneider Electric Iem3455 Power Meter",
        "TelemetryNameList": ["PowerW"],
        "PollPeriodMs": 1000,
        "Interface": "RS485",
        "DefaultBaud": 9600,
        "TypeName": "electric.meter.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("ElectricMeterCac", d, ElectricMeterCacGt)])
