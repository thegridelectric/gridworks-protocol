"""Type telemetry.snapshot.spaceheat, version 000"""

from typing import List, Literal

from pydantic import BaseModel

from gwproto.enums import TelemetryName
from gwproto.property_format import LeftRightDotStr, UTCMilliseconds


class TelemetrySnapshotSpaceheat(BaseModel):
    ReportTimeUnixMs: UTCMilliseconds
    AboutNodeAliasList: list[LeftRightDotStr]
    ValueList: List[int]
    TelemetryNameList: list[TelemetryName]
    TypeName: Literal["telemetry.snapshot.spaceheat"] = "telemetry.snapshot.spaceheat"
    Version: Literal["000"] = "000"
