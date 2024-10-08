"""Type report, version 000"""

from typing import List, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    PositiveInt,
    field_validator,
    model_validator,
)
from typing_extensions import Self

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
    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    AboutGNodeAlias: LeftRightDotStr
    SlotStartUnixS: UTCSeconds
    BatchedTransmissionPeriodS: PositiveInt
    ChannelReadingList: List[ChannelReadings]
    MessageCreatedMs: UTCMilliseconds
    Id: UUID4Str
    FsmActionList: List[FsmAtomicReport] = []
    FsmReportList: List[FsmFullReport] = []
    TypeName: Literal["report"] = "report"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow", use_enum_values=True)

    @field_validator("FsmActionList")
    @classmethod
    def check_fsm_action_list(cls, v: List[FsmAtomicReport]) -> List[FsmAtomicReport]:
        """
        Axiom 1: Each of the fsm.atomic.reports in this list must be actions (i.e. ActionType is not None)).
        """
        # Implement Axiom(s)
        return v

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: Time Consistency.
        For every ScadaReadTimeUnixMs   let read_s = read_ms / 1000.  Let start_s be SlotStartUnixS.  Then read_s >= start_s and start_s + BatchedTransmissionPeriodS + 1 + start_s > read_s.
        """
        # Implement check for axiom 1"

        return self

    @model_validator(mode="after")
    def check_axiom_3(self) -> Self:
        """
        Axiom 2: Unique Channel names and Ids
        """

        ids = [cr.ChannelId for cr in self.ChannelReadingList]
        if len(ids) != len(set(ids)):
            raise ValueError(
                "Axiom 1 violated! ChannelReadingList ChannelIds must be unique"
            )
        names = [cr.ChannelName for cr in self.ChannelReadingList]
        if len(names) != len(set(names)):
            raise ValueError(
                "Axiom 1 violated! ChannelReadingList ChannelNames must be unique"
            )
        return self
