"""Tests resistive.heater.cac.gt type, version 000"""

from gwproto.types import ResistiveHeaterCacGt
from tests.cac_load_utils import CacCase, assert_cac_load


def test_resistive_heater_cac_gt_load() -> None:
    d = {
        "ComponentAttributeClassId": "cf1f2587-7462-4701-b962-d2b264744c1d",
        # "MakeModelGtEnumSymbol": "00000000",
        "MakeModel": "UNKNOWNMAKE__UNKNOWNMODEL",
        "DisplayName": "Fake Boost Element",
        "NameplateMaxPowerW": 4500,
        "RatedVoltageV": 240,
        "TypeName": "resistive.heater.cac.gt",
        "Version": "000",
    }
    assert_cac_load([CacCase("ResistiveHeaterCacGt", d, ResistiveHeaterCacGt)])
