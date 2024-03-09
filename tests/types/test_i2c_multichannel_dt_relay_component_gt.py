"""Tests i2c.multichannel.dt.relay.component.gt type, version 000"""
import json

import pytest
from pydantic import ValidationError

from gwproto.errors import SchemaError
from gwproto.types.i2c_multichannel_dt_relay_component_gt import I2cMultichannelDtRelayComponentGt
from gwproto.types.i2c_multichannel_dt_relay_component_gt import I2cMultichannelDtRelayComponentGt_Maker as Maker
from gwproto.types import ChannelConfig, RelayActorConfig
from gwproto.enums import Unit, RelayWiringConfig

def test_i2c_multichannel_dt_relay_component_gt_generated() -> None:
    t = I2cMultichannelDtRelayComponentGt(
        ComponentId="1b9dd897-b203-4a9a-9d6e-4859d1f4c39d",
        ComponentAttributeClassId="018d9ffb-89d1-4cc4-95c0-f170711b5ffa",
        ConfigList=[ChannelConfig(
             ChannelName='vdc-24-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='tstat-common-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='iso-valve-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='charge-discharge-valve-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='hp-failsafe-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='hp-scada-ops-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='open-all-therms-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='zone1-failsafe-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='zone1-scada-ops-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='zone2-failsafe-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            ),
            ChannelConfig(
             ChannelName='zone2-scada-ops-relay',
             PollPeriodMs=1000,
             CapturePeriodS=300,
             AsyncCapture=True,
             AsyncCaptureDelta=1,
             Exponent=0,
             Unit=Unit.Unitless
            )
        ],
        RelayConfigList = [
             RelayActorConfig(
                  RelayIdx=1,
                  ActorName='vdc-24-relay',
                  WiringConfig=RelayWiringConfig.NormallyClosed,
             ),
             RelayActorConfig(
                  RelayIdx=2,
                  ActorName='tstat-common-relay',
                  WiringConfig=RelayWiringConfig.NormallyClosed,
             ),
             RelayActorConfig(
                  RelayIdx=3,
                  ActorName='iso-valve-relay',
                  WiringConfig=RelayWiringConfig.NormallyOpen,
             ),
             RelayActorConfig(
                  RelayIdx=4,
                  ActorName='charge-discharge-valve-relay',
                  WiringConfig=RelayWiringConfig.NormallyOpen,
             ),
             RelayActorConfig(
                  RelayIdx=5,
                  ActorName='hp-failsafe-relay',
                  WiringConfig=RelayWiringConfig.DoubleThrow,
             ),
             RelayActorConfig(
                  RelayIdx=6,
                  ActorName='hp-scada-ops-relay',
                  WiringConfig=RelayWiringConfig.NormallyClosed,
             ),
             RelayActorConfig(
                  RelayIdx=16,
                  ActorName='open-all-therms-relay',
                  WiringConfig=RelayWiringConfig.NormallyClosed,
             ),
             RelayActorConfig(
                  RelayIdx=17,
                  ActorName='zone1-failsafe-relay',
                  WiringConfig=RelayWiringConfig.DoubleThrow,
             ),
             RelayActorConfig(
                  RelayIdx=18,
                  ActorName='zone1-scada-ops-relay',
                  WiringConfig=RelayWiringConfig.NormallyOpen,
             ),
             RelayActorConfig(
                  RelayIdx=19,
                  ActorName='zone2-failsafe-relay',
                  WiringConfig=RelayWiringConfig.DoubleThrow,
             ),
             RelayActorConfig(
                  RelayIdx=20,
                  ActorName='zone2-scada-ops-relay',
                  WiringConfig=RelayWiringConfig.NormallyOpen,
             )
             ],
             DisplayName="Krida Relay Boards Emr16-I2c-V3 Component"

        )

    d = {'ComponentId': '1b9dd897-b203-4a9a-9d6e-4859d1f4c39d', 'ComponentAttributeClassId': '018d9ffb-89d1-4cc4-95c0-f170711b5ffa', 'ConfigList': [{'ChannelName': 'vdc-24-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'tstat-common-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'iso-valve-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'charge-discharge-valve-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'hp-failsafe-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'hp-scada-ops-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'open-all-therms-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'zone1-failsafe-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'zone1-scada-ops-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'zone2-failsafe-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}, {'ChannelName': 'zone2-scada-ops-relay', 'PollPeriodMs': 1000, 'CapturePeriodS': 300, 'AsyncCapture': True, 'AsyncCaptureDelta': 1, 'Exponent': 0, 'TypeName': 'channel.config', 'Version': '000', 'UnitGtEnumSymbol': 'ec972387'}], 'RelayConfigList': [{'RelayIdx': 1, 'ActorName': 'vdc-24-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '00000000'}, {'RelayIdx': 2, 'ActorName': 'tstat-common-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '00000000'}, {'RelayIdx': 3, 'ActorName': 'iso-valve-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '63f5da41'}, {'RelayIdx': 4, 'ActorName': 'charge-discharge-valve-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '63f5da41'}, {'RelayIdx': 5, 'ActorName': 'hp-failsafe-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '8b15ff3f'}, {'RelayIdx': 6, 'ActorName': 'hp-scada-ops-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '00000000'}, {'RelayIdx': 16, 'ActorName': 'open-all-therms-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '00000000'}, {'RelayIdx': 17, 'ActorName': 'zone1-failsafe-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '8b15ff3f'}, {'RelayIdx': 18, 'ActorName': 'zone1-scada-ops-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '63f5da41'}, {'RelayIdx': 19, 'ActorName': 'zone2-failsafe-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '8b15ff3f'}, {'RelayIdx': 20, 'ActorName': 'zone2-scada-ops-relay', 'TypeName': 'relay.actor.config', 'Version': '000', 'WiringConfigGtEnumSymbol': '63f5da41'}], 'DisplayName': 'Krida Relay Boards Emr16-I2c-V3 Component', 'TypeName': 'i2c.multichannel.dt.relay.component.gt', 'Version': '000'}
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
    del d2["ConfigList"]
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d)
    del d2["RelayConfigList"]
    with pytest.raises(SchemaError):
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

    d2  = dict(d, ConfigList="Not a list.")
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, ConfigList=["Not a list of dicts"])
    with pytest.raises(SchemaError):
        Maker.dict_to_tuple(d2)

    d2  = dict(d, ConfigList= [{"Failed": "Not a GtSimpleSingleStatus"}])
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
