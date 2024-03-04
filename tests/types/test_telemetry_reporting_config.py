"""Tests telemetry.reporting.config type, version 001"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import TelemetryReportingConfig_Maker as Maker
from gwproto.enums import TelemetryName
from gwproto.enums import Unit


def test_telemetry_reporting_config_generated() -> None:
    d = {
        "AboutNodeName": "a.elt1",
        "TelemetryNameGtEnumSymbol": "af39eec9",
        "PollPeriodMs": 300,
        "CapturePeriodS": 60,
        "AsyncCapture": True,
        "AsyncCaptureDelta": 0.2,
        "Exponent": 6,
        "UnitGtEnumSymbol": "f459a9c3",
        "TypeName": "telemetry.reporting.config",
        "Version": "001",
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
        about_node_name=gtuple.AboutNodeName,
        telemetry_name=gtuple.TelemetryName,
        poll_period_ms=gtuple.PollPeriodMs,
        capture_period_s=gtuple.CapturePeriodS,
        async_capture=gtuple.AsyncCapture,
        async_capture_delta=gtuple.AsyncCaptureDelta,
        exponent=gtuple.Exponent,
        unit=gtuple.Unit,
        
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
    del d2["AboutNodeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TelemetryNameGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["PollPeriodMs"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["CapturePeriodS"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AsyncCapture"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Exponent"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["UnitGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "AsyncCaptureDelta" in d2.keys():
        del d2["AsyncCaptureDelta"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TelemetryNameGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).TelemetryName == TelemetryName.default()

    d2 = dict(d, PollPeriodMs="300.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CapturePeriodS="60.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AsyncCapture="this is not a boolean")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AsyncCaptureDelta="0.2.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Exponent="6.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, UnitGtEnumSymbol="unknown_symbol")
    Maker.dict_to_tuple(d2).Unit == Unit.default()

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, AboutNodeName="A.hot-stuff")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, PollPeriodMs=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, CapturePeriodS=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AsyncCaptureDelta=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
