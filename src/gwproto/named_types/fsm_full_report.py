"""Type fsm.full.report, version 000"""

from typing import Literal

from gw.named_types import GwBase
from pydantic import ConfigDict

from gwproto.named_types.fsm_atomic_report import FsmAtomicReport
from gwproto.property_format import (
    SpaceheatName,
    UUID4Str,
)


class FsmFullReport(GwBase):
    """ASL schema of record [fsm.full.report v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/fsm.full.report.000.yaml)"""

    from_name: SpaceheatName
    trigger_id: UUID4Str
    atomic_list: list[FsmAtomicReport]
    type_name: Literal["fsm.full.report"] = "fsm.full.report"
    version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")
