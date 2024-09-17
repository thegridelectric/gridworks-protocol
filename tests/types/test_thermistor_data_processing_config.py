"""Tests thermistor.data.processing.config type, version 000"""

from gwproto.enums import MakeModel, ThermistorDataMethod
from gwproto.types import ThermistorDataProcessingConfig


def test_thermistor_data_processing_config_generated() -> None:
    d = {
        "ChannelName": "hp-ewt",
        "TerminalBlockIdx": 4,
        "ThermistorMakeModel": "TEWA__TT0P10KC3T1051500",
        "DataProcessingMethod": "SimpleBeta",
        "DataProcessingDescription": "using a beta of 3977.",
        "TypeName": "thermistor.data.processing.config",
        "Version": "000",
    }

    t = ThermistorDataProcessingConfig(**d)

    assert t.model_dump(exclude_none=True, by_alias=True) == d

    ######################################
    # Behavior on unknown enum values: sends to default
    ######################################

    d2 = dict(d, ThermistorMakeModel="unknown_enum_thing")
    assert (
        ThermistorDataProcessingConfig(**d2).thermistor_make_model
        == MakeModel.default()
    )

    d2 = dict(d, DataProcessingMethod="unknown_enum_thing")
    assert (
        ThermistorDataProcessingConfig(**d2).data_processing_method
        == ThermistorDataMethod.default()
    )
