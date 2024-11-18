"""Type dfr.config, version 000"""

from typing import Literal, Optional

from pydantic import BaseModel, PositiveInt, StrictInt

from gwproto.enums import Unit
from gwproto.property_format import (
    SpaceheatName,
)


class DfrConfig(BaseModel):
    """ """

    ChannelName: SpaceheatName
    PollPeriodMs: Optional[PositiveInt] = None
    CapturePeriodS: PositiveInt
    AsyncCapture: bool
    AsyncCaptureDelta: Optional[PositiveInt] = None
    Exponent: StrictInt
    Unit: Unit
    OutputIdx: PositiveInt
    InitialVoltsTimes100: PositiveInt
    TypeName: Literal["dfr.config"] = "dfr.config"
    Version: Literal["000"] = "000"
