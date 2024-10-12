"""Type report, version 001"""

from typing import List, Literal

from pydantic import BaseModel, PositiveInt, field_validator  # Count:true

from gwproto.property_format import (
    LeftRightDotStr,
    UTCMilliseconds,
    UTCSeconds,
    UUID4Str,
)
from gwproto.types.channel_readings import ChannelReadings
from gwproto.types.fsm_atomic_report import FsmAtomicReport
from gwproto.types.fsm_full_report import FsmFullReport


class Report(BaseModel):
    """ """

    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    AboutGNodeAlias: LeftRightDotStr
    SlotStartUnixS: UTCSeconds
    SlotDurationS: PositiveInt
    ChannelReadingList: List[ChannelReadings]
    FsmActionList: List[FsmAtomicReport]
    FsmReportList: List[FsmFullReport]
    MessageCreatedMs: UTCMilliseconds
    Id: UUID4Str
    TypeName: Literal["report"] = "report"
    Version: Literal["001"] = "001"

    @field_validator("ChannelReadingList")
    @classmethod
    def _check_channel_reading_list(
        cls, v: List[ChannelReadings]
    ) -> List[ChannelReadings]:
        return v
