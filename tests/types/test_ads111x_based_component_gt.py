"""Tests ads111x.based.component.gt type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.enums import MakeModel
from gwproto.enums import ThermistorDataMethod
from gwproto.enums import Unit
from gwproto.errors import SchemaError
from gwproto.types import ChannelConfig
from gwproto.types import ThermistorDataProcessingConfig
from gwproto.types.ads111x_based_component_gt import Ads111xBasedComponentGt
from gwproto.types.ads111x_based_component_gt import (
    Ads111xBasedComponentGt_Maker as Maker,
)


def test_ads111x_based_component_gt_generated() -> None:
    t = Ads111xBasedComponentGt(
        ComponentId="02f600e3-8692-43f8-84f2-a03c09c197e7",
        ComponentAttributeClassId="432073b8-4d2b-4e36-9229-73893f33f846",
        DisplayName="4-channel Ads for Beachrose",
        OpenVoltageByAds=[4.89, 4.95, 4.75],
        ConfigList=[
            ChannelConfig(
                ChannelName="hp-ewt",
                PollPeriodMs=200,
                CapturePeriodS=60,
                AsyncCapture=True,
                AsyncCaptureDelta=250,
                Exponent=3,
                Unit=Unit.Celcius,
            )
        ],
        ThermistorConfigList=[
            ThermistorDataProcessingConfig(
                ChannelName="hp-ewt",
                TerminalBlockIdx=4,
                ThermistorMakeModel=MakeModel.TEWA__TT0P10KC3T1051500,
                DataProcessingMethod=ThermistorDataMethod.SimpleBeta,
                DataProcessingDescription="using a beta of 3977.",
            )
        ],
        HwUid="1001",
    )

    d = {
        "ComponentId": "02f600e3-8692-43f8-84f2-a03c09c197e7",
        "ComponentAttributeClassId": "432073b8-4d2b-4e36-9229-73893f33f846",
        "DisplayName": "4-channel Ads for Beachrose",
        "OpenVoltageByAds": [4.89, 4.95, 4.75],
        "ConfigList": [
            {
                "ChannelName": "hp-ewt",
                "PollPeriodMs": 200,
                "CapturePeriodS": 60,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 250,
                "Exponent": 3,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec14bd47",
            }
        ],
        "ThermistorConfigList": [
            {
                "ChannelName": "hp-ewt",
                "TerminalBlockIdx": 4,
                "DataProcessingDescription": "using a beta of 3977.",
                "TypeName": "thermistor.data.processing.config",
                "Version": "000",
                "ThermistorMakeModelGtEnumSymbol": "652abfd6",
                "DataProcessingMethodGtEnumSymbol": "00000000",
            }
        ],
        "HwUid": "1001",
        "TypeName": "ads111x.based.component.gt",
        "Version": "000",
    }

    assert t.as_dict() == d

    with pytest.raises(SchemaError):
        Maker.type_to_tuple(d)

    with pytest.raises(SchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gtype = json.dumps(d)
    gtuple = Maker.type_to_tuple(gtype)
    assert gtuple == t

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gtuple)) == gtuple

    ######################################
    # Dataclass related tests
    ######################################

    dc = Maker.tuple_to_dc(gtuple)
    assert gtuple == Maker.dc_to_tuple(dc)
    assert Maker.type_to_dc(Maker.dc_to_type(dc)) == dc

    ######################################
    # SchemaError raised if missing a required attribute
    ######################################

    d2 = dict(d)
    del d2["TypeName"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ComponentId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ComponentAttributeClassId"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["OpenVoltageByAds"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ConfigList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["ThermistorConfigList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    # Axiom 2: channel names need to match between ConfigList and ThermistorConfigList
    d2 = dict(d)
    d2["ConfigList"] = [
        {
            "ChannelName": "hp-lwt",  # instead of "hp-ewt"
            "PollPeriodMs": 200,
            "CapturePeriodS": 60,
            "AsyncCapture": True,
            "AsyncCaptureDelta": 250,
            "Exponent": 3,
            "TypeName": "channel.config",
            "Version": "000",
            "UnitGtEnumSymbol": "ec14bd47",
        }
    ]
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # Optional attributes can be removed from type
    ######################################

    d2 = dict(d)
    if "DisplayName" in d2.keys():
        del d2["DisplayName"]
    Maker.dict_to_tuple(d2)

    d2 = dict(d)
    if "HwUid" in d2.keys():
        del d2["HwUid"]
    Maker.dict_to_tuple(d2)

    ######################################
    # Behavior on incorrect types
    ######################################

    d2 = dict(d, ConfigList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ThermistorConfigList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ThermistorConfigList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ThermistorConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
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

    d2 = dict(d, ComponentId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
