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

    d2 = ThermistorDataProcessingConfig.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["ThermistorMakeModel"]) is str

    d2 = dict(d, ThermistorMakeModel="unknown_enum_thing")
    assert (
        ThermistorDataProcessingConfig(**d2).ThermistorMakeModel == MakeModel.default()
    )

    assert type(d2["DataProcessingMethod"]) is str

    d2 = dict(d, DataProcessingMethod="unknown_enum_thing")
    assert (
        ThermistorDataProcessingConfig(**d2).DataProcessingMethod
        == ThermistorDataMethod.default()
    )
