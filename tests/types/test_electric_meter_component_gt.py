"""Tests electric.meter.component.gt type, version 001"""

from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGt


def test_electric_meter_component_gt_generated() -> None:
    d = {
        "ComponentId": "04ceb282-d7e8-4293-80b5-72455e1a5db3",
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "DisplayName": "Main power meter for Little orange house garage space heat",
        "ConfigList": ,
        "HwUid": "35941_308",
        "ModbusHost": "eGauge4922.local",
        "ModbusPort": 502,
        "EgaugeIoList": ,
        "TypeName": "electric.meter.component.gt",
        "Version": "001",
    }

    t = ElectricMeterComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
