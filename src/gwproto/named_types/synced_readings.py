"""Type synced.readings, version 000"""

from typing import Literal

from gw.named_types import GwBase
from pydantic import StrictInt, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    SpaceheatName,
    UTCMilliseconds,
)


class SyncedReadings(GwBase):
    """ASL schema of record [synced.readings v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/synced.readings.000.yaml)"""

    channel_name_list: list[SpaceheatName]
    value_list: list[StrictInt]
    scada_read_time_unix_ms: UTCMilliseconds
    type_name: Literal["synced.readings"] = "synced.readings"
    version: Literal["000"] = "000"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: List Length Consistency.
        len(ChannelNameList) = len(ValueList)
        """
        # Implement check for axiom 1
        return self
