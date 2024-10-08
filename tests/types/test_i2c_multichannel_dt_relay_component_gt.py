"""Tests i2c.multichannel.dt.relay.component.gt type, version 000"""

from gwproto.types.i2c_multichannel_dt_relay_component_gt import (
    I2cMultichannelDtRelayComponentGt,
)


def test_i2c_multichannel_dt_relay_component_gt_generated() -> None:
    d = {
        "ComponentAttributeClassId": "29eab8b1-100f-4230-bb44-3a2fcba33cc3",
        "ComponentId": "cadd18d8-29f4-4909-9fe6-143380093fd0",
        "ConfigList": [
            {
                "ChannelName": "relay3-energization",
                "ActorName": "relay3",
                "DeEnergizingEvent": "Discharge",
                "EventType": "ChangeStoreFlowDirection",
                "RelayIdx": 3,
                "WiringConfig": "NormallyOpen",
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "CapturePeriodS": 300,
                "Exponent": 0,
                "PollPeriodMs": 5000,
                "Unit": "Unitless",
                "TypeName": "relay.actor.config",
                "Version": "000",
            },
            {
                "ActorName": "relay5",
                "DeEnergizingEvent": "SwitchToTankAquastat",
                "EventType": "ChangeHeatPumpControl",
                "RelayIdx": 5,
                "WiringConfig": "DoubleThrow",
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "CapturePeriodS": 300,
                "ChannelName": "relay5-energization",
                "Exponent": 0,
                "PollPeriodMs": 5000,
                "Unit": "Unitless",
                "TypeName": "relay.actor.config",
                "Version": "000",
            },
            {
                "ActorName": "relay6",
                "DeEnergizingEvent": "CloseRelay",
                "EventType": "ChangeRelayState",
                "RelayIdx": 6,
                "WiringConfig": "NormallyClosed",
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "CapturePeriodS": 300,
                "ChannelName": "relay6-energization",
                "Exponent": 0,
                "PollPeriodMs": 5000,
                "Unit": "Unitless",
                "TypeName": "relay.actor.config",
                "Version": "000",
            },
            {
                "ActorName": "relay8",
                "DeEnergizingEvent": "SwitchToBoiler",
                "EventType": "ChangeAquastatControl",
                "RelayIdx": 6,
                "WiringConfig": "DoubleThrow",
                "AsyncCapture": True,
                "AsyncCaptureDelta": 1,
                "CapturePeriodS": 300,
                "ChannelName": "aquastat-ctrl-relay-energization",
                "Exponent": 0,
                "PollPeriodMs": 5000,
                "Unit": "Unitless",
                "TypeName": "relay.actor.config",
                "Version": "000",
            },
        ],
        "DisplayName": "GSCADA double 16-pin Krida I2c Relay boards, as component",
        "I2cAddressList": [32, 33],
        "TypeName": "i2c.multichannel.dt.relay.component.gt",
        "Version": "000",
    }

    d2 = I2cMultichannelDtRelayComponentGt.model_validate(d).model_dump(
        exclude_none=True
    )

    assert type(d2["ConfigList"][0]["EventType"]) is str

    assert d2 == d
