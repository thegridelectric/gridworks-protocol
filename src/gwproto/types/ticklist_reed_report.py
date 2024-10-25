from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import LeftRightDotStr, SpaceheatName, UTCMilliseconds
from gwproto.types.ticklist_reed import TicklistReed


class TicklistReedReport(BaseModel):
    TerminalAssetAlias: LeftRightDotStr
    ChannelName: SpaceheatName
    ScadaReceivedUnixMs: UTCMilliseconds
    Ticklist: TicklistReed

    TypeName: Literal["ticklist.reed.report"] = "ticklist.reed.report"
    Version: Literal["000"] = "000"
