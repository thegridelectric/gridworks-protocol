"""Tests snapshot.spaceheat type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.errors import SchemaError
from gwproto.messages import SnapshotSpaceheat
from gwproto.messages import SnapshotSpaceheat_Maker as Maker


def test_snapshot_spaceheat_generated():

    d = {
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "FromGNodeInstanceId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "Snapshot": {
            "TelemetryNameList": ["5a71d4b3"],
            "AboutNodeAliasList": ["a.elt1.relay"],
            "ReportTimeUnixMs": 1656363448000,
            "ValueList": [1],
            "TypeAlias": "telemetry.snapshot.spaceheat",
        },
        "TypeAlias": "snapshot.spaceheat",
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
        from_g_node_instance_id=gw_tuple.FromGNodeInstanceId,
        snapshot=gw_tuple.Snapshot,
        #
    ).tuple
    assert payload == gw_tuple

    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["FromGNodeAlias"]
    with pytest.raises(ValidationError):
        SnapshotSpaceheat(**d2)

    d2 = dict(d)
    del d2["FromGNodeInstanceId"]
    with pytest.raises(ValidationError):
        SnapshotSpaceheat(**d2)

    d2 = dict(d)
    del d2["Snapshot"]
    with pytest.raises(ValidationError):
        SnapshotSpaceheat(**d2)

    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, FromGNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeInstanceId={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Snapshot="Not a TelemetrySnapshotSpaceheat.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeAlias="not the type alias")
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

    # End of Test
