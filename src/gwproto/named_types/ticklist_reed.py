"""Type ticklist.reed, version 101"""

from typing import Literal, Optional

from gw.named_types import GwBase
from pydantic import StrictInt, model_validator
from typing_extensions import Self


class TicklistReed(GwBase):
    """ASL schema of record [ticklist.reed v101](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/ticklist.reed.101.yaml)"""

    hw_uid: str
    first_tick_timestamp_nano_second: Optional[StrictInt] = None
    relative_millisecond_list: list[StrictInt]
    pico_before_post_timestamp_nano_second: StrictInt
    type_name: Literal["ticklist.reed"] = "ticklist.reed"
    version: Literal["101"] = "101"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: .
        FirstTickTimestampNanoSecond is None iff RelativeMillisecondList has length 0
        """
        if (
            self.first_tick_timestamp_nano_second is None
            and len(self.relative_millisecond_list) > 0
        ):
            raise ValueError(
                "FirstTickTimestampNanoSecond is None but RelativeMillisecondList has nonzero length!"
            )
        if (
            self.first_tick_timestamp_nano_second
            and len(self.relative_millisecond_list) == 0
        ):
            raise ValueError(
                "FirstTickTimestampNanoSecond exists but RelativeMillisecondList has no elements!"
            )
        return self
