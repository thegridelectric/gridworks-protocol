"""Tests synth.channel.gt type, version 000"""

import json

from gwproto.enums import TelemetryName
from gwproto.named_types import SynthChannelGt


def test_synth_channel_gt_generated() -> None:
    d = {
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

    t = SynthChannelGt.model_validate(d).model_dump_json(exclude_none=True)
    d2 = json.loads(t)
    assert d2 == d

    assert d2 == d

    ######################################
    # Enum related
    ######################################

    assert type(d2["TelemetryName"]) is str

    d2 = dict(d, TelemetryName="unknown_enum_thing")
    assert SynthChannelGt(**d2).TelemetryName == TelemetryName.default()
