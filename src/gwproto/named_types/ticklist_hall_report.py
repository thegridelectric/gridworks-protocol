"""Type ticklist.hall.report, version 000"""

from typing import Literal

from gw.named_types import GwBase

from gwproto.named_types.ticklist_hall import TicklistHall
from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UTCMilliseconds,
)


class TicklistHallReport(GwBase):
    """ASL schema of record [ticklist.hall.report v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/ticklist.hall.report.000.yaml)"""

    terminal_asset_alias: LeftRightDotStr
    channel_name: SpaceheatName
    scada_received_unix_ms: UTCMilliseconds
    ticklist: TicklistHall
    type_name: Literal["ticklist.hall.report"] = "ticklist.hall.report"
    version: Literal["000"] = "000"
