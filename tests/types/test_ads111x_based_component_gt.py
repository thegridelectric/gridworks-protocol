"""Tests ads111x.based.component.gt type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import MakeModel, ThermistorDataMethod, Unit
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import ChannelConfig, ThermistorDataProcessingConfig
from gwproto.types import ComponentAttributeClassGt as CacGt
from gwproto.types import ComponentAttributeClassGtMaker as CacMaker
from gwproto.types.ads111x_based_component_gt import Ads111xBasedComponentGt
from gwproto.types.ads111x_based_component_gt import (
    Ads111xBasedComponentGtMaker as Maker,
)
from pydantic import ValidationError

from tests.utils import flush_all


def test_ads111x_based_component_gt_generated() -> None:
    flush_all()
    cac_gt = CacGt(
        component_attribute_class_id=CACS_BY_MAKE_MODEL[MakeModel.GRIDWORKS__MULTITEMP1],
        make_model=MakeModel.GRIDWORKS__MULTITEMP1,
        display_name="GridWorks MultiTemp1 (12-block temp sensor)",
    )
    CacMaker.tuple_to_dc(cac_gt)
    t = Ads111xBasedComponentGt(
        component_id="02f600e3-8692-43f8-84f2-a03c09c197e7",
        component_attribute_class_id="432073b8-4d2b-4e36-9229-73893f33f846",
        display_name="4-channel Ads for Beachrose",
        open_voltage_by_ads=[4.89, 4.95, 4.75],
        config_list=[
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
        thermistor_config_list=[
            ThermistorDataProcessingConfig(
                ChannelName="hp-ewt",
                TerminalBlockIdx=4,
                ThermistorMakeModel=MakeModel.TEWA__TT0P10KC3T1051500,
                DataProcessingMethod=ThermistorDataMethod.SimpleBeta,
                DataProcessingDescription="using a beta of 3977.",
            )
        ],
        hw_uid="1001",
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

    with pytest.raises(GwTypeError):
        Maker.type_to_tuple(d)

    with pytest.raises(GwTypeError):
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
    # GwTypeError raised if missing a required attribute
    ######################################

    d2 = d.copy()
    del d2["TypeName"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ComponentId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ComponentAttributeClassId"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["OpenVoltageByAds"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ConfigList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ThermistorConfigList"]
    with pytest.raises(GwTypeError):
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
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=["Not a list of dicts"])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ThermistorConfigList="Not a list.")
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ThermistorConfigList=["Not a list of dicts"])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, ThermistorConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if TypeName is incorrect
    ######################################

    d2 = dict(d, TypeName="not the type name")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)

    ######################################
    # ValidationError raised if primitive attributes do not have appropriate property_format
    ######################################

    d2 = dict(d, ComponentId="d4be12d5-33ba-4f1f-b9e5")
    with pytest.raises(ValidationError):
        Maker.dict_to_tuple(d2)
