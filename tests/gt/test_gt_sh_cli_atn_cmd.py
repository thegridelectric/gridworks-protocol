"""Tests gt.sh.cli.atn.cmd type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.errors import SchemaError
from gwproto.messages import GtShCliAtnCmd
from gwproto.messages import GtShCliAtnCmd_Maker as Maker


def test_gt_sh_cli_atn_cmd_generated():

    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1",
        "SendSnapshot": True,
        "FromGNodeId": "e7f7d6cc-08b0-4b36-bbbb-0a1f8447fd32",
        "TypeAlias": "gt.sh.cli.atn.cmd",
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
        from_g_node_alias=gw_tuple.FromGNodeAlias,
        send_snapshot=gw_tuple.SendSnapshot,
        from_g_node_id=gw_tuple.FromGNodeId,
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
    del d2["FromGNodeAlias"]
    with pytest.raises(ValidationError):
        GtShCliAtnCmd(**d2)

    d2 = dict(d)
    del d2["SendSnapshot"]
    with pytest.raises(ValidationError):
        GtShCliAtnCmd(**d2)

    d2 = dict(d)
    del d2["FromGNodeId"]
    with pytest.raises(ValidationError):
        GtShCliAtnCmd(**d2)
    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, FromGNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SendSnapshot="This string is not a boolean.")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeId={})
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

    d2 = dict(d, FromGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
