"""Type synth.channel.gt, version 000"""

from typing import Literal

from gw.named_types import GwBase
from pydantic import PositiveInt

from gwproto.enums import TelemetryName
from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UUID4Str,
)


class SynthChannelGt(GwBase):
    """ASL schema of record [synth.channel.gt v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/synth.channel.gt.000.yaml)"""

    id: UUID4Str
    name: SpaceheatName
    created_by_node_name: SpaceheatName
    telemetry_name: TelemetryName
    terminal_asset_alias: LeftRightDotStr
    strategy: str
    display_name: str
    sync_report_minutes: PositiveInt
    type_name: Literal["synth.channel.gt"] = "synth.channel.gt"
    version: Literal["000"] = "000"
