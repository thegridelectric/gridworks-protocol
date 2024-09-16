"""Tests electric.meter.cac.gt type, version 000"""

from gwproto.types import ElectricMeterCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_electric_meter_cac_load() -> None:
    d = {
        "ComponentAttributeClassId": "a3d298fb-a4ef-427a-939d-02cc9c9689c1",
        # "MakeModelGtEnumSymbol": "d300635e",
        "MakeModel": "SCHNEIDERELECTRIC__IEM3455",
        "DisplayName": "Schneider Electric Iem3455 Power Meter",
        # "TelemetryNameList": ["af39eec9"],
        "TelemetryNameList": ["PowerW"],
        "PollPeriodMs": 1000,
        # "InterfaceGtEnumSymbol": "a6a4ac9f",
        "Interface": "RS485",
        "DefaultBaud": 9600,
        "TypeName": "electric.meter.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("ElectricMeterCac", d, ElectricMeterCacGt)])
