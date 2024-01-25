"""Tests batched.readings type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import BatchedReadings_Maker as Maker


def test_batched_readings_generated() -> None:
    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeInstanceId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "AboutGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta",
        "SlotStartUnixS": 1656945300,
        "BatchedTransmissionPeriodS": 300,
        "ChannelReadingList": ,
        "BooleanactuatorCmdList": [ { "ShNodeAlias": "a.elt1.relay", "RelayStateCommandList": [1], "CommandTimeUnixMsList": [1656945413464], "TypeName": "gt.sh.booleanactuator.cmd.status", "Version": "100", } ],
        "TypeName": "batched.readings",
        "Version": "000",
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
        from_g_node_alias=gtuple.FromGNodeAlias,
        from_g_node_instance_id=gtuple.FromGNodeInstanceId,
        about_g_node_alias=gtuple.AboutGNodeAlias,
        slot_start_unix_s=gtuple.SlotStartUnixS,
        batched_transmission_period_s=gtuple.BatchedTransmissionPeriodS,
        channel_reading_list=gtuple.ChannelReadingList,
        booleanactuator_cmd_list=gtuple.BooleanactuatorCmdList,
        
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
    del d2["FromGNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FromGNodeInstanceId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AboutGNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SlotStartUnixS"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["BatchedTransmissionPeriodS"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ChannelReadingList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["BooleanactuatorCmdList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, SlotStartUnixS="1656945300.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, BatchedTransmissionPeriodS="300.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, ChannelReadingList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, ChannelReadingList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, ChannelReadingList= [{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, BooleanactuatorCmdList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, BooleanactuatorCmdList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, BooleanactuatorCmdList= [{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, FromGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeInstanceId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AboutGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SlotStartUnixS=32503683600)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
