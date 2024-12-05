"""Type energy.instruction, version 000"""

from typing import Literal

from pydantic import BaseModel, PositiveInt

from gwproto.property_format import (
    LeftRightDotStr,
    UTCMilliseconds,
    UTCSeconds,
)


class EnergyInstruction(BaseModel):
    FromGNodeAlias: LeftRightDotStr
    SlotStartS: UTCSeconds
    SlotDurationMinutes: PositiveInt
    SendTimeMs: UTCMilliseconds
    AvgPowerWatts: PositiveInt
    TypeName: Literal["energy.instruction"] = "energy.instruction"
    Version: Literal["000"] = "000"
