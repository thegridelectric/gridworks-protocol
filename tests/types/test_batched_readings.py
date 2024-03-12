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
        FromGNodeInstanceId="0384ef21-648b-4455-b917-58a1172d7fc1",
        AboutGNodeAlias="d1.isone.ct.newhaven.rose.scada.ta",
        SlotStartUnixS=1710116340,
        BatchedTransmissionPeriodS=30,
        DataChannelList=[
            DataChannelGt(
                Name="hp-ewt",
                DisplayName="HP EWT",
                AboutNodeName="hp-ewt",
                CapturedByNodeName="analog-temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
                Id="4693a282-9b9f-4d35-a060-92aa0d0a29aa",
            ),
            DataChannelGt(
                Name="hp-lwt",
                DisplayName="HP LWT",
                AboutNodeName="hp-lwt",
                CapturedByNodeName="analog-temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
                Id="6eae748c-a618-4f72-8e42-cff6ef578b3e",
            ),
        ],
        ChannelReadingList=[
            ChannelReadings(
                ChannelId="4693a282-9b9f-4d35-a060-92aa0d0a29aa",
                ValueList=[48320, 49100],
                ScadaReadTimeUnixMsList=[1710116345232, 1710116348732],
            ),
            ChannelReadings(
                ChannelId="6eae748c-a618-4f72-8e42-cff6ef578b3e",
                ValueList=[60155, 61200],
                ScadaReadTimeUnixMsList=[1710116345232, 1710116348732],
            ),
        ],
        FsmActionList=[],
        FsmReportList=[],
        Id="0d956f31-d120-42a0-97e3-eb04a8bb6ac2",
    )

    d = {
        "FromGNodeAlias": "d1.isone.ct.newhaven.rose.scada",
        "FromGNodeInstanceId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "AboutGNodeAlias": "d1.isone.ct.newhaven.rose.scada.ta",
        "SlotStartUnixS": 1710116340,
        "BatchedTransmissionPeriodS": 30,
        "DataChannelList": [
            {
                "Name": "hp-ewt",
                "DisplayName": "HP EWT",
                "AboutNodeName": "hp-ewt",
                "CapturedByNodeName": "analog-temp",
                "Id": "4693a282-9b9f-4d35-a060-92aa0d0a29aa",
                "TypeName": "data.channel.gt",
                "Version": "000",
                "TelemetryNameGtEnumSymbol": "c89d0ba1",
            },
            {
                "Name": "hp-lwt",
                "DisplayName": "HP LWT",
                "AboutNodeName": "hp-lwt",
                "CapturedByNodeName": "analog-temp",
                "Id": "6eae748c-a618-4f72-8e42-cff6ef578b3e",
                "TypeName": "data.channel.gt",
                "Version": "000",
                "TelemetryNameGtEnumSymbol": "c89d0ba1",
            },
        ],
        "ChannelReadingList": [
            {
                "ChannelId": "4693a282-9b9f-4d35-a060-92aa0d0a29aa",
                "ValueList": [48320, 49100],
                "ScadaReadTimeUnixMsList": [1710116345232, 1710116348732],
                "TypeName": "channel.readings",
                "Version": "000",
            },
            {
                "ChannelId": "6eae748c-a618-4f72-8e42-cff6ef578b3e",
                "ValueList": [60155, 61200],
                "ScadaReadTimeUnixMsList": [1710116345232, 1710116348732],
                "TypeName": "channel.readings",
                "Version": "000",
            },
        ],
        "FsmActionList": [],
        "FsmReportList": [],
        "Id": "0d956f31-d120-42a0-97e3-eb04a8bb6ac2",
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
