"""Type synth.channel.gt, version 000"""
from typing import Literal

from pydantic import BaseModel, PositiveInt

from gwproto.enums import TelemetryName, ActorClass
from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UUID4Str,
)


class SynthChannelGt(BaseModel):
    Id: UUID4Str
    Name: SpaceheatName
    CreatedByNodeName: SpaceheatName
    TelemetryName: TelemetryName
    TerminalAssetAlias: LeftRightDotStr
    Strategy: str
    DisplayName: str
    SyncReportMinutes: PositiveInt
    TypeName: Literal["synth.channel.gt"] = "synth.channel.gt"
    Version: Literal["000"] = "000"
