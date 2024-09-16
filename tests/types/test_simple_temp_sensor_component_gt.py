"""Tests simple.temp.sensor.component.gt type, version 000"""

from gwproto.data_classes.components import SimpleTempSensorComponent
from gwproto.types import SimpleTempSensorComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_simple_temp_sensor_component_gt_generated() -> None:
    d = {
        "ComponentId": "2ca9e65a-5e85-4eaa-811b-901e940f8d09",
        "ComponentAttributeClassId": "8a1a1538-ed2d-4829-9c03-f9be1c9f9c83",
        "DisplayName": "Temp sensor on pipe out of tank",
        "HwUid": "00033ffe",
        "Channel": 0,
        "TypeName": "simple.temp.sensor.component.gt",
        "Version": "000",
    }
    assert_component_load(
        [
            ComponentCase(
                "SimpleTempSensorComponentGt",
                d,
                SimpleTempSensorComponentGt,
                SimpleTempSensorComponent,
            )
        ],
    )
