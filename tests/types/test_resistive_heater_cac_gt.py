"""Tests resistive.heater.cac.gt type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import MakeModel
from gwproto.types import ResistiveHeaterCacGt
from gwproto.types import ResistiveHeaterCacGtMaker as Maker
from pydantic import ValidationError


def test_resistive_heater_cac_gt_generated() -> None:
    t = ResistiveHeaterCacGt(
        component_attribute_class_id="cf1f2587-7462-4701-b962-d2b264744c1d",
        make_model=MakeModel.UNKNOWNMAKE__UNKNOWNMODEL,
        display_name="Fake Boost Element",
        nameplate_max_power_w=4500,
        rated_voltage_v=240,
    )

    d = {
        "ComponentAttributeClassId": "cf1f2587-7462-4701-b962-d2b264744c1d",
        "MakeModelGtEnumSymbol": "00000000",
        "DisplayName": "Fake Boost Element",
        "NameplateMaxPowerW": 4500,
        "RatedVoltageV": 240,
        "TypeName": "resistive.heater.cac.gt",
        "Version": "000",
    }

    assert t.as_dict() == d

    d2 = d.copy()

    del d2["MakeModelGtEnumSymbol"]
    d2["MakeModel"] = MakeModel.UNKNOWNMAKE__UNKNOWNMODEL.value
    assert t == Maker.dict_to_tuple(d2)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple(d)

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)
    assert gtuple == t

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    ######################################
    # Dataclass related tests
    ######################################

    dc = Maker.tuple_to_dc(gtuple)
    assert gtuple == Maker.dc_to_tuple(dc)
    assert Maker.type_to_dc(Maker.dc_to_type(dc)) == dc

    ######################################
    # GwTypeError raised if missing a required attribute
    ######################################

    d2 = d.copy()
    del d2["TypeName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ComponentAttributeClassId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["MakeModelGtEnumSymbol"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["NameplateMaxPowerW"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["RatedVoltageV"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, MakeModelGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).make_model == MakeModel.default()

    d2 = dict(d, NameplateMaxPowerW="4500.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RatedVoltageV="240.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ComponentAttributeClassId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RatedVoltageV=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
