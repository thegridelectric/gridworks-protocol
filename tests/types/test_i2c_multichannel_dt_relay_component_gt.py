"""Tests i2c.multichannel.dt.relay.component.gt type, version 000"""

import json

import pytest
from gw.errors import GwTypeError
from gwproto.enums import FsmEventType, MakeModel, RelayWiringConfig, Unit
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import ChannelConfig, RelayActorConfig
from gwproto.types import ComponentAttributeClassGt as CacGt
from gwproto.types import ComponentAttributeClassGtMaker as CacMaker
from gwproto.types.i2c_multichannel_dt_relay_component_gt import (
    I2cMultichannelDtRelayComponentGt,
)
from gwproto.types.i2c_multichannel_dt_relay_component_gt import (
    I2cMultichannelDtRelayComponentGtMaker as Maker,
)
from pydantic import ValidationError

from tests.utils import flush_all


def test_i2c_multichannel_dt_relay_component_gt_generated() -> None:
    flush_all()
    cac_gt = CacGt(
        component_attribute_class_id=CACS_BY_MAKE_MODEL[MakeModel.KRIDA__DOUBLEEMR16I2CV3],
        make_model=MakeModel.KRIDA__DOUBLEEMR16I2CV3,
        display_name="Krida EMR16 16-pin Relay Board",
    )
    CacMaker.tuple_to_dc(cac_gt)
    t = I2cMultichannelDtRelayComponentGt(
        component_id="1b9dd897-b203-4a9a-9d6e-4859d1f4c39d",
        component_attribute_class_id="29eab8b1-100f-4230-bb44-3a2fcba33cc3",
        i2c_address_list=[0x20, 0x21],
        config_list=[
            ChannelConfig(
                channel_name="vdc-24-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="tstat-common-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="iso-valve-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="charge-discharge-valve-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="hp-failsafe-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="hp-scada-ops-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="open-all-therms-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="zone1-failsafe-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="zone1-scada-ops-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="zone2-failsafe-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
            ChannelConfig(
                channel_name="zone2-scada-ops-relay",
                poll_period_ms=1000,
                capture_period_s=300,
                async_capture=True,
                async_capture_delta=1,
                exponent=0,
                unit=Unit.Unitless,
            ),
        ],
        relay_config_list=[
            RelayActorConfig(
                relay_idx=1,
                actor_name="vdc-24-relay",
                wiring_config=RelayWiringConfig.NormallyClosed,
                event_type=FsmEventType.ChangeRelayState,
                de_energizing_event="CloseRelay",
            ),
            RelayActorConfig(
                relay_idx=2,
                actor_name="tstat-common-relay",
                wiring_config=RelayWiringConfig.NormallyClosed,
                event_type=FsmEventType.ChangeRelayState,
                de_energizing_event="CloseRelay",
            ),
            RelayActorConfig(
                relay_idx=3,
                actor_name="iso-valve-relay",
                wiring_config=RelayWiringConfig.NormallyOpen,
                event_type=FsmEventType.ChangeValveState,
                de_energizing_event="OpenValve",
            ),
            RelayActorConfig(
                relay_idx=4,
                actor_name="charge-discharge-valve-relay",
                wiring_config=RelayWiringConfig.NormallyOpen,
                event_type=FsmEventType.ChangeStoreFlowDirection,
                de_energizing_event="Discharge",
            ),
            RelayActorConfig(
                relay_idx=5,
                actor_name="hp-failsafe-relay",
                wiring_config=RelayWiringConfig.DoubleThrow,
                event_type=FsmEventType.ChangeHeatPumpControl,
                de_energizing_event="SwitchToTankAquastat",
            ),
            RelayActorConfig(
                relay_idx=6,
                actor_name="hp-scada-ops-relay",
                wiring_config=RelayWiringConfig.NormallyClosed,
                event_type=FsmEventType.ChangeRelayState,
                de_energizing_event="CloseRelay",
            ),
            RelayActorConfig(
                relay_idx=16,
                actor_name="open-all-therms-relay",
                wiring_config=RelayWiringConfig.NormallyClosed,
                event_type=FsmEventType.ChangeRelayState,
                de_energizing_event="CloseRelay",
            ),
            RelayActorConfig(
                relay_idx=17,
                actor_name="zone1-failsafe-relay",
                wiring_config=RelayWiringConfig.DoubleThrow,
                event_type=FsmEventType.ChangeHeatcallSource,
                de_energizing_event="SwitchToWallThermostat",
            ),
            RelayActorConfig(
                relay_idx=18,
                actor_name="zone1-scada-ops-relay",
                wiring_config=RelayWiringConfig.NormallyOpen,
                event_type=FsmEventType.ChangeRelayState,
                de_energizing_event="OpenRelay",
            ),
            RelayActorConfig(
                relay_idx=19,
                actor_name="zone2-failsafe-relay",
                wiring_config=RelayWiringConfig.DoubleThrow,
                event_type=FsmEventType.ChangeHeatcallSource,
                de_energizing_event="SwitchToWallThermostat",
            ),
            RelayActorConfig(
                relay_idx=20,
                actor_name="zone2-scada-ops-relay",
                wiring_config=RelayWiringConfig.NormallyOpen,
                event_type=FsmEventType.ChangeRelayState,
                de_energizing_event="OpenRelay",
            ),
        ],
        display_name="Krida Relay Boards",
    )

    d = {
        "ComponentId": "1b9dd897-b203-4a9a-9d6e-4859d1f4c39d",
        "ComponentAttributeClassId": "29eab8b1-100f-4230-bb44-3a2fcba33cc3",
        "I2cAddressList": [32, 33],
        "ConfigList": [
            {
                "ChannelName": "vdc-24-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "tstat-common-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "iso-valve-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "charge-discharge-valve-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "hp-failsafe-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "hp-scada-ops-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "open-all-therms-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "zone1-failsafe-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "zone1-scada-ops-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "zone2-failsafe-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
            {
                "ChannelName": "zone2-scada-ops-relay",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 300,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "Exponent": 0,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "ec972387",
            },
        ],
        "RelayConfigList": [
            {
                "RelayIdx": 1,
                "ActorName": "vdc-24-relay",
                "DeEnergizingEvent": "CloseRelay",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "00000000",
                "EventTypeGtEnumSymbol": "00000000",
            },
            {
                "RelayIdx": 2,
                "ActorName": "tstat-common-relay",
                "DeEnergizingEvent": "CloseRelay",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "00000000",
                "EventTypeGtEnumSymbol": "00000000",
            },
            {
                "RelayIdx": 3,
                "ActorName": "iso-valve-relay",
                "DeEnergizingEvent": "OpenValve",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "63f5da41",
                "EventTypeGtEnumSymbol": "c234ee7a",
            },
            {
                "RelayIdx": 4,
                "ActorName": "charge-discharge-valve-relay",
                "DeEnergizingEvent": "Discharge",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "63f5da41",
                "EventTypeGtEnumSymbol": "1efc9909",
            },
            {
                "RelayIdx": 5,
                "ActorName": "hp-failsafe-relay",
                "DeEnergizingEvent": "SwitchToTankAquastat",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "8b15ff3f",
                "EventTypeGtEnumSymbol": "50ea0661",
            },
            {
                "RelayIdx": 6,
                "ActorName": "hp-scada-ops-relay",
                "DeEnergizingEvent": "CloseRelay",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "00000000",
                "EventTypeGtEnumSymbol": "00000000",
            },
            {
                "RelayIdx": 16,
                "ActorName": "open-all-therms-relay",
                "DeEnergizingEvent": "CloseRelay",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "00000000",
                "EventTypeGtEnumSymbol": "00000000",
            },
            {
                "RelayIdx": 17,
                "ActorName": "zone1-failsafe-relay",
                "DeEnergizingEvent": "SwitchToWallThermostat",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "8b15ff3f",
                "EventTypeGtEnumSymbol": "c5717e64",
            },
            {
                "RelayIdx": 18,
                "ActorName": "zone1-scada-ops-relay",
                "DeEnergizingEvent": "OpenRelay",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "63f5da41",
                "EventTypeGtEnumSymbol": "00000000",
            },
            {
                "RelayIdx": 19,
                "ActorName": "zone2-failsafe-relay",
                "DeEnergizingEvent": "SwitchToWallThermostat",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "8b15ff3f",
                "EventTypeGtEnumSymbol": "c5717e64",
            },
            {
                "RelayIdx": 20,
                "ActorName": "zone2-scada-ops-relay",
                "DeEnergizingEvent": "OpenRelay",
                "TypeName": "relay.actor.config",
                "Version": "000",
                "WiringConfigGtEnumSymbol": "63f5da41",
                "EventTypeGtEnumSymbol": "00000000",
            },
        ],
        "DisplayName": "Krida Relay Boards",
        "TypeName": "i2c.multichannel.dt.relay.component.gt",
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
    del d2["I2cAddressList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["ConfigList"]
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = d.copy()
    del d2["RelayConfigList"]
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

    d2 = dict(d, RelayConfigList="Not a list.")
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayConfigList=["Not a list of dicts"])
    with pytest.raises(GwTypeError):
        Maker.dict_to_tuple(d2)

    d2 = dict(d, RelayConfigList=[{"Failed": "Not a GtSimpleSingleStatus"}])
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
