from gwproto.types import ElectricMeterCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_electric_meter_cac() -> None:
    d = {
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "DefaultBaud": 9600,
        "DisplayName": "EGauge 4030",
        "MakeModel": "EGAUGE__4030",
        "MinPollPeriodMs": 1000,
        "TelemetryNameList": [
            "PowerW",
            "MilliWattHours",
            "VoltageRmsMilliVolts",
            "CurrentRmsMicroAmps",
            "FrequencyMicroHz",
        ],
        "TypeName": "electric.meter.cac.gt",
        "Version": "001",
    }
    assert_cac_load([CacCase("ElectricMeterCac", d, ElectricMeterCacGt)])
