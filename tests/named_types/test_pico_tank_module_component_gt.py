"""Tests pico.tank.module.component.gt type, version 010"""

from gwproto.enums import TempCalcMethod
from gwproto.named_types import PicoTankModuleComponentGt


def test_pico_tank_module_component_gt_generated() -> None:
    d = {
        "Enabled": True,
        "PicoAHwUid": "pico_4c1a21",
        "PicoBHwUid": "pico_487a22",
        "TempCalcMethod": "SimpleBeta",
        "ThermistorBeta": 3977,
        "SendMicroVolts": True,
        "Samples": 1000,
        "NumSampleAverages": 10,
        "ComponentId": "3ac4b198-f464-49cb-a612-7e36adcda411",
        "ComponentAttributeClassId": "f88fbf89-5b74-46d6-84a3-8e7494d08435",
        "ConfigList": [
            {
                "AsyncCapture": True,
                "CapturePeriodS": 60,
                "ChannelName": "tank1-depth1",
                "Exponent": 3,
                "TypeName": "channel.config",
                "Unit": "Celcius",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "CapturePeriodS": 60,
                "ChannelName": "tank1-depth2",
                "Exponent": 3,
                "TypeName": "channel.config",
                "Unit": "Celcius",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "CapturePeriodS": 60,
                "ChannelName": "tank1-depth3",
                "Exponent": 3,
                "TypeName": "channel.config",
                "Unit": "Celcius",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "CapturePeriodS": 60,
                "ChannelName": "tank1-depth4",
                "Exponent": 3,
                "TypeName": "channel.config",
                "Unit": "Celcius",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "AsyncCaptureDelta": 2000,
                "CapturePeriodS": 60,
                "ChannelName": "tank1-depth1-micro-v",
                "Exponent": 6,
                "TypeName": "channel.config",
                "Unit": "VoltsRms",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "AsyncCaptureDelta": 2000,
                "CapturePeriodS": 60,
                "ChannelName": "tank1-depth2-micro-v",
                "Exponent": 6,
                "TypeName": "channel.config",
                "Unit": "VoltsRms",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "AsyncCaptureDelta": 2000,
                "CapturePeriodS": 60,
                "ChannelName": "tank1-depth3-micro-v",
                "Exponent": 6,
                "TypeName": "channel.config",
                "Unit": "VoltsRms",
                "Version": "000",
            },
            {
                "AsyncCapture": True,
                "AsyncCaptureDelta": 2000,
                "CapturePeriodS": 60,
                "ChannelName": "tank1-depth4-micro-v",
                "Exponent": 6,
                "TypeName": "channel.config",
                "Unit": "VoltsRms",
                "Version": "000",
            },
        ],
        "DisplayName": "buffer PicoTankModule",
        "SerialNumber": "NA",
        "AsyncCaptureDeltaMicroVolts": 2000,
        "TypeName": "pico.tank.module.component.gt",
        "Version": "010",
    }

    d2 = PicoTankModuleComponentGt.from_dict(d).to_dict()

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["TempCalcMethod"]) is str

    d2 = dict(d, TempCalcMethod="unknown_enum_thing")
    assert PicoTankModuleComponentGt(**d2).temp_calc_method == TempCalcMethod.default()
