"""Type fsm.full.report, version 000"""

from typing import List, Literal

from pydantic import BaseModel, ConfigDict

from gwproto.property_format import (
    SpaceheatName,
    UUID4Str,
)
from gwproto.types.fsm_atomic_report import FsmAtomicReport


class FsmFullReport(BaseModel):
    """
    There will be cascading events, actions and transitions that will naturally follow a single
    high-level event. This message is designed to encapsulate all of those.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    FromName: SpaceheatName
    TriggerId: UUID4Str
    AtomicList: List[FsmAtomicReport]
    TypeName: Literal["fsm.full.report"] = "fsm.full.report"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @classmethod
    def type_name_value(cls) -> str:
        return "fsm.full.report"
