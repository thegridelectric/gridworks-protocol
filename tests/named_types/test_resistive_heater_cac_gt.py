"""Tests resistive.heater.cac.gt type, version 001"""

from gwproto.named_types import ResistiveHeaterCacGt


def test_resistive_heater_cac_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "cf1f2587-7462-4701-b962-d2b264744c1d",
        "MakeModel": "UNKNOWNMAKE__UNKNOWNMODEL",
        "DisplayName": "Fake Boost Element",
        "MinPollPeriodMs": 1000,
        "NameplateMaxPowerW": 4500,
        "RatedVoltageV": 240,
        "TypeName": "resistive.heater.cac.gt",
        "Version": "001",
    }

    d2 = ResistiveHeaterCacGt.from_dict(d).to_dict()
    assert d2 == d
