"""Tests telemetry.reporting.config type, version 000"""

import json

import pytest
from pydantic import ValidationError

from gwproto.enums import TelemetryName, Unit
from gwproto.errors import SchemaError
from gwproto.types import TelemetryReportingConfig_Maker as Maker


def test_telemetry_reporting_config_generated() -> None:  # noqa: PLR0915
    d = {
        "TelemetryNameGtEnumSymbol": "af39eec9",
        "AboutNodeName": "a.elt1",
        "ReportOnChange": True,
        "SamplePeriodS": 300,
        "Exponent": 6,
        "UnitGtEnumSymbol": "f459a9c3",
        "AsyncReportThreshold": 0.2,
        "NameplateMaxValue": 4000,
        "TypeName": "telemetry.reporting.config",
        "Version": "000",
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
        telemetry_name=gtuple.TelemetryName,
        about_node_name=gtuple.AboutNodeName,
        report_on_change=gtuple.ReportOnChange,
        sample_period_s=gtuple.SamplePeriodS,
        exponent=gtuple.Exponent,
        unit=gtuple.Unit,
        async_report_threshold=gtuple.AsyncReportThreshold,
        nameplate_max_value=gtuple.NameplateMaxValue,
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
    del d2["TelemetryNameGtEnumSymbol"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["AboutNodeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ReportOnChange"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["SamplePeriodS"]
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
    del d2["AsyncReportThreshold"]
    Maker.dict_to_tuple(d2)

    # Test axiom 1: If AsyncReportThreshold exists, NameplateMaxValue must as well
    d2 = dict(d)
    del d2["NameplateMaxValue"]
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    del d2["AsyncReportThreshold"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TelemetryNameGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).TelemetryName == TelemetryName.default()

    d2 = dict(d, ReportOnChange="this is not a boolean")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SamplePeriodS="300.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Exponent="6.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, UnitGtEnumSymbol="unknown_symbol")
    assert Maker.dict_to_tuple(d2).Unit == Unit.default()

    d2 = dict(d, AsyncReportThreshold="this is not a float")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, NameplateMaxValue="4000.1")
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

    d2 = dict(d, AboutNodeName="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, NameplateMaxValue=0)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
