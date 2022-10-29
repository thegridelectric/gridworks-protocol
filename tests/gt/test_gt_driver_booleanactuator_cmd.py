"""Tests gt.driver.booleanactuator.cmd type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.errors import SchemaError
from gwproto.messages import GtDriverBooleanactuatorCmd
from gwproto.messages import GtDriverBooleanactuatorCmd_Maker as Maker


def test_gt_driver_booleanactuator_cmd_generated():

    d = {
        "RelayState": 0,
        "ShNodeAlias": "a.elt1.relay",
        "CommandTimeUnixMs": 1656869326637,
        "TypeAlias": "gt.driver.booleanactuator.cmd",
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
        relay_state=gw_tuple.RelayState,
        sh_node_alias=gw_tuple.ShNodeAlias,
        command_time_unix_ms=gw_tuple.CommandTimeUnixMs,
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
    del d2["RelayState"]
    with pytest.raises(ValidationError):
        GtDriverBooleanactuatorCmd(**d2)

    d2 = dict(d)
    del d2["ShNodeAlias"]
    with pytest.raises(ValidationError):
        GtDriverBooleanactuatorCmd(**d2)

    d2 = dict(d)
    del d2["CommandTimeUnixMs"]
    with pytest.raises(ValidationError):
        GtDriverBooleanactuatorCmd(**d2)
    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, RelayState="0.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayState="0")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, RelayState=0.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, ShNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CommandTimeUnixMs="1656869326637.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CommandTimeUnixMs="1656869326637")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, CommandTimeUnixMs=1656869326637.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeAlias="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, RelayState=2)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ShNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CommandTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
