"""Type send.snap, version 000"""

from typing import Literal

from gw.named_types import GwBase

from gwproto.property_format import (
    LeftRightDotStr,
)


class SendSnap(GwBase):
    """ASL schema of record [send.snap v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/send.snap.000.yaml)"""

    from_g_node_alias: LeftRightDotStr
    type_name: Literal["send.snap"] = "send.snap"
    version: Literal["000"] = "000"
