"""Tests snapshot.spaceheat type, version 001"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import SingleReading
from gwproto.types import Snapshot
from gwproto.types import Snapshot_Maker as Maker


def test_snapshot_spaceheat_generated() -> None:
    t = Snapshot(
        FromGNodeAlias="d1.isone.ct.newhaven.rose.scada",
        FromGNodeInstanceId="0384ef21-648b-4455-b917-58a1172d7fc1",
        SnapshotTimeUnixMs=1709915800472,
        LatestReadingList=[],
    )

    d = {
        "FromGNodeAlias": "d1.isone.ct.newhaven.rose.scada",
        "FromGNodeInstanceId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "SnapshotTimeUnixMs": 1709915800472,
        "LatestReadingList": [],
        "TypeName": "snapshot.spaceheat",
        "Version": "001",
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
    del d2["SnapshotTimeUnixMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["LatestReadingList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, SnapshotTimeUnixMs="1709915800472.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, LatestReadingList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, LatestReadingList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, LatestReadingList=[{"Failed": "Not a GtSimpleSingleStatus"}])
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

    d2 = dict(d, SnapshotTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
