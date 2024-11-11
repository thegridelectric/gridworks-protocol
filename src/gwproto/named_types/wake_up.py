"""Type wake.up, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import SpaceheatName


class WakeUp(BaseModel):
    ToName: SpaceheatName
    TypeName: Literal["wake.up"] = "wake.up"
    Version: Literal["000"] = "000"
