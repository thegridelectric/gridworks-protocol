"""Type report, version 002"""

from typing import Literal

from gw.named_types import GwBase
from pydantic import PositiveInt, model_validator
from typing_extensions import Self

from gwproto.named_types.channel_readings import ChannelReadings
from gwproto.named_types.fsm_full_report import FsmFullReport
from gwproto.named_types.machine_states import MachineStates
from gwproto.property_format import (
    LeftRightDotStr,
    UTCMilliseconds,
    UTCSeconds,
    UUID4Str,
)


class Report(GwBase):
    """ASL schema of record [report v002](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/report.002.yaml)"""

    from_g_node_alias: LeftRightDotStr
    from_g_node_instance_id: UUID4Str
    about_g_node_alias: LeftRightDotStr
    slot_start_unix_s: UTCSeconds
    slot_duration_s: PositiveInt
    channel_reading_list: list[ChannelReadings]
    state_list: list[MachineStates]
    fsm_report_list: list[FsmFullReport]
    message_created_ms: UTCMilliseconds
    id: UUID4Str
    type_name: Literal["report"] = "report"
    version: Literal["002"] = "002"

    @model_validator(mode="after")
    def check_channel_reading_list(self) -> Self:
        """
        Axiom 2: Unique Channel names and Ids.
        The ChannelIds in the ChannelReadingList are all unique, as are the ChannelNames.
        """
        # Implement Axiom(s)
        return self
