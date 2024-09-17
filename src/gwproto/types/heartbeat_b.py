"""Type heartbeat.b, version 001"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import (
    HexChar,
    LeftRightDotStr,
    UTCMilliseconds,
    UUID4Str,
)


class HeartbeatB(BaseModel):
    """
    Heartbeat B.

    This is the Heartbeat intended to be sent between the Scada and the AtomicTNode to allow
    for block-chain validation of the status of their communication.

    [More info](https://gridworks.readthedocs.io/en/latest/dispatch-contract.html)
    """

    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    MyHex: HexChar
    YourLastHex: HexChar
    LastReceivedTimeUnixMs: UTCMilliseconds
    SendTimeUnixMs: UTCMilliseconds
    StartingOver: bool
    TypeName: Literal["heartbeat.b"] = "heartbeat.b"
    Version: Literal["001"] = "001"

    @classmethod
    def type_name_value(cls) -> str:
        return "heartbeat.b"
