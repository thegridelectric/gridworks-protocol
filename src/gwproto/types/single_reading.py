"""Type single.reading, version 000"""

from typing import Literal

from pydantic import BaseModel, ConfigDict

from gwproto.property_format import (
    ReallyAnInt,
    SpaceheatName,
    UTCMilliseconds,
)


class SingleReading(BaseModel):
    """
    Simple Sensor Telemetry.

    A single data channel reading sent from a spaceheat node actor. The value is an integer.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/spaceheat-actor.html)
    """

    ScadaReadTimeUnixMs: UTCMilliseconds
    ChannelName: SpaceheatName
    Value: ReallyAnInt
    TypeName: Literal["single.reading"] = "single.reading"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @classmethod
    def type_name_value(cls) -> str:
        return "single.reading"
