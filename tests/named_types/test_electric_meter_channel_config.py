"""Tests electric.meter.config type, version 000"""

from gwproto.named_types import ElectricMeterChannelConfig


def test_electric_meter_channel_config_generated() -> None:
    d = {
        "AsyncCapture": True,
        "AsyncCaptureDelta": 200,
        "CapturePeriodS": 300,
        "ChannelName": "hp-odu-pwr",
        "Exponent": 0,
        "PollPeriodMs": 1000,
        "Unit": "W",
        "EgaugeRegisterConfig": {
            "Address": 9004,
            "Name": "Garage power",
            "Description": "",
            "Type": "f32",
            "Denominator": 1,
            "Unit": "W",
            "TypeName": "egauge.register.config",
            "Version": "000",
        },
        "TypeName": "electric.meter.channel.config",
        "Version": "000",
    }

    d2 = ElectricMeterChannelConfig.from_dict(d).to_dict()
    assert d2 == d
