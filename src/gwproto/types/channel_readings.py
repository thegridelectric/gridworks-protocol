"""Type channel.readings, version 000"""

from typing import List, Literal

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    ReallyAnInt,
    UTCMilliseconds,
    UUID4Str,
)


class ChannelReadings(BaseModel):
    """
    A list of timestamped readings (values) for a data channel. This is meant to be reported
    for non-local consumption (AtomicTNode, other) by a SCADA. Therefore, the data channel is
    referenced by its globally unique identifier. The receiver needs to reference this idea
    against a list of the data channels used by the SCADA for accurate parsing. Replaces both
    GtShSimpleTelemetryStatus and GtShMultipurposeTelemetryStatus
    """

    ChannelId: UUID4Str
    ValueList: List[ReallyAnInt]
    ScadaReadTimeUnixMsList: List[UTCMilliseconds]
    TypeName: Literal["channel.readings"] = "channel.readings"
    Version: Literal["000"] = "000"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: ListLengthConsistency.
        ValueList and ScadaReadTimeUnixMsList must have the same length.
        """
        # Implement check for axiom 1"
        return self

    @classmethod
    def type_name_value(cls) -> str:
        return "channel.readings"
