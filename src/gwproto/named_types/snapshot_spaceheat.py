"""Type snapshot.spaceheat, version 002"""

from typing import List, Literal

from pydantic import BaseModel

from gwproto.named_types.machine_states import MachineStates
from gwproto.named_types.single_reading import SingleReading
from gwproto.property_format import (
    LeftRightDotStr,
    UTCMilliseconds,
    UUID4Str,
)


class SnapshotSpaceheat(BaseModel):
    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    SnapshotTimeUnixMs: UTCMilliseconds
    LatestReadingList: List[SingleReading]
    LatestStateList: List[MachineStates]
    TypeName: Literal["snapshot.spaceheat"] = "snapshot.spaceheat"
    Version: Literal["002"] = "002"
