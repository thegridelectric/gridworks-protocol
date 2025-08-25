"""Type ticklist.hall, version 101"""

from typing import Literal, Optional

from gw.named_types import GwBase
from pydantic import StrictInt, model_validator
from typing_extensions import Self


class TicklistHall(GwBase):
    """ASL schema of record [ticklist.hall v101](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/ticklist.hall.101.yaml)"""

    hw_uid: str
    first_tick_timestamp_nano_second: Optional[StrictInt] = None
    relative_microsecond_list: list[StrictInt]
    pico_before_post_timestamp_nano_second: StrictInt
    type_name: Literal["ticklist.hall"] = "ticklist.hall"
    version: Literal["101"] = "101"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: FirstTickTimestampNanoSecond is none iff RelativeMicrosecondList has length 0.

        """
        # Implement check for axiom 1
        return self
