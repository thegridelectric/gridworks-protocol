"""Tests batched.readings type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
from gwproto.types import BatchedReadings
from gwproto.types import BatchedReadings_Maker as Maker
from gwproto.types import ChannelReadings
from gwproto.types import DataChannelGt


def test_batched_readings_generated() -> None:
    t = BatchedReadings(
        FromGNodeAlias="d1.isone.ct.newhaven.rose.scada",
        FromGNodeInstanceId="9479051a-55fd-4da7-b14f-746853d70357",
        AboutGNodeAlias="d1.isone.ct.newhaven.rose.ta",
        SlotStartUnixS=1710010410,
        BatchedTransmissionPeriodS=30,
        DataChannelList=[
            DataChannelGt(
                Name="hp-idu-pwr",
                DisplayName="Hp IDU",
                AboutNodeName="hp-idu-pwr",
                CapturedByNodeName="s.pwr-meter",
                TelemetryName=TelemetryName.PowerW,
                Id="50cf426b-ff3f-4a30-8415-8d3fba5e0ab7",
            )
        ],
        ChannelReadingList=[
            ChannelReadings(
                ChannelId="50cf426b-ff3f-4a30-8415-8d3fba5e0ab7",
                ValueList=[1220, 1400],
                ScadaReadTimeUnixMsList=[1_710_010_425_545, 1_710_010_438_720],
            )
        ],
        FsmActionList=[],
        FsmReportList=[],
        Id="aa3dc3d6-3ef5-4b1f-8c3f-c9a4ef15195e",
    )
    d = {
        "FromGNodeAlias": "d1.isone.ct.newhaven.rose.scada",
        "FromGNodeInstanceId": "9479051a-55fd-4da7-b14f-746853d70357",
        "AboutGNodeAlias": "d1.isone.ct.newhaven.rose.ta",
        "SlotStartUnixS": 1710010410,
        "BatchedTransmissionPeriodS": 30,
        "DataChannelList": [
            {
                "Name": "hp-idu-pwr",
                "DisplayName": "Hp IDU",
                "AboutNodeName": "hp-idu-pwr",
                "CapturedByNodeName": "s.pwr-meter",
                "Id": "50cf426b-ff3f-4a30-8415-8d3fba5e0ab7",
                "TypeName": "data.channel.gt",
                "Version": "000",
                "TelemetryNameGtEnumSymbol": "af39eec9",
            }
        ],
        "ChannelReadingList": [
            {
                "ChannelId": "50cf426b-ff3f-4a30-8415-8d3fba5e0ab7",
                "ValueList": [1220, 1400],
                "ScadaReadTimeUnixMsList": [1710010425545, 1710010438720],
                "TypeName": "channel.readings",
                "Version": "000",
            }
        ],
        "FsmActionList": [],
        "FsmReportList": [],
        "Id": "aa3dc3d6-3ef5-4b1f-8c3f-c9a4ef15195e",
        "TypeName": "batched.readings",
        "Version": "000",
    }

    assert t.as_dict() == d

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)
    assert gtuple == t

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

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
    del d2["DataChannelList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ChannelReadingList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FsmActionList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["FsmReportList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Id"]
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

    d2 = dict(d, DataChannelList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, DataChannelList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, DataChannelList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ChannelReadingList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ChannelReadingList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ChannelReadingList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FsmActionList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FsmActionList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FsmActionList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FsmReportList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FsmReportList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FsmReportList=[{"Failed": "Not a GtSimpleSingleStatus"}])
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

    d2 = dict(d, BatchedTransmissionPeriodS=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Id="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
