"""Type ticklist.reed.report, version 000"""

from typing import Literal

from gw.named_types import GwBase

from gwproto.named_types.ticklist_reed import TicklistReed
from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UTCMilliseconds,
)


class TicklistReedReport(GwBase):
    """ASL schema of record [ticklist.reed.report v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/ticklist.reed.report.000.yaml)"""

    terminal_asset_alias: LeftRightDotStr
    channel_name: SpaceheatName
    scada_received_unix_ms: UTCMilliseconds
    ticklist: TicklistReed
    type_name: Literal["ticklist.reed.report"] = "ticklist.reed.report"
    version: Literal["000"] = "000"
