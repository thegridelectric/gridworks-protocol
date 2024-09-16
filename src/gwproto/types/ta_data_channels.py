"""Type ta.data.channels, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import LeftRightDotStr, UTCSeconds, UUID4Str
from gwproto.types.data_channel import DataChannel


class TaDataChannels(BaseModel):
    TerminalAssetGNodeAlias: LeftRightDotStr
    TerminalAssetGNodeId: UUID4Str
    TimeUnixS: UTCSeconds
    Author: str
    Channels: list[DataChannel]
    Identifier: UUID4Str
    TypeName: Literal["ta.data.channels"] = "ta.data.channels"
    Version: Literal["000"] = "000"
