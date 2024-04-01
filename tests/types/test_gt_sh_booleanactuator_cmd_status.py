"""Tests gt.sh.booleanactuator.cmd.status type, version 100"""

import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import GtShBooleanactuatorCmdStatus_Maker as Maker


def test_gt_sh_booleanactuator_cmd_status_generated() -> None:
    d = {
        "ShNodeAlias": "a.elt1.relay",
        "RelayStateCommandList": [0],
        "CommandTimeUnixMsList": [1656443704800],
        "TypeName": "gt.sh.booleanactuator.cmd.status",
        "Version": "100",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # test Maker init
    t = Maker(
        sh_node_alias=gtuple.ShNodeAlias,
        relay_state_command_list=gtuple.RelayStateCommandList,
        command_time_unix_ms_list=gtuple.CommandTimeUnixMsList,
    ).tuple
    assert t == gtuple

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ShNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RelayStateCommandList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["CommandTimeUnixMsList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ShNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CommandTimeUnixMsList=[1656245000])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
