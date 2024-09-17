"""Tests resistive.heater.cac.gt type, version 001"""

from gwproto.enums import MakeModel
from gwproto.types import ResistiveHeaterCacGt


def test_resistive_heater_cac_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "cf1f2587-7462-4701-b962-d2b264744c1d",
        "MakeModel": "UNKNOWNMAKE__UNKNOWNMODEL",
        "DisplayName": "Fake Boost Element",
        "MinPollPeriodMs": ,
        "NameplateMaxPowerW": 4500,
        "RatedVoltageV": 240,
        "TypeName": "resistive.heater.cac.gt",
        "Version": "001",
    }

    t = ResistiveHeaterCacGt(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, MakeModel="unknown_enum_thing")
    assert ResistiveHeaterCacGt(**d2).make_model == MakeModel.default()
