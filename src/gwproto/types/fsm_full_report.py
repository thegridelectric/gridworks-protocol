"""Type fsm.full.report, version 000"""

from typing import Any, List, Literal

from pydantic import BaseModel, ConfigDict

from gwproto.property_format import (
    SpaceheatName,
    UUID4Str,
)
from gwproto.types.fsm_atomic_report import FsmAtomicReport


class FsmFullReport(BaseModel):
    FromName: SpaceheatName
    TriggerId: UUID4Str
    AtomicList: List[FsmAtomicReport]
    TypeName: Literal["fsm.full.report"] = "fsm.full.report"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["AtomicList"] = [elt.model_dump(**kwargs) for elt in self.AtomicList]
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "fsm.full.report"
