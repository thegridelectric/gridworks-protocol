"""Type gt.telemetry, version 110"""

from typing import Literal

from pydantic import BaseModel

from gwproto.enums import TelemetryName
from gwproto.property_format import UTCMilliseconds


class GtTelemetry(BaseModel):
    ScadaReadTimeUnixMs: UTCMilliseconds
    Value: int
    Name: TelemetryName
    Exponent: int
    TypeName: Literal["gt.telemetry"] = "gt.telemetry"
    Version: Literal["110"] = "110"

    def __hash__(self) -> int:
        return hash((type(self), *self.__dict__.values()))
