# Running the below disrupts other tests. Need to set up the
# test isolation as per scada


def test_electric_meter_component():
    ...
    # HardwareLayout.load("tests/config/hardware-layout.json")
    # d = {
    #     "ComponentId": "2bfd0036-0b0e-4732-8790-bc7d0536a85e",
    #     "ComponentAttributeClassId": "28897ac1-ea42-4633-96d3-196f63f5a951",
    #     "DisplayName": "Power Meter for Simulated Test system",
    #     "ConfigList": [
    #         {
    #             "ChannelName": "elt1-pwr",
    #             "PollPeriodMs": 1000,
    #             "CapturePeriodS": 300,
    #             "AsyncCapture": True,
    #             "SamplePeriodS": 300,
    #             "Exponent": 0,
    #             "AsyncReportThreshold": 0.02,
    #             "NameplateMaxValue": 4500,
    #             "TypeName": "telemetry.reporting.config",
    #             "Version": "000",
    #             "TelemetryNameGtEnumSymbol": "af39eec9",
    #             "UnitGtEnumSymbol": "f459a9c3",
    #         },
    #         {
    #             "AboutNodeName": "a.elt2",
    #             "ReportOnChange": True,
    #             "SamplePeriodS": 300,
    #             "Exponent": 0,
    #             "AsyncReportThreshold": 0.02,
    #             "NameplateMaxValue": 4500,
    #             "TypeName": "telemetry.reporting.config",
    #             "Version": "000",
    #             "TelemetryNameGtEnumSymbol": "af39eec9",
    #             "UnitGtEnumSymbol": "f459a9c3",
    #         },
    #     ],
    #     "HwUid": "9999",
    #     "EgaugeIoList": [],
    #     "TypeName": "electric.meter.component.gt",
    #     "Version": "000",
    # }

    # gw_tuple = ElectricMeterComponentGtMaker.dict_to_tuple(d)
    # # assert gw_tuple.component_id in ElectricMeterComponent.by_id.keys()
    # # component_as_dc = ElectricMeterComponent.by_id[gw_tuple.component_id]
    # assert gw_tuple.HwUid == "9999"
    # # assert component_as_dc.hw_uid == "1001ab"
