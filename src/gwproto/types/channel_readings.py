"""Type channel.readings, version 000"""

from typing import List, Literal

from pydantic import StrictInt, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    UTCMilliseconds,
)
from gwproto.types.data_channel_gt import DataChannelGt


class ChannelReadings(DataChannelGt):
    ValueList: List[StrictInt]
    ScadaReadTimeUnixMsList: List[UTCMilliseconds]
    TypeName: Literal["channel.readings"] = "channel.readings"
    Version: Literal["001"] = "001"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: ListLengthConsistency.
        ValueList and ScadaReadTimeUnixMsList must have the same length.
        """
        # Implement check for axiom 1"
        return self
