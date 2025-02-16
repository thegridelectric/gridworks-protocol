"""Tests dfr.config type, version 000"""

from gwproto.enums import Unit
from gwproto.named_types import DfrConfig


def test_dfr_config_generated() -> None:
    d = {
        "ChannelName": "dist-dfr-010",
        "PollPeriodMs": 300,
        "CapturePeriodS": 60,
        "AsyncCapture": True,
        "AsyncCaptureDelta": 30,
        "Exponent": 6,
        "Unit": "W",
        "OutputIdx": 1,
        "InitialVoltsTimes100": 40,
        "TypeName": "dfr.config",
        "Version": "000",
    }

    d2 = DfrConfig.model_validate(d).model_dump(exclude_none=True)

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["Unit"]) is str

    d2 = dict(d, Unit="unknown_enum_thing")
    assert DfrConfig(**d2).Unit == Unit.default()
