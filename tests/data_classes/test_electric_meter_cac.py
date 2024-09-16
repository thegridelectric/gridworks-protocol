from gwproto.types import ElectricMeterCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_electric_meter_cac() -> None:
    d = {
        "ComponentAttributeClassId": "28897ac1-ea42-4633-96d3-196f63f5a951",
        "MakeModel": "GRIDWORKS__SIMPM1",
        "DisplayName": "Gridworks Pm1 Simulated Power Meter",
        "Interface": "SIMRABBIT",
        "PollPeriodMs": 1000,
        "TelemetryNameList": ["PowerW"],
        "TypeName": "electric.meter.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("ElectricMeterCac", d, ElectricMeterCacGt)])
