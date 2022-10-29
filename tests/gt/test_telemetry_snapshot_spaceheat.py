"""Tests telemetry.snapshot.spaceheat type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
from gwproto.messages import TelemetrySnapshotSpaceheat
from gwproto.messages import TelemetrySnapshotSpaceheat_Maker as Maker


def test_telemetry_snapshot_spaceheat_generated():

    d = {
        "AboutNodeAliasList": ["a.elt1.relay", "a.tank.temp0"],
        "ValueList": [1, 66086],
        "TelemetryNameList": ["5a71d4b3", "c89d0ba1"],
        "ReportTimeUnixMs": 1656363448000,
        "TypeAlias": "telemetry.snapshot.spaceheat",
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
        about_node_alias_list=gw_tuple.AboutNodeAliasList,
        value_list=gw_tuple.ValueList,
        telemetry_name_list=gw_tuple.TelemetryNameList,
        report_time_unix_ms=gw_tuple.ReportTimeUnixMs,
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
    del d2["AboutNodeAliasList"]
    with pytest.raises(ValidationError):
        TelemetrySnapshotSpaceheat(**d2)

    d2 = dict(d)
    del d2["ValueList"]
    with pytest.raises(ValidationError):
        TelemetrySnapshotSpaceheat(**d2)

    d2 = dict(d)
    del d2["TelemetryNameList"]
    with pytest.raises(ValidationError):
        TelemetrySnapshotSpaceheat(**d2)

    d2 = dict(d)
    del d2["ReportTimeUnixMs"]
    with pytest.raises(ValidationError):
        TelemetrySnapshotSpaceheat(**d2)
    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, AboutNodeAliasList=[{}])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ValueList=["1.1"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TelemetryNameList=["Unrecognized enum symbol"])
    assert Maker.dict_to_tuple(d2).TelemetryNameList == [TelemetryName.UNKNOWN]

    d2 = dict(d, ReportTimeUnixMs="1656363448000.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReportTimeUnixMs="1656363448000")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, ReportTimeUnixMs=1656363448000.1)
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

    d2 = dict(d, AboutNodeAliasList=["a.b-h"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReportTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
