"""Tests fsm.full.report type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import FsmFullReport
from gwproto.types import FsmFullReport_Maker as Maker


# def test_fsm_full_report_generated() -> None:
#     t = FsmFullReport(
#         FromName="s",
#         TriggerId="12da4269-63c3-44f4-ab65-3ee5e29329fe",
#         AtomicList=,
#     )

#     d = {
#         "FromName": "admin",
#         "TriggerId": "12da4269-63c3-44f4-ab65-3ee5e29329fe",
#         "AtomicList": ,
#         "TypeName": "fsm.full.report",
#         "Version": "000",
#     }

#     assert t.as_dict() == d

#     with pytest.raises(SchemaError):
#         Maker.type_to_tuple(d)

#     with pytest.raises(SchemaError):
#         Maker.type_to_tuple('"not a dict"')

#     # Test type_to_tuple
#     gtype = json.dumps(d)
#     gtuple = Maker.type_to_tuple(gtype)
#     assert gtuple == t

#     # test type_to_tuple and tuple_to_type maps
#     assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

#     ######################################
#     # SchemaError raised if missing a required attribute
#     ######################################

#     d2 = dict(d)
#     del d2["TypeName"]
#     with pytest.raises(SchemaError):
#         Maker.dict_to_tuple(d2)

#     d2 = dict(d)
#     del d2["FromName"]
#     with pytest.raises(SchemaError):
#         Maker.dict_to_tuple(d2)

#     d2 = dict(d)
#     del d2["TriggerId"]
#     with pytest.raises(SchemaError):
#         Maker.dict_to_tuple(d2)

#     d2 = dict(d)
#     del d2["AtomicList"]
#     with pytest.raises(SchemaError):
#         Maker.dict_to_tuple(d2)

#     ######################################
#     # Behavior on incorrect types
#     ######################################

#     d2  = dict(d, AtomicList="Not a list.")
#     with pytest.raises(SchemaError):
#         Maker.dict_to_tuple(d2)

#     d2  = dict(d, AtomicList=["Not a list of dicts"])
#     with pytest.raises(SchemaError):
#         Maker.dict_to_tuple(d2)

#     d2  = dict(d, AtomicList= [{"Failed": "Not a GtSimpleSingleStatus"}])
#     with pytest.raises(SchemaError):
#         Maker.dict_to_tuple(d2)

#     ######################################
#     # SchemaError raised if TypeName is incorrect
#     ######################################

#     d2 = dict(d, TypeName="not the type name")
#     with pytest.raises(ValidationError):
#         Maker.dict_to_tuple(d2)

#     ######################################
#     # SchemaError raised if primitive attributes do not have appropriate property_format
#     ######################################

#     d2 = dict(d, FromName="A.hot-stuff")
#     with pytest.raises(ValidationError):
#         Maker.dict_to_tuple(d2)

#     d2 = dict(d, TriggerId="d4be12d5-33ba-4f1f-b9e5")
#     with pytest.raises(ValidationError):
#         Maker.dict_to_tuple(d2)
