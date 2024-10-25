"""Type ticklist.reed, version 101"""

from typing import List, Literal, Optional

from pydantic import BaseModel, model_validator
from typing_extensions import Self


class TicklistReed(BaseModel):
    HwUid: str
    FirstTickTimestampNanoSecond: Optional[int]
    RelativeMillisecondList: List[int]
    PicoBeforePostTimestampNanoSecond: float
    TypeName: Literal["ticklist.reed"] = "ticklist.reed"
    Version: Literal["101"] = "101"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        if (
            self.FirstTickTimestampNanoSecond is None
            and len(self.RelativeMillisecondList) > 0
        ):
            raise ValueError(
                "FirstTickTimestampNanoSecond is None but RelativeMillisecondList has nonzero length!"
            )
        if self.FirstTickTimestampNanoSecond and len(self.RelativeMillisecondList) == 0:
            raise ValueError(
                "FirstTickTimestampNanoSecond exists but RelativeMillisecondList has no elements!"
            )
        return self
