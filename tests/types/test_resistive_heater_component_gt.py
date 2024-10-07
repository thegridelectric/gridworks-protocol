"""Tests resistive.heater.component.gt type, version 000"""

from gwproto.data_classes.components import ResistiveHeaterComponent
from gwproto.types import ResistiveHeaterComponentGt
from tests.component_load_utils import ComponentCase, assert_component_load


def test_resistive_heater_component_gt_generated() -> None:
    d = {
        "ComponentId": "80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        "ComponentAttributeClassId": "cf1f2587-7462-4701-b962-d2b264744c1d",
        "DisplayName": "First 4.5 kW boost in tank",
        "HwUid": "aaaa2222",
        "ConfigList": [],
        "TestedMaxHotMilliOhms": 13714,
        "TestedMaxColdMilliOhms": 14500,
        "TypeName": "resistive.heater.component.gt",
        "Version": "001",
    }
    assert_component_load(
        [
            ComponentCase(
                "ResistiveHeaterComponentGt",
                d,
                ResistiveHeaterComponentGt,
                ResistiveHeaterComponent,
            )
        ],
    )
