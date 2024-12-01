"""Type go.dormant, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import (
    SpaceheatName,
    UUID4Str,
)


class GoDormant(BaseModel):
    """ """

    FromName: SpaceheatName
    ToName: SpaceheatName
    TriggerId: UUID4Str
    TypeName: Literal["go.dormant"] = "go.dormant"
    Version: Literal["000"] = "000"