"""Tests ads.channel.config type, version 000"""

from gwproto.enums import MakeModel, ThermistorDataMethod
from gwproto.types import AdsChannelConfig


def test_ads_channel_config_generated() -> None:
    d = {
        "ChannelName": "hp-ewt",
        "TerminalBlockIdx": 4,
        "ThermistorMakeModel": "TEWA__TT0P10KC3T1051500",
        "DataProcessingMethod": "SimpleBeta",
        "DataProcessingDescription": "using a beta of 3977.",
        "AsyncCapture": True,
        "AsyncCaptureDelta": 250,
        "CapturePeriodS": 60,
        "Exponent": 3,
        "PollPeriodMs": 200,
        "Unit": "Celcius",
        "TypeName": "ads.channel.config",
        "Version": "000",
    }

    d2 = AdsChannelConfig.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["ThermistorMakeModel"]) is str

    d2 = dict(d, ThermistorMakeModel="unknown_enum_thing")
    assert AdsChannelConfig(**d2).ThermistorMakeModel == MakeModel.default()

    assert type(d2["DataProcessingMethod"]) is str

    d2 = dict(d, DataProcessingMethod="unknown_enum_thing")
    assert AdsChannelConfig(**d2).DataProcessingMethod == ThermistorDataMethod.default()
