"""Tests gt.sh.multipurpose.telemetry.status type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
from gwproto.messages import GtShMultipurposeTelemetryStatus
from gwproto.messages import GtShMultipurposeTelemetryStatus_Maker as Maker


def test_gt_sh_multipurpose_telemetry_status_generated():

    d = {
        "AboutNodeAlias": "a.elt1",
        "ValueList": [4559],
        "ReadTimeUnixMsList": [1656443705023],
        "SensorNodeAlias": "a.m",
        "TelemetryNameGtEnumSymbol": "af39eec9",
        "TypeAlias": "gt.sh.multipurpose.telemetry.status",
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
        about_node_alias=gw_tuple.AboutNodeAlias,
        telemetry_name=gw_tuple.TelemetryName,
        value_list=gw_tuple.ValueList,
        read_time_unix_ms_list=gw_tuple.ReadTimeUnixMsList,
        sensor_node_alias=gw_tuple.SensorNodeAlias,
        #
    ).tuple
    assert payload == gw_tuple

    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeAlias"]
    with pytest.raises(ValidationError):
        GtDispatchBoolean(**d2)

    d2 = dict(d)
    del d2["AboutNodeAlias"]
    with pytest.raises(ValidationError):
        GtShMultipurposeTelemetryStatus(**d2)

    d2 = dict(d)
    del d2["TelemetryNameGtEnumSymbol"]
    with pytest.raises(ValidationError):
        GtShMultipurposeTelemetryStatus(**d2)

    d2 = dict(d)
    del d2["ValueList"]
    with pytest.raises(ValidationError):
        GtShMultipurposeTelemetryStatus(**d2)

    d2 = dict(d)
    del d2["ReadTimeUnixMsList"]
    with pytest.raises(ValidationError):
        GtShMultipurposeTelemetryStatus(**d2)

    d2 = dict(d)
    del d2["SensorNodeAlias"]
    with pytest.raises(ValidationError):
        GtShMultipurposeTelemetryStatus(**d2)

    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, AboutNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TelemetryNameGtEnumSymbol="Unrecognized enum symbol")
    assert Maker.dict_to_tuple(d2).TelemetryName == TelemetryName.UNKNOWN

    d2 = dict(d, ValueList=["1.1"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReadTimeUnixMsList=["1.1"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SensorNodeAlias={})
    with pytest.raises(ValidationError):
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

    d2 = dict(d, AboutNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReadTimeUnixMsList=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
