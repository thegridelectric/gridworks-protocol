"""Type gt.driver.booleanactuator.cmd, version 100"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import LeftRightDotStr, UTCMilliseconds


class GtDriverBooleanactuatorCmd(BaseModel):
    """
    Boolean Actuator Driver Command.

    The boolean actuator actor reports when it has sent an actuation command to its driver so
    that the SCADA can add this to information to be sent up to the AtomicTNode.

    [More info](https://gridworks.readthedocs.io/en/latest/relay-state.html)
    """

    RelayState: bool
    ShNodeAlias: LeftRightDotStr
    CommandTimeUnixMs: UTCMilliseconds
    TypeName: Literal["gt.driver.booleanactuator.cmd"] = "gt.driver.booleanactuator.cmd"
    Version: Literal["100"] = "100"
