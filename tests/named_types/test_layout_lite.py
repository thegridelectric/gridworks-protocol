"""Tests layout.lite type, version 001"""

from gwproto.named_types import LayoutLite


def test_layout_lite_generated() -> None:
    d = {
        "FromGNodeAlias": "hw1.isone.me.versant.keene.beech.scada",
        "FromGNodeInstanceId": "98542a17-3180-4f2a-a929-6023f0e7a106",
        "MessageCreatedMs": 1728651445746,
        "MessageId": "1302c0f8-1983-43b2-90d2-61678d731db3",
        "Strategy": "House0",
        "ZoneList": ["Down", "Up"],
        "TotalStoreTanks": 3,
        "Ha1Params": {
            "AlphaTimes10": 120,
            "BetaTimes100": -22,
            "GammaEx6": 0,
            "IntermediatePowerKw": 1.5,
            "IntermediateRswtF": 100,
            "DdPowerKw": 12,
            "DdRswtF": 160,
            "DdDeltaTF": 20,
            "HpMaxKwTh": 6,
            "MaxEwtF": 170,
            "TypeName": "ha1.params",
            "Version": "001",
        },
        "ShNodes": [
            {
                "ActorClass": "Scada",
                "DisplayName": "Keene Beech Scada",
                "Name": "s",
                "ShNodeId": "da9a0427-d6c0-44c0-b51c-492c1e580dc5",
                "TypeName": "spaceheat.node.gt",
                "Version": "200",
            },
            {
                "ActorClass": "PowerMeter",
                "ActorHierarchyName": "s.power-meter",
                "ComponentId": "9633adef-2373-422d-8a0e-dfbd16ae081c",
                "DisplayName": "Primary Power Meter",
                "Name": "power-meter",
                "ShNodeId": "6c0563b7-5171-4b1c-bba3-de156bea4b95",
                "TypeName": "spaceheat.node.gt",
                "Version": "200",
            },
            {
                "ActorClass": "NoActor",
                "DisplayName": "Hp Idu",
                "InPowerMetering": True,
                "Name": "hp-idu",
                "NameplatePowerW": 4000,
                "ShNodeId": "07b8ca98-12c4-4510-8d0f-14fda2331215",
                "TypeName": "spaceheat.node.gt",
                "Version": "200",
            },
        ],
        "SynthChannels": [
            {
                "Id": "99fb8f0e-3c7c-4b62-be5a-4f7a6376519f",
                "Name": "required-swt",
                "CreatedByNodeName": "homealone",
                "TelemetryName": "WaterTempCTimes1000",
                "TerminalAssetAlias": "d1.isone.ct.orange.ta",
                "Strategy": "simple",
                "DisplayName": "Required Source Water Temp",
                "TypeName": "synth.channel.gt",
                "Version": "000",
            }
        ],
        "DataChannels": [
            {
                "Name": "hp-idu-pwr",
                "DisplayName": "Hp IDU",
                "AboutNodeName": "hp-idu",
                "CapturedByNodeName": "power-meter",
                "TelemetryName": "PowerW",
                "TerminalAssetAlias": "hw1.isone.me.versant.keene.beech.ta",
                "InPowerMetering": True,
                "StartS": 1721405699,
                "Id": "50cf426b-ff3f-4a30-8415-8d3fba5e0ab7",
                "TypeName": "data.channel.gt",
                "Version": "001",
            }
        ],
        "TankModuleComponents": [
            {
                "ComponentAttributeClassId": "f88fbf89-5b74-46d6-84a3-8e7494d08435",
                "ComponentId": "8aef0b11-5a1c-415e-b40e-d277e0ff4403",
                "ConfigList": [
                    {
                        "AsyncCapture": True,
                        "CapturePeriodS": 60,
                        "ChannelName": "buffer-depth1",
                        "Exponent": 3,
                        "TypeName": "channel.config",
                        "Unit": "Celcius",
                        "Version": "000",
                    },
                    {
                        "AsyncCapture": True,
                        "CapturePeriodS": 60,
                        "ChannelName": "buffer-depth2",
                        "Exponent": 3,
                        "TypeName": "channel.config",
                        "Unit": "Celcius",
                        "Version": "000",
                    },
                    {
                        "AsyncCapture": True,
                        "CapturePeriodS": 60,
                        "ChannelName": "buffer-depth3",
                        "Exponent": 3,
                        "TypeName": "channel.config",
                        "Unit": "Celcius",
                        "Version": "000",
                    },
                    {
                        "AsyncCapture": True,
                        "CapturePeriodS": 60,
                        "ChannelName": "buffer-depth4",
                        "Exponent": 3,
                        "TypeName": "channel.config",
                        "Unit": "Celcius",
                        "Version": "000",
                    },
                    {
                        "AsyncCapture": True,
                        "AsyncCaptureDelta": 2000,
                        "CapturePeriodS": 60,
                        "ChannelName": "buffer-depth1-micro-v",
                        "Exponent": 6,
                        "TypeName": "channel.config",
                        "Unit": "VoltsRms",
                        "Version": "000",
                    },
                    {
                        "AsyncCapture": True,
                        "AsyncCaptureDelta": 2000,
                        "CapturePeriodS": 60,
                        "ChannelName": "buffer-depth2-micro-v",
                        "Exponent": 6,
                        "TypeName": "channel.config",
                        "Unit": "VoltsRms",
                        "Version": "000",
                    },
                    {
                        "AsyncCapture": True,
                        "AsyncCaptureDelta": 2000,
                        "CapturePeriodS": 60,
                        "ChannelName": "buffer-depth3-micro-v",
                        "Exponent": 6,
                        "TypeName": "channel.config",
                        "Unit": "VoltsRms",
                        "Version": "000",
                    },
                    {
                        "AsyncCapture": True,
                        "AsyncCaptureDelta": 2000,
                        "CapturePeriodS": 60,
                        "ChannelName": "buffer-depth4-micro-v",
                        "Exponent": 6,
                        "TypeName": "channel.config",
                        "Unit": "VoltsRms",
                        "Version": "000",
                    },
                ],
                "DisplayName": "buffer PicoTankModule",
                "Enabled": True,
                "SerialNumber": "1030",
                "NumSampleAverages": 10,
                "PicoAHwUid": "pico_4c1a21",
                "PicoBHwUid": "pico_487a22",
                "PicoKOhms": 30,
                "Samples": 1000,
                "SendMicroVolts": True,
                "TempCalcMethod": "SimpleBetaForPico",
                "ThermistorBeta": 3977,
                "AsyncCaptureDeltaMicroVolts": 2000,
                "TypeName": "pico.tank.module.component.gt",
                "Version": "000",
            }
        ],
        "FlowModuleComponents": [
            {
                "AsyncCaptureThresholdGpmTimes100": 5,
                "ComponentAttributeClassId": "aa4ad342-883a-4f89-bf86-9eb430aeb308",
                "ComponentId": "b505a781-1671-467f-af8f-6d0ad7aca172",
                "ConfigList": [
                    {
                        "AsyncCapture": True,
                        "CapturePeriodS": 10,
                        "ChannelName": "primary-flow",
                        "Exponent": 2,
                        "TypeName": "channel.config",
                        "Unit": "Gpm",
                        "Version": "000",
                    },
                    {
                        "AsyncCapture": True,
                        "CapturePeriodS": 10,
                        "ChannelName": "primary-flow-hz",
                        "Exponent": 6,
                        "TypeName": "channel.config",
                        "Unit": "VoltsRms",
                        "Version": "000",
                    },
                ],
                "ConstantGallonsPerTick": 0.0748,
                "CutoffFrequency": 1.25,
                "DisplayName": "Primary Flow ReedFlowModule",
                "Enabled": True,
                "FlowMeterType": "EKM__HOTSPWM075HD",
                "FlowNodeName": "primary-flow",
                "GpmFromHzMethod": "Constant",
                "HwUid": "pico_1b5636",
                "HzCalcMethod": "BasicExpWeightedAvg",
                "NoFlowMs": 5000,
                "PublishAnyTicklistAfterS": 10,
                "PublishTicklistLength": 10,
                "SendGallons": False,
                "SendHz": True,
                "SendTickLists": False,
                "SerialNumber": "NA",
                "TypeName": "pico.flow.module.component.gt",
                "Version": "000",
            }
        ],
        "I2cRelayComponent": {
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
                    "EventType": "change.relay.state",
                    "Exponent": 0,
                    "PollPeriodMs": 200,
                    "RelayIdx": 1,
                    "TypeName": "relay.actor.config",
                    "Unit": "Unitless",
                    "Version": "001",
                    "WiringConfig": "NormallyClosed",
                },
                {
                    "ActorName": "relay2",
                    "AsyncCapture": True,
                    "CapturePeriodS": 300,
                    "ChannelName": "tstat-common-relay2",
                    "DeEnergizingEvent": "CloseRelay",
                    "EnergizingEvent": "OpenRelay",
                    "EventType": "change.relay.state",
                    "Exponent": 0,
                    "PollPeriodMs": 200,
                    "RelayIdx": 2,
                    "TypeName": "relay.actor.config",
                    "Unit": "Unitless",
                    "Version": "001",
                    "WiringConfig": "NormallyClosed",
                },
                {
                    "ActorName": "relay3",
                    "AsyncCapture": True,
                    "CapturePeriodS": 300,
                    "ChannelName": "charge-discharge-relay3",
                    "DeEnergizingEvent": "DischargeStore",
                    "EnergizingEvent": "ChargeStore",
                    "EventType": "change.store.flow.relay",
                    "Exponent": 0,
                    "PollPeriodMs": 200,
                    "RelayIdx": 3,
                    "TypeName": "relay.actor.config",
                    "Unit": "Unitless",
                    "Version": "001",
                    "WiringConfig": "NormallyOpen",
                },
            ],
            "DisplayName": "i2c krida relay boards",
            "I2cAddressList": [32, 33],
            "TypeName": "i2c.multichannel.dt.relay.component.gt",
            "Version": "001",
        },
        "TypeName": "layout.lite",
        "Version": "002",
    }

    d2 = LayoutLite.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
