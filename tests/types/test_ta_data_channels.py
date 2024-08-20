"""Tests ta.data.channels type, version 000"""

import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types import TaDataChannels_Maker as Maker


def test_ta_data_channels_generated() -> None:  # noqa: PLR0915
    d = {
        "TerminalAssetGNodeAlias": "hw1.isone.me.versant.keene.oak.ta",
        "TerminalAssetGNodeId": "7e152072-c91b-49d2-9ebd-f4fe1b684d06",
        "TimeUnixS": 1704142951,
        "Author": "Jessica Millar",
        "Channels": [
            {
                "DisplayName": "BoostPower",
                "AboutName": "a.elt1",
                "CapturedByName": "a.m",
                "TelemetryNameGtEnumSymbol": "af39eec9",
                "TypeName": "data.channel",
                "Version": "000",
            }
        ],
        "Identifier": "ba6558d8-2fe8-4174-ac16-c36f84367c50",
        "TypeName": "ta.data.channels",
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
        terminal_asset_g_node_alias=gtuple.TerminalAssetGNodeAlias,
        terminal_asset_g_node_id=gtuple.TerminalAssetGNodeId,
        time_unix_s=gtuple.TimeUnixS,
        author=gtuple.Author,
        channels=gtuple.Channels,
        identifier=gtuple.Identifier,
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
    del d2["TerminalAssetGNodeAlias"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TerminalAssetGNodeId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["TimeUnixS"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Author"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Channels"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["Identifier"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, TimeUnixS="1704142951.1")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Channels="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Channels=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Channels=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
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

    d2 = dict(d, TerminalAssetGNodeAlias="a.b-h")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TerminalAssetGNodeId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, TimeUnixS=32503683600)
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, Identifier="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    # End of Test
