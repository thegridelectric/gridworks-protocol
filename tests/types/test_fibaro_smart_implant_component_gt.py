"""Tests fibaro.smart.implant.component.gt type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types.fibaro_smart_implant_component_gt import FibaroSmartImplantComponentGt_Maker as Maker


def test_fibaro_smart_implant_component_gt_generated() -> None:
    ...

    # d = {
    #     "ComponentId": ,
    #     "ComponentAttributeClassId": ,
    #     "ZWaveDSK": ,
    #     "DisplayName": ,
    #     "HwUid": ,
    #     "TypeName": "fibaro.smart.implant.component.gt",
    #     "Version": "000",
    # }

    # with pytest.raises(SchemaError):
    #     Maker.type_to_tuple(d)

    # with pytest.raises(SchemaError):
    #     Maker.type_to_tuple('"not a dict"')

    # # Test type_to_tuple
    # gtype = json.dumps(d)
    # gtuple = Maker.type_to_tuple(gtype)

    # # test type_to_tuple and tuple_to_type maps
    # assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # # test Maker init
    # t = Maker(
    #     component_id=gtuple.ComponentId,
    #     component_attribute_class_id=gtuple.ComponentAttributeClassId,
    #     z_wave_d_s_k=gtuple.ZWaveDSK,
    #     display_name=gtuple.DisplayName,
    #     hw_uid=gtuple.HwUid,

    # ).tuple
    # assert t == gtuple

    # ######################################
    # # Dataclass related tests
    # ######################################

    # dc = Maker.tuple_to_dc(gtuple)
    # assert gtuple == Maker.dc_to_tuple(dc)
    # assert Maker.type_to_dc(Maker.dc_to_type(dc)) == dc

    # ######################################
    # # SchemaError raised if missing a required attribute
    # ######################################

    # d2 = dict(d)
    # del d2["TypeName"]
    # with pytest.raises(SchemaError):
    #     Maker.dict_to_tuple(d2)

    # d2 = dict(d)
    # del d2["ComponentId"]
    # with pytest.raises(SchemaError):
    #     Maker.dict_to_tuple(d2)

    # d2 = dict(d)
    # del d2["ComponentAttributeClassId"]
    # with pytest.raises(SchemaError):
    #     Maker.dict_to_tuple(d2)

    # d2 = dict(d)
    # del d2["ZWaveDSK"]
    # with pytest.raises(SchemaError):
    #     Maker.dict_to_tuple(d2)

    # ######################################
    # # Optional attributes can be removed from type
    # ######################################

    # d2 = dict(d)
    # if "DisplayName" in d2.keys():
    #     del d2["DisplayName"]
    # Maker.dict_to_tuple(d2)

    # d2 = dict(d)
    # if "HwUid" in d2.keys():
    #     del d2["HwUid"]
    # Maker.dict_to_tuple(d2)

    # ######################################
    # # Behavior on incorrect types
    # ######################################

    # ######################################
    # # SchemaError raised if TypeName is incorrect
    # ######################################

    # d2 = dict(d, TypeName="not the type name")
    # with pytest.raises(ValidationError):
    #     Maker.dict_to_tuple(d2)

    # ######################################
    # # SchemaError raised if primitive attributes do not have appropriate property_format
    # ######################################

    # d2 = dict(d, ComponentId="d4be12d5-33ba-4f1f-b9e5")
    # with pytest.raises(ValidationError):
    #     Maker.dict_to_tuple(d2)

    # d2 = dict(d, ComponentAttributeClassId="d4be12d5-33ba-4f1f-b9e5")
    # with pytest.raises(ValidationError):
    #     Maker.dict_to_tuple(d2)

    # # End of Test
