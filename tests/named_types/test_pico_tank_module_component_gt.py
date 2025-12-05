from gwproto.named_types import PicoTankModuleComponentGt


def test_pico_tank_module_component_gt_generated() -> None:
    d = {
        "AsyncCaptureDeltaMicroVolts": 2000,
        "ComponentAttributeClassId": "f88fbf89-5b74-46d6-84a3-8e7494d08435",
        "ComponentId": "f4308bf6-2f52-4500-9961-c44d94e56879",
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
                "ChannelName": "buffer-depth1-micro-v",
                "Exponent": 6,
                "TypeName": "channel.config",
                "Unit": "VoltsRms",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "CapturePeriodS": 60,
                "ChannelName": "buffer-depth2-micro-v",
                "Exponent": 6,
                "TypeName": "channel.config",
                "Unit": "VoltsRms",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "CapturePeriodS": 60,
                "ChannelName": "buffer-depth3-micro-v",
                "Exponent": 6,
                "TypeName": "channel.config",
                "Unit": "VoltsRms",
                "Version": "000",
            },
        ],
        "DisplayName": "buffer PicoTankModule",
        "Enabled": True,
        "NumSampleAverages": 30,
        "PicoHwUid": "pico_aaaaaa",
        "Samples": 1000,
        "SendMicroVolts": True,
        "SerialNumber": "9999",
        "TempCalcMethod": "SimpleBeta",
        "ThermistorBeta": 3977,
        "TypeName": "pico.tank.module.component.gt",
        "Version": "011",
    }
    d2 = PicoTankModuleComponentGt.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d
