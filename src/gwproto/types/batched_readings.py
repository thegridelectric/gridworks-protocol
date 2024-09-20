"""Type batched.readings, version 000"""

from typing import List, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    PositiveInt,
    model_validator,
)
from typing_extensions import Self

from gwproto.property_format import (
    LeftRightDotStr,
    UTCMilliseconds,
    UTCSeconds,
    UUID4Str,
)
from gwproto.types.channel_readings import ChannelReadings


class BatchedReadings(BaseModel):
    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    AboutGNodeAlias: LeftRightDotStr
    SlotStartUnixS: UTCSeconds
    BatchedTransmissionPeriodS: PositiveInt
    MessageCreatedMs: UTCMilliseconds
    ChannelReadingList: List[ChannelReadings]
    Id: UUID4Str
    TypeName: Literal["batched.readings"] = "batched.readings"
    Version: Literal["001"] = "001"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 3: Time Consistency.
        For every ScadaReadTimeUnixMs   let read_s = read_ms / 1000.  Let start_s be SlotStartUnixS.  Then read_s >= start_s and start_s + BatchedTransmissionPeriodS + 1 + start_s > read_s.
        """
        # Implement check for axiom 3"
        return self
