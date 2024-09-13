"""Type gt.dispatch.boolean, version 110"""

from typing import Literal

from pydantic import BaseModel, Field

from gwproto.property_format import LeftRightDotStr, UTCMilliseconds, UUID4Str


class GtDispatchBoolean(BaseModel):
    """
    GridWorks Type Boolean Dispatch.

    Boolean dispatch command designed to be sent from an AtomicTNode to a SCADA.
    """

    AboutNodeName: LeftRightDotStr
    ToGNodeAlias: LeftRightDotStr
    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    RelayState: bool = Field(
        title="Relay State (False or True)",
        description=(
            "A Relay State of `False` indicates the relay is OPEN (off). A Relay State of `True` indicates "
            "the relay is CLOSED (on). Note that `False` means the relay is open whether or not the "
            "relay is normally open or normally closed (For a normally open relay, the relay "
            "is ENERGIZED when it is in state `False` and DE-ENERGIZED when it is in state `True`.)"
            "[More info](https://gridworks.readthedocs.io/en/latest/relay-state.html)"
        ),
    )
    SendTimeUnixMs: UTCMilliseconds
    TypeName: Literal["gt.dispatch.boolean"] = "gt.dispatch.boolean"
    Version: Literal["110"] = "110"
