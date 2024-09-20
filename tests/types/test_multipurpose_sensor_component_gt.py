"""Tests multipurpose.sensor.component.gt type, version 000"""

from gwproto.data_classes.components import MultipurposeSensorComponent
from gwproto.types import MultipurposeSensorComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_multipurpose_sensor_component_gt_generated() -> None:
    d = {
        "ComponentId": "2ca9e65a-5e85-4eaa-811b-901e940f8d09",
        "ComponentAttributeClassId": "432073b8-4d2b-4e36-9229-73893f33f846",
        "ChannelList": [1],
        "ConfigList": [
            {
                "ReportOnChange": False,
                "Exponent": 3,
                "AboutNodeName": "a.distsourcewater.temp",
                "SamplePeriodS": 60,
                "TypeName": "telemetry.reporting.config",
                "Version": "000",
                "Unit": "Celcius",
                "TelemetryName": "WaterTempCTimes1000",
            }
        ],
        "HwUid": "a4f",
        "DisplayName": "TSnap for Almond",
        "TypeName": "multipurpose.sensor.component.gt",
        "Version": "000",
    }
    assert_component_load(
        [
            ComponentCase(
                "MultipurposeSensorComponentGt",
                d,
                MultipurposeSensorComponentGt,
                MultipurposeSensorComponent,
            )
        ]
    )
