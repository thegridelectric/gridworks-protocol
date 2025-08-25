"""Tests synth.channel.gt type, version 000"""

from gwproto.enums import TelemetryName
from gwproto.named_types import SynthChannelGt


def test_synth_channel_gt_generated() -> None:
    d = {
        "Id": "99fb8f0e-3c7c-4b62-be5a-4f7a6376519f",
        "Name": "required-swt",
        "CreatedByNodeName": "synth-generator",
        "TelemetryName": "WaterTempFTimes1000",
        "TerminalAssetAlias": "d1.isone.ct.orange.ta",
        "Strategy": "simple",
        "DisplayName": "Required Source Water Temp",
        "SyncReportMinutes": 60,
        "TypeName": "synth.channel.gt",
        "Version": "000",
    }

    d2 = SynthChannelGt.from_dict(d).to_dict()
    assert d == d2

    ######################################
    # Enum related
    ######################################

    assert type(d2["TelemetryName"]) is str

    d2 = dict(d, TelemetryName="unknown_enum_thing")
    assert SynthChannelGt(**d2).telemetry_name == TelemetryName.default()
