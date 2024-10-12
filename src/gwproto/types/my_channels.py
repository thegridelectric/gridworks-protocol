"""Type my.channels, version 000"""

from typing import List, Literal

from pydantic import BaseModel  # Count:true

from gwproto.property_format import (
    LeftRightDotStr,
    UTCMilliseconds,
    UUID4Str,
)
from gwproto.types.data_channel_gt import DataChannelGt


class MyChannels(BaseModel):
    """
    A message designed for a SCADA or AtomicTNode to share its data channels
    """

    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    MessageCreatedMs: UTCMilliseconds
    MessageId: UUID4Str
    ChannelList: List[DataChannelGt]
    TypeName: Literal["my.channels"] = "my.channels"
    Version: Literal["000"] = "000"
