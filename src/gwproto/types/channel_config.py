"""Type channel.config, version 000"""

from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict, PositiveInt, model_validator
from typing_extensions import Self

from gwproto.enums import Unit
from gwproto.property_format import (
    ReallyAnInt,
    SpaceheatName,
)


class ChannelConfig(BaseModel):
    ChannelName: SpaceheatName
    PollPeriodMs: PositiveInt
    CapturePeriodS: PositiveInt
    AsyncCapture: bool
    AsyncCaptureDelta: Optional[PositiveInt] = None
    Exponent: ReallyAnInt
    Unit: Unit
    TypeName: Literal["channel.config"] = "channel.config"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Async Capture Consistency.
        If AsyncCapture is True, then AsyncCaptureDelta exists
        """
        # Implement check for axiom 1"
        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: Capture and Polling Consistency.
        CapturePeriodMs (CapturePeriodS * 1000) must be larger than PollPeriodMs. If CapturePeriodMs < 10 * PollPeriodMs then CapturePeriodMs must be a multiple of PollPeriodMs.
        """
        # Implement check for axiom 2"
        return self

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["Unit"] = self.Unit.value
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "channel.config"
