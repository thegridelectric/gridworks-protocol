"""Tests electric.meter.component.gt type, version 000"""

from gwproto.data_classes.components import ElectricMeterComponent
from gwproto.types import ElectricMeterComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_electric_meter_component_gt_generated() -> None:
    d = {
        "ComponentId": "2dfb0cb6-6015-4273-b02b-bd446cc785d7",
        "ComponentAttributeClassId": "204832ef-0c88-408b-9640-264d2ee74914",
        "DisplayName": "EGauge Power Meter",
        "ConfigList": [
            {
                "AboutNodeName": "a.m.hp.outdoor.power",
                "ReportOnChange": True,
                "SamplePeriodS": 300,
                "Exponent": 0,
                "AsyncReportThreshold": 0.02,
                "NameplateMaxValue": 3500,
                "TypeName": "telemetry.reporting.config",
                "Version": "000",
                "TelemetryName": "PowerW",
                "Unit": "W",
            }
        ],
        "HwUid": "BP01349",
        "ModbusHost": "eGauge6069.local",
        "ModbusPort": 502,
        "EgaugeIoList": [
            {
                "InputConfig": {
                    "Address": 9006,
                    "Name": "",
                    "Description": "change in value",
                    "Type": "f32",
                    "Denominator": 1,
                    "Unit": "W",
                    "TypeName": "egauge.register.config",
                    "Version": "000",
                },
                "OutputConfig": {
                    "AboutNodeName": "a.m.hp.outdoor.power",
                    "ReportOnChange": True,
                    "SamplePeriodS": 300,
                    "Exponent": 0,
                    "AsyncReportThreshold": 0.02,
                    "NameplateMaxValue": 3500,
                    "TypeName": "telemetry.reporting.config",
                    "Version": "000",
                    "TelemetryName": "PowerW",
                    "Unit": "W",
                },
                "TypeName": "egauge.io",
                "Version": "000",
            }
        ],
        "TypeName": "electric.meter.component.gt",
        "Version": "000",
    }
    assert_component_load(
        [
            ComponentCase(
                "ElectricMeterComponentGt",
                d,
                ElectricMeterComponentGt,
                ElectricMeterComponent,
            )
        ]
    )
