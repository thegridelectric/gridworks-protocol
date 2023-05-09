"""Tests gt.sh.multipurpose.telemetry.status type, version 100"""
import json

import pytest
from pydantic import ValidationError

from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
from gwproto.types import GtShMultipurposeTelemetryStatus_Maker as Maker


def test_gt_sh_multipurpose_telemetry_status_generated() -> None:
    d = {
        "AboutNodeAlias": "a.elt1",
        "SensorNodeAlias": "a.m",
        "TelemetryNameGtEnumSymbol": "af39eec9",
        "ValueList": [4559],
        "ReadTimeUnixMsList": [1656443705023],
        "TypeName": "gt.sh.multipurpose.telemetry.status",
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
        about_node_alias=gtuple.AboutNodeAlias,
        sensor_node_alias=gtuple.SensorNodeAlias,
        telemetry_name=gtuple.TelemetryName,
        value_list=gtuple.ValueList,
        read_time_unix_ms_list=gtuple.ReadTimeUnixMsList,
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
    del d2["AboutNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SensorNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TelemetryNameGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ValueList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ReadTimeUnixMsList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TelemetryNameGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).TelemetryName = TelemetryName.default()

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, AboutNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReadTimeUnixMsList=[1656245000])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
