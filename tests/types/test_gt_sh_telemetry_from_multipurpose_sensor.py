"""Tests gt.sh.telemetry.from.multipurpose.sensor type, version 100"""

import json

import pytest
from gwproto.errors import SchemaError
from gwproto.types import GtShTelemetryFromMultipurposeSensor_Maker as Maker
from pydantic import ValidationError


def test_gt_sh_telemetry_from_multipurpose_sensor_generated() -> None:
    d = {
        "ScadaReadTimeUnixMs": 1656587343297,
        "AboutNodeAliasList": ["a.elt1"],
        "TelemetryNameList": ["ad19e79c"],
        "ValueList": [18000],
        # TODO: bump-pydnatic hack; restore this to "gt.sh.telemetry.from.multipurpose.sensor"
        "TypeName": "gt.sh.telemetry.FROM.multipurpose.sensor",
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
        scada_read_time_unix_ms=gtuple.ScadaReadTimeUnixMs,
        about_node_alias_list=gtuple.AboutNodeAliasList,
        telemetry_name_list=gtuple.TelemetryNameList,
        value_list=gtuple.ValueList,
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
    del d2["ScadaReadTimeUnixMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AboutNodeAliasList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TelemetryNameList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ValueList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, ScadaReadTimeUnixMs="1656587343297.1")
    with pytest.raises(ValidationError):
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

    d2 = dict(d, ScadaReadTimeUnixMs=1656245000)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AboutNodeAliasList=["a.b-h"])
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
