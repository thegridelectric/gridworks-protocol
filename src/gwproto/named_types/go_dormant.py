"""Type go.dormant, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import (
    SpaceheatName,
)


class GoDormant(BaseModel):
    ToName: SpaceheatName
    TypeName: Literal["go.dormant"] = "go.dormant"
    Version: Literal["000"] = "000"
