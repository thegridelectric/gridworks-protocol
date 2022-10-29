"""Tests gt.sh.booleanactuator.cmd.status type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.errors import SchemaError
from gwproto.messages import GtShBooleanactuatorCmdStatus
from gwproto.messages import GtShBooleanactuatorCmdStatus_Maker as Maker


def test_gt_sh_booleanactuator_cmd_status_generated():

    d = {
        "ShNodeAlias": "a.elt1.relay",
        "RelayStateCommandList": [0],
        "CommandTimeUnixMsList": [1656443704800],
        "TypeAlias": "gt.sh.booleanactuator.cmd.status",
    }

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gw_type = json.dumps(d)
    gw_tuple = Maker.type_to_tuple(gw_type)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple

    # test Maker init
    payload = Maker(
        sh_node_alias=gw_tuple.ShNodeAlias,
        relay_state_command_list=gw_tuple.RelayStateCommandList,
        command_time_unix_ms_list=gw_tuple.CommandTimeUnixMsList,
        #
    ).tuple
    assert payload == gw_tuple

    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ShNodeAlias"]
    with pytest.raises(ValidationError):
        GtShBooleanactuatorCmdStatus(**d2)

    d2 = dict(d)
    del d2["RelayStateCommandList"]
    with pytest.raises(ValidationError):
        GtShBooleanactuatorCmdStatus(**d2)

    d2 = dict(d)
    del d2["CommandTimeUnixMsList"]
    with pytest.raises(ValidationError):
        GtShBooleanactuatorCmdStatus(**d2)
    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, ShNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayStateCommandList=["1.1"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CommandTimeUnixMsList=["1.1"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeAlias="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ShNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayStateCommandList=[2])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CommandTimeUnixMsList=[1656245000])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
