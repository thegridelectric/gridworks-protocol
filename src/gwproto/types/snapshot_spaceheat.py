"""Type snapshot.spaceheat, version 001"""

from typing import Any, List, Literal

from pydantic import BaseModel

from gwproto.property_format import (
    LeftRightDotStr,
    UTCMilliseconds,
    UUID4Str,
)
from gwproto.types.single_reading import SingleReading


class SnapshotSpaceheat(BaseModel):
    """
    Snapshot.

    Collection of all the latest measurements (timestamped) captured by the SCADA for all of
    its data channels.
    """

    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    SnapshotTimeUnixMs: UTCMilliseconds
    LatestReadingList: List[SingleReading]
    TypeName: Literal["snapshot.spaceheat"] = "snapshot.spaceheat"
    Version: Literal["001"] = "001"

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["LatestReadingList"] = [
            elt.model_dump(**kwargs) for elt in self.LatestReadingList
        ]
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "snapshot.spaceheat"
