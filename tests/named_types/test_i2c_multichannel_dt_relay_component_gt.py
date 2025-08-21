"""Tests i2c.multichannel.dt.relay.component.gt type, version 000"""

from gwproto.named_types.i2c_multichannel_dt_relay_component_gt import (
    I2cMultichannelDtRelayComponentGt,
)


def test_i2c_multichannel_dt_relay_component_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "29eab8b1-100f-4230-bb44-3a2fcba33cc3",
        "ComponentId": "b95e75a3-1483-484f-954f-65d202d50e6d",
        "ConfigList": [
            {
                "ActorName": "relay1",
                "AsyncCapture": True,
                "CapturePeriodS": 300,
                "ChannelName": "vdc-relay1",
                "DeEnergizingEvent": "CloseRelay",
                "EnergizingEvent": "OpenRelay",
                "DeEnergizedState": "RelayClosed",
                "EnergizedState": "RelayOpen",
                "EventType": "change.relay.state",
                "StateType": "relay.closed.or.open",
                "Exponent": 0,
                "PollPeriodMs": 200,
                "RelayIdx": 1,
                "TypeName": "relay.actor.config",
                "Unit": "Unitless",
                "Version": "002",
                "WiringConfig": "NormallyClosed",
            },
            {
                "ActorName": "relay2",
                "AsyncCapture": True,
                "CapturePeriodS": 300,
                "ChannelName": "tstat-common-relay2",
                "DeEnergizingEvent": "CloseRelay",
                "EnergizingEvent": "OpenRelay",
                "DeEnergizedState": "RelayClosed",
                "EnergizedState": "RelayOpen",
                "EventType": "change.relay.state",
                "StateType": "relay.closed.or.open",
                "Exponent": 0,
                "PollPeriodMs": 200,
                "RelayIdx": 2,
                "TypeName": "relay.actor.config",
                "Unit": "Unitless",
                "Version": "002",
                "WiringConfig": "NormallyClosed",
            },
            {
                "ActorName": "relay3",
                "AsyncCapture": True,
                "CapturePeriodS": 300,
                "ChannelName": "charge-discharge-relay3",
                "DeEnergizingEvent": "DischargeStore",
                "EnergizingEvent": "ChargeStore",
                "DeEnergizedState": "DischargingStore",
                "EnergizedState": "ChargingStore",
                "EventType": "change.store.flow.relay",
                "StateType": "store.flow.relay",
                "Exponent": 0,
                "PollPeriodMs": 200,
                "RelayIdx": 3,
                "TypeName": "relay.actor.config",
                "Unit": "Unitless",
                "Version": "002",
                "WiringConfig": "NormallyOpen",
            },
        ],
        "DisplayName": "i2c krida relay boards",
        "I2cAddressList": [32, 33],
        "TypeName": "i2c.multichannel.dt.relay.component.gt",
        "Version": "002",
    }

    d2 = I2cMultichannelDtRelayComponentGt.from_dict(d).to_dict()
    assert d2 == d

    assert type(d2["ConfigList"][0]["EventType"]) is str
