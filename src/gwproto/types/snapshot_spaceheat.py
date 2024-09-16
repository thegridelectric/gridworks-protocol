"""Type snapshot.spaceheat, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import LeftRightDotStr, UUID4Str
from gwproto.types.telemetry_snapshot_spaceheat import (
    TelemetrySnapshotSpaceheat,
)


class SnapshotSpaceheat(BaseModel):
    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    Snapshot: TelemetrySnapshotSpaceheat
    TypeName: Literal["snapshot.spaceheat"] = "snapshot.spaceheat"
    Version: Literal["000"] = "000"
