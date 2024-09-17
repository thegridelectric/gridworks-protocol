"""Tests resistive.heater.component.gt type, version 000"""

from gwproto.types.resistive_heater_component_gt import ResistiveHeaterComponentGt


def test_resistive_heater_component_gt_generated() -> None:
    d = {
        "ComponentId": "80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        "ComponentAttributeClassId": "cf1f2587-7462-4701-b962-d2b264744c1d",
        "DisplayName": "First 4.5 kW boost in tank",
        "HwUid": "aaaa2222",
        "TestedMaxHotMilliOhms": 13714,
        "TestedMaxColdMilliOhms": 14500,
        "ConfigList": [],
        "TypeName": "resistive.heater.component.gt",
        "Version": "000",
    }

    t = ResistiveHeaterComponentGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d
