"""Type alert, version 000"""

from typing import Literal, Optional

from gw.named_types import GwBase

from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UTCSeconds,
)


class Alert(GwBase):
    """ASL schema of record [alert v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/alert.000.yaml)"""

    from_g_node_alias: LeftRightDotStr
    about_node: Optional[SpaceheatName] = None
    unix_s: UTCSeconds
    summary: str
    ops_genie_alias: Optional[str] = None
    type_name: Literal["alert"] = "alert"
    version: Literal["000"] = "000"
