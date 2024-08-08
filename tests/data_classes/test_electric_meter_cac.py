from gwproto.types import ElectricMeterCacGtMaker

# Running the below disrupts other tests. Need to set up the
# test isolation as per scada


def test_electric_meter_cac():
    # HardwareLayout.load("tests/config/hardware-layout.json")
    d = {
        "ComponentAttributeClassId": "28897ac1-ea42-4633-96d3-196f63f5a951",
        "MakeModelGtEnumSymbol": "076da322",
        "DisplayName": "Gridworks Pm1 Simulated Power Meter",
        "InterfaceGtEnumSymbol": "efc144cd",
        "MinPollPeriodMs": 1000,
        "TelemetryNameList": ["af39eec9"],
        "TypeName": "electric.meter.cac.gt",
        "Version": "000",
    }

    gw_tuple = ElectricMeterCacGtMaker.dict_to_tuple(d)
    # assert gw_tuple.component_attribute_class_id in ElectricMeterCac.by_id.keys()
    # dc = ElectricMeterCac.by_id[gw_tuple.component_attribute_class_id]

    # assert dc.repr() == "GRIDWORKS__SIMPM1 Gridworks Pm1 Simulated Power Meter"
