"""Tests multipurpose.sensor.cac.gt type, version 000"""

from gwproto.types import MultipurposeSensorCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_multipurpose_sensor_cac_gt_load() -> None:
    d = {
        "ComponentAttributeClassId": "8a1a1538-ed2d-4829-9c03-f9be1c9f9c83",
        # "MakeModelGtEnumSymbol": "09185ae3",
        "MakeModel": "GRIDWORKS__MULTITEMP1",
        "PollPeriodMs": 880,
        "Exponent": -3,
        # "TempUnitGtEnumSymbol": "8e6dd6dd",
        "TempUnit": "Celcius",
        # "TelemetryNameList": ["22641963"],
        "TelemetryNameList": ["WaterTempCTimes1000"],
        "MaxThermistors": 12,
        "DisplayName": "Simulated GridWorks high precision water temp sensor",
        "CommsMethod": "I2C",
        "TypeName": "multipurpose.sensor.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("MultipurposeSensorCacGt", d, MultipurposeSensorCacGt)])
