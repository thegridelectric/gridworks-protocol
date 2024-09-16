"""Tests pipe.flow.sensor.component.gt type, version 000"""

from gwproto.data_classes.components import PipeFlowSensorComponent
from gwproto.types import PipeFlowSensorComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_pipe_flow_sensor_component_gt_generated() -> None:
    d = {
        "ComponentId": "dd5ac673-91a8-40e2-a233-b67479cec709",
        "ComponentAttributeClassId": "14e7105a-e797-485a-a304-328ecc85cd98",
        "I2cAddress": 100,
        "ConversionFactor": 0.1328,
        "DisplayName": "Flow meter on pipe out of tank",
        "HwUid": "1234",
        "ExpectedMaxGpmTimes100": 1000,
        "TypeName": "pipe.flow.sensor.component.gt",
        "Version": "000",
    }
    assert_component_load(
        [
            ComponentCase(
                "PipeFlowSensorComponentGt",
                d,
                PipeFlowSensorComponentGt,
                PipeFlowSensorComponent,
            )
        ]
    )
