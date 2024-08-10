from gwproto.data_classes.cacs.electric_meter_cac import ElectricMeterCac
from gwproto.data_classes.hardware_layout import HardwareLayout
from gwproto.types import ElectricMeterCacGt_Maker

# Running the below disrupts other tests. Need to set up the
# test isolation as per scada


def test_electric_meter_cac():
    HardwareLayout.load("tests/config/hardware-layout.json")
    d = {
        "ComponentAttributeClassId": "28897ac1-ea42-4633-96d3-196f63f5a951",
        "MakeModelGtEnumSymbol": "076da322",
        "DisplayName": "Gridworks Pm1 Simulated Power Meter",
        "InterfaceGtEnumSymbol": "efc144cd",
        "PollPeriodMs": 1000,
        "TelemetryNameList": ["af39eec9"],
        "TypeName": "electric.meter.cac.gt",
        "Version": "000",
    }

    gw_tuple = ElectricMeterCacGt_Maker.dict_to_tuple(d)
    assert gw_tuple.ComponentAttributeClassId in ElectricMeterCac.by_id.keys()
    dc = ElectricMeterCac.by_id[gw_tuple.ComponentAttributeClassId]

    assert dc.__repr__() == "GRIDWORKS__SIMPM1 Gridworks Pm1 Simulated Power Meter"
