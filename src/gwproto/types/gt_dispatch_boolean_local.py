"""Type gt.dispatch.boolean.local, version 110"""

from typing import Literal

from pydantic import BaseModel, Field

from gwproto.property_format import Bit, LeftRightDotStr, UTCMilliseconds


class GtDispatchBooleanLocal(BaseModel):
    """
    Dispatch message sent locally by SCADA HomeAlone actor.

    By Locally, this means sent without access to Internet. The HomeAlone actor must reside
    within the Local Area Network of the SCADA - typically it should reside on the same hardware.
    """

    AboutNodeName: LeftRightDotStr
    FromNodeName: LeftRightDotStr
    RelayState: Bit = Field(
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
    TypeName: Literal["gt.dispatch.boolean.local"] = "gt.dispatch.boolean.local"
    Version: Literal["110"] = "110"
