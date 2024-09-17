"""Type synced.readings, version 000"""

from typing import List, Literal

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    ReallyAnInt,
    SpaceheatName,
    UTCMilliseconds,
)


class SyncedReadings(BaseModel):
    """
    A set of readings made at the same time by a multipurpose sensor, sent by SpaceheatNode
    actor capturing the data (which will be associated to some sort of multipurpose sensing
    component). The nth element of each of its three readings are coupled: AboutNodeName, what
    the value is, what the TelemetryName is.
    """

    ScadaReadTimeUnixMs: UTCMilliseconds
    ChannelNameList: List[SpaceheatName]
    ValueList: List[ReallyAnInt]
    TypeName: Literal["synced.readings"] = "synced.readings"
    Version: Literal["000"] = "000"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: List Length Consistency.
        len(ChannelNameList) = len(ValueList)
        """
        # Implement check for axiom 1"
        return self

    @classmethod
    def type_name_value(cls) -> str:
        return "synced.readings"
