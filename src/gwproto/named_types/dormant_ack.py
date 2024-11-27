"""Type dormant.ack, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import (
    SpaceheatName,
    UUID4Str,
)


class DormantAck(BaseModel):
    FromName: SpaceheatName
    ToName: SpaceheatName
    TriggerId: UUID4Str
    TypeName: Literal["dormant.ack"] = "dormant.ack"
    Version: Literal["000"] = "000"
