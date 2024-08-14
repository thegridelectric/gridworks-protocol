"""Tests resistive.heater.component.gt type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import MakeModel
from gwproto.types import ComponentAttributeClassGt as CacGt
from gwproto.types import ComponentAttributeClassGtMaker as CacMaker
from gwproto.types.resistive_heater_component_gt import ResistiveHeaterComponentGt
from gwproto.types.resistive_heater_component_gt import (
    ResistiveHeaterComponentGtMaker as Maker,
)
from pydantic import ValidationError

from tests.utils import flush_all


def test_resistive_heater_component_gt_generated() -> None:
    flush_all()
    cac_gt = CacGt(
        component_attribute_class_id="cf1f2587-7462-4701-b962-d2b264744c1d",
        make_model=MakeModel.UNKNOWNMAKE__UNKNOWNMODEL,
    )
    CacMaker.tuple_to_dc(cac_gt)
    t = ResistiveHeaterComponentGt(
        component_id="80f95280-e999-49e0-a0e4-a7faf3b5b3bd",
        component_attribute_class_id="cf1f2587-7462-4701-b962-d2b264744c1d",
        display_name="First 4.5 kW boost in tank",
        hw_uid="aaaa2222",
        tested_max_hot_milli_ohms=13714,
        tested_max_cold_milli_ohms=14500,
        config_list=[],
    )

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

    assert t.as_dict() == d

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
    del d2["ComponentId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ComponentAttributeClassId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "HwUid" in d2.keys():
        del d2["HwUid"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "TestedMaxHotMilliOhms" in d2.keys():
        del d2["TestedMaxHotMilliOhms"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "TestedMaxColdMilliOhms" in d2.keys():
        del d2["TestedMaxColdMilliOhms"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TestedMaxHotMilliOhms="13714.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TestedMaxColdMilliOhms="14500.1")
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

    d2 = dict(d, ComponentId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
