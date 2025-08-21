"""Type heartbeat.b, version 001"""

from typing import Literal

from gw.named_types import GwBase

from gwproto.property_format import (
    HexChar,
    LeftRightDotStr,
    UTCMilliseconds,
    UUID4Str,
)


class HeartbeatB(GwBase):
    """ASL schema of record [heartbeat.b v001](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/heartbeat.b.001.yaml)"""

    from_g_node_alias: LeftRightDotStr
    from_g_node_instance_id: UUID4Str
    my_hex: HexChar
    your_last_hex: HexChar
    last_received_time_unix_ms: UTCMilliseconds
    send_time_unix_ms: UTCMilliseconds
    starting_over: bool
    type_name: Literal["heartbeat.b"] = "heartbeat.b"
    version: Literal["001"] = "001"
