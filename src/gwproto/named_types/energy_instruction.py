"""Type energy.instruction, version 000"""

from typing import Literal

from pydantic import BaseModel, PositiveInt, model_validator
from typing_extensions import Self

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

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: SlotStartS should fall on the top of 5 minutes
        """
        if self.SlotStartS % 300 != 0:
            raise ValueError(
                "Axiom 1: SlotStartS should fall on the top of 5 minutes! "
                f"self.SlotStartS % 300: {self.SlotStartS % 300} "
            )
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: SendTimeMs should be no more than 10 seconds after SlotStartS
        """
        delay = self.SendTimeMs / 1000 - self.SlotStartS
        if delay > 10:
            raise ValueError(
                f"SendTimeMs should be no more than 10 seconds after SlotStartS, got {int(delay)}"
            )
        return self
