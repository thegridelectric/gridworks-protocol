"""Tests simple.temp.sensor.cac.gt type, version 000"""

from gwproto.types import SimpleTempSensorCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_simple_temp_sensor_cac_gt_load() -> None:
    d = {
        "ComponentAttributeClassId": "8a1a1538-ed2d-4829-9c03-f9be1c9f9c83",
        # "MakeModelGtEnumSymbol": "acd93fb3",
        "MakeModel": "ADAFRUIT__642",
        "TypicalResponseTimeMs": 880,
        "Exponent": -3,
        # "TempUnitGtEnumSymbol": "ec14bd47",
        "TempUnit": "Celcius",
        "TelemetryNameGtEnumSymbol": "WaterTempCTimes1000",
        "TelemetryName": "",
        "DisplayName": "Simulated GridWorks high precision water temp sensor",
        "CommsMethod": "SassyMQ",
        "TypeName": "simple.temp.sensor.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("SimpleTempSensorCacGt", d, SimpleTempSensorCacGt)])
