"""Type batched.readings, version 000"""

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
from gwproto.types.data_channel_gt import DataChannelGt
from gwproto.types.fsm_atomic_report import FsmAtomicReport
from gwproto.types.fsm_full_report import FsmFullReport


class BatchedReadings(BaseModel):
    """
    Batched Readings.

    A collection of telemetry readings sent up in periodic reports from a SCADA to an AtomicTNode.
    These are organized into data channels (a triple of TelemetryName, AboutNode, and CapturedByNode).
    This replaces GtShStatus. Changes include: FromGNodeId -> FromGNodeInstanveId ReportPeriodS
    -> BatchedTransmissionPeriodS
    """

    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    AboutGNodeAlias: LeftRightDotStr
    SlotStartUnixS: UTCSeconds
    BatchedTransmissionPeriodS: PositiveInt
    MessageCreatedMs: UTCMilliseconds
    DataChannelList: List[DataChannelGt]
    ChannelReadingList: List[ChannelReadings]
    FsmActionList: List[FsmAtomicReport]
    FsmReportList: List[FsmFullReport]
    Id: UUID4Str
    TypeName: Literal["batched.readings"] = "batched.readings"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

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
        Axiom 2: DataChannel Consistency.
        There is a bijection between the DataChannelLists and ChannelReadingLists via the ChannelId.
        """
        # Implement check for axiom 2"
        return self

    @model_validator(mode="after")
    def check_axiom_3(self) -> Self:
        """
        Axiom 3: Time Consistency.
        For every ScadaReadTimeUnixMs   let read_s = read_ms / 1000.  Let start_s be SlotStartUnixS.  Then read_s >= start_s and start_s + BatchedTransmissionPeriodS + 1 + start_s > read_s.
        """
        # Implement check for axiom 3"
        return self

    @classmethod
    def type_name_value(cls) -> str:
        return "batched.readings"
