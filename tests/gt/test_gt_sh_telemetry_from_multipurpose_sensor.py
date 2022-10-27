"""Tests gt.sh.telemetry.from.multipurpose.sensor type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.enums import TelemetryName
from gwproto.errors import SchemaError
from gwproto.messages import GtShTelemetryFromMultipurposeSensor
from gwproto.messages import GtShTelemetryFromMultipurposeSensor_Maker as Maker


def test_gt_sh_telemetry_from_multipurpose_sensor_generated():

    d = {
        "AboutNodeAliasList": ["a.elt1"],
        "ValueList": [18000],
        "ScadaReadTimeUnixMs": 1656587343297,
        "TelemetryNameList": ["ad19e79c"],
        "TypeAlias": "gt.sh.telemetry.from.multipurpose.sensor",
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
        scada_read_time_unix_ms=gw_tuple.ScadaReadTimeUnixMs,
        telemetry_name_list=gw_tuple.TelemetryNameList,
        #
    ).tuple
    assert payload == gw_tuple

    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["AboutNodeAliasList"]
    with pytest.raises(ValidationError):
        GtShTelemetryFromMultipurposeSensor(**d2)

    d2 = dict(d)
    del d2["ValueList"]
    with pytest.raises(ValidationError):
        GtShTelemetryFromMultipurposeSensor(**d2)

    d2 = dict(d)
    del d2["ScadaReadTimeUnixMs"]
    with pytest.raises(ValidationError):
        GtShTelemetryFromMultipurposeSensor(**d2)

    d2 = dict(d)
    del d2["TelemetryNameList"]
    with pytest.raises(ValidationError):
        GtShTelemetryFromMultipurposeSensor(**d2)

    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, AboutNodeAliasList=[{}])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ValueList=["1.1"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ScadaReadTimeUnixMs="1656587343297.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ScadaReadTimeUnixMs="1656587343297")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, ScadaReadTimeUnixMs=1656587343297.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, TelemetryNameList=["Unrecognized enum symbol"])
    assert Maker.dict_to_tuple(d2).TelemetryNameList == [TelemetryName.UNKNOWN]

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeAlias="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, AboutNodeAliasList="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ScadaReadTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
