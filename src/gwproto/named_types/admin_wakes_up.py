"""Type admin.wakes.up, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import (
    SpaceheatName,
)


class AdminWakesUp(BaseModel):
    FromName: SpaceheatName
    ToName: SpaceheatName
    TypeName: Literal["admin.wakes.up"] = "admin.wakes.up"
    Version: Literal["000"] = "000"
