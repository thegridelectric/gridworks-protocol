"""Tests gt.sh.status type"""
import json

import pytest
from pydantic import ValidationError

from gwproto import Message
from gwproto.errors import SchemaError
from gwproto.messages import GtShStatus
from gwproto.messages import GtShStatus_Maker as Maker


def test_gt_sh_status_generated():

    d = {
        "SlotStartUnixS": 1656945300,
        "SimpleTelemetryList": [
            {
                "ValueList": [0, 1],
                "ReadTimeUnixMsList": [1656945400527, 1656945414270],
                "ShNodeAlias": "a.elt1.relay",
                "TypeAlias": "gt.sh.simple.telemetry.status",
                "TelemetryNameGtEnumSymbol": "5a71d4b3",
            }
        ],
        "AboutGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta",
        "BooleanactuatorCmdList": [
            {
                "ShNodeAlias": "a.elt1.relay",
                "RelayStateCommandList": [1],
                "CommandTimeUnixMsList": [1656945413464],
                "TypeAlias": "gt.sh.booleanactuator.cmd.status",
            }
        ],
        "FromGNodeAlias": "dwtest.isone.ct.newhaven.orange1.ta.scada",
        "MultipurposeTelemetryList": [
            {
                "AboutNodeAlias": "a.elt1",
                "ValueList": [18000],
                "ReadTimeUnixMsList": [1656945390152],
                "SensorNodeAlias": "a.m",
                "TypeAlias": "gt.sh.multipurpose.telemetry.status",
                "TelemetryNameGtEnumSymbol": "ad19e79c",
            }
        ],
        "FromGNodeId": "0384ef21-648b-4455-b917-58a1172d7fc1",
        "StatusUid": "dedc25c2-8276-4b25-abd6-f53edc79b62b",
        "ReportingPeriodS": 300,
        "TypeAlias": "gt.sh.status",
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
        slot_start_unix_s=gw_tuple.SlotStartUnixS,
        simple_telemetry_list=gw_tuple.SimpleTelemetryList,
        about_g_node_alias=gw_tuple.AboutGNodeAlias,
        booleanactuator_cmd_list=gw_tuple.BooleanactuatorCmdList,
        from_g_node_alias=gw_tuple.FromGNodeAlias,
        multipurpose_telemetry_list=gw_tuple.MultipurposeTelemetryList,
        from_g_node_id=gw_tuple.FromGNodeId,
        status_uid=gw_tuple.StatusUid,
        reporting_period_s=gw_tuple.ReportingPeriodS,
        #
    ).tuple
    assert payload == gw_tuple

    ######################################
    # ValidationError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["SlotStartUnixS"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    d2 = dict(d)
    del d2["SimpleTelemetryList"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    d2 = dict(d)
    del d2["AboutGNodeAlias"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    d2 = dict(d)
    del d2["BooleanactuatorCmdList"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    d2 = dict(d)
    del d2["FromGNodeAlias"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    d2 = dict(d)
    del d2["MultipurposeTelemetryList"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    d2 = dict(d)
    del d2["FromGNodeId"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    d2 = dict(d)
    del d2["StatusUid"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    d2 = dict(d)
    del d2["ReportingPeriodS"]
    with pytest.raises(ValidationError):
        GtShStatus(**d2)

    ######################################
    # Behavior on attribute types
    ######################################

    d2 = dict(d, SlotStartUnixS="1656945300.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, SlotStartUnixS="1656945300")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, SlotStartUnixS=1656945300.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    orig_value = d["SimpleTelemetryList"]
    d["SimpleTelemetryList"] = "Not a list."
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["SimpleTelemetryList"] = orig_value

    orig_value = d["SimpleTelemetryList"]
    d["SimpleTelemetryList"] = ["Not even a dict"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)

    d["SimpleTelemetryList"] = [{"Failed": "Not a GtSimpleSingleStatus"}]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["SimpleTelemetryList"] = orig_value

    with pytest.raises(ValidationError):
        Maker(
            slot_start_unix_s=d["SlotStartUnixS"],
            about_g_node_alias=d["AboutGNodeAlias"],
            booleanactuator_cmd_list=d["BooleanactuatorCmdList"],
            from_g_node_alias=d["FromGNodeAlias"],
            multipurpose_telemetry_list=d["MultipurposeTelemetryList"],
            from_g_node_id=d["FromGNodeId"],
            status_uid=d["StatusUid"],
            reporting_period_s=d["ReportingPeriodS"],
            simple_telemetry_list=["Not a GtShSimpleTelemetryStatus100"],
        )

    with pytest.raises(ValidationError):
        Maker(
            slot_start_unix_s=gw_tuple.SlotStartUnixS,
            about_g_node_alias=gw_tuple.AboutGNodeAlias,
            booleanactuator_cmd_list=gw_tuple.BooleanactuatorCmdList,
            from_g_node_alias=gw_tuple.FromGNodeAlias,
            multipurpose_telemetry_list=gw_tuple.MultipurposeTelemetryList,
            from_g_node_id=gw_tuple.FromGNodeId,
            status_uid=gw_tuple.StatusUid,
            reporting_period_s=gw_tuple.ReportingPeriodS,
            simple_telemetry_list="This string is not a list",
        )

    d2 = dict(d, AboutGNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    orig_value = d["BooleanactuatorCmdList"]
    d["BooleanactuatorCmdList"] = "Not a list."
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["BooleanactuatorCmdList"] = orig_value

    orig_value = d["BooleanactuatorCmdList"]
    d["BooleanactuatorCmdList"] = ["Not even a dict"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)

    d["BooleanactuatorCmdList"] = [{"Failed": "Not a GtSimpleSingleStatus"}]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["BooleanactuatorCmdList"] = orig_value

    with pytest.raises(ValidationError):
        Maker(
            slot_start_unix_s=d["SlotStartUnixS"],
            simple_telemetry_list=d["SimpleTelemetryList"],
            about_g_node_alias=d["AboutGNodeAlias"],
            from_g_node_alias=d["FromGNodeAlias"],
            multipurpose_telemetry_list=d["MultipurposeTelemetryList"],
            from_g_node_id=d["FromGNodeId"],
            status_uid=d["StatusUid"],
            reporting_period_s=d["ReportingPeriodS"],
            booleanactuator_cmd_list=["Not a GtShBooleanactuatorCmdStatus100"],
        )

    with pytest.raises(ValidationError):
        Maker(
            slot_start_unix_s=gw_tuple.SlotStartUnixS,
            simple_telemetry_list=gw_tuple.SimpleTelemetryList,
            about_g_node_alias=gw_tuple.AboutGNodeAlias,
            from_g_node_alias=gw_tuple.FromGNodeAlias,
            multipurpose_telemetry_list=gw_tuple.MultipurposeTelemetryList,
            from_g_node_id=gw_tuple.FromGNodeId,
            status_uid=gw_tuple.StatusUid,
            reporting_period_s=gw_tuple.ReportingPeriodS,
            booleanactuator_cmd_list="This string is not a list",
        )

    d2 = dict(d, FromGNodeAlias={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    orig_value = d["MultipurposeTelemetryList"]
    d["MultipurposeTelemetryList"] = "Not a list."
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["MultipurposeTelemetryList"] = orig_value

    orig_value = d["MultipurposeTelemetryList"]
    d["MultipurposeTelemetryList"] = ["Not even a dict"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)

    d["MultipurposeTelemetryList"] = [{"Failed": "Not a GtSimpleSingleStatus"}]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d)
    d["MultipurposeTelemetryList"] = orig_value

    with pytest.raises(ValidationError):
        Maker(
            slot_start_unix_s=d["SlotStartUnixS"],
            simple_telemetry_list=d["SimpleTelemetryList"],
            about_g_node_alias=d["AboutGNodeAlias"],
            booleanactuator_cmd_list=d["BooleanactuatorCmdList"],
            from_g_node_alias=d["FromGNodeAlias"],
            from_g_node_id=d["FromGNodeId"],
            status_uid=d["StatusUid"],
            reporting_period_s=d["ReportingPeriodS"],
            multipurpose_telemetry_list=["Not a GtShMultipurposeTelemetryStatus100"],
        )

    with pytest.raises(ValidationError):
        Maker(
            slot_start_unix_s=gw_tuple.SlotStartUnixS,
            simple_telemetry_list=gw_tuple.SimpleTelemetryList,
            about_g_node_alias=gw_tuple.AboutGNodeAlias,
            booleanactuator_cmd_list=gw_tuple.BooleanactuatorCmdList,
            from_g_node_alias=gw_tuple.FromGNodeAlias,
            from_g_node_id=gw_tuple.FromGNodeId,
            status_uid=gw_tuple.StatusUid,
            reporting_period_s=gw_tuple.ReportingPeriodS,
            multipurpose_telemetry_list="This string is not a list",
        )

    d2 = dict(d, FromGNodeId={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StatusUid={})
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReportingPeriodS="300.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ReportingPeriodS="300")
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    d2 = dict(d, ReportingPeriodS=300.1)
    assert Maker.dict_to_tuple(d2) == Maker.dict_to_tuple(d)

    ######################################
    # SchemaError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeAlias="not the type alias")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # SchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, SlotStartUnixS=32503683600)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, AboutGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, FromGNodeId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, StatusUid="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
