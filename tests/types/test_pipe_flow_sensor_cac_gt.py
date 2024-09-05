"""Tests pipe.flow.sensor.cac.gt type, version 000"""

from gwproto.types import PipeFlowSensorCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_pipe_flow_sensor_cac_gt_load() -> None:
    d = {
        "ComponentAttributeClassId": "14e7105a-e797-485a-a304-328ecc85cd98",
        # "MakeModelGtEnumSymbol": "d0b0e375",
        "MakeModel": "ATLAS__EZFLO",
        "DisplayName": "EZFLO for a.tank.out",
        "CommsMethod": "I2C",
        "TypeName": "pipe.flow.sensor.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("PipeFlowSensorCacGt", d, PipeFlowSensorCacGt)])
