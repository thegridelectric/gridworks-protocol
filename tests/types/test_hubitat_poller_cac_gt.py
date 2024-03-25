"""Tests hubitat.poller.cac.gt type, version 000"""

import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import HubitatPollerCacGt_Maker as Maker


def test_hubitat_poller_cac_gt_generated() -> None:
    ...
    # d = {
    #     "TypeName": "hubitat.poller.cac.gt",
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
    # t = Maker().tuple
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

    # ######################################
    # # Behavior on incorrect types
    # ######################################

    # ######################################
    # # SchemaError raised if TypeName is incorrect
    # ######################################

    # d2 = dict(d, TypeName="not the type name")
    # with pytest.raises(ValidationError):
    #     Maker.dict_to_tuple(d2)
