"""Tests gt.sh.simple.telemetry.status type, version 100"""
import json

import pytest
from pydantic import ValidationError

from gwproto.enums import TelemetryName
from gwproto.errors import MpSchemaError
from gwproto.types import GtShSimpleTelemetryStatus_Maker as Maker


def test_gt_sh_simple_telemetry_status_generated() -> None:
    d = {
        "ShNodeAlias": "a.elt1.relay",
        "TelemetryNameGtEnumSymbol": "5a71d4b3",
        "ValueList": [0],
        "ReadTimeUnixMsList": [1656443705023],
        "TypeName": "gt.sh.simple.telemetry.status",
        "Version": "100",
    }

    with pytest.raises(MpSchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(MpSchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    # test Maker init
    t = Maker(
        sh_node_alias=gtuple.ShNodeAlias,
        telemetry_name=gtuple.TelemetryName,
        value_list=gtuple.ValueList,
        read_time_unix_ms_list=gtuple.ReadTimeUnixMsList,
    ).tuple
    assert t == gtuple

    ######################################
    # MpSchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ShNodeAlias"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TelemetryNameGtEnumSymbol"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ValueList"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ReadTimeUnixMsList"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TelemetryNameGtEnumSymbol="hi")
    Maker.dict_to_tuple(d2).TelemetryName = TelemetryName.default()

    ######################################
    # MpSchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # MpSchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ShNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReadTimeUnixMsList=[1656245000])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
