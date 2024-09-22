"""Tests multipurpose.sensor.cac.gt type, version 000"""

from gwproto.types import MultipurposeSensorCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_multipurpose_sensor_cac_gt_load() -> None:
    d = {
        "ComponentAttributeClassId": "432073b8-4d2b-4e36-9229-73893f33f846",
        "MakeModel": "GRIDWORKS__MULTITEMP1",
        "PollPeriodMs": 880,
        "Exponent": -3,
        "TempUnit": "Celcius",
        "TelemetryNameList": ["WaterTempCTimes1000"],
        "MaxThermistors": 12,
        "DisplayName": "Simulated GridWorks high precision water temp sensor",
        "CommsMethod": "I2C",
        "TypeName": "multipurpose.sensor.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("MultipurposeSensorCacGt", d, MultipurposeSensorCacGt)])
