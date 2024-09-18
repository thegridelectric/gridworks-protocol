"""Type power.watts, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import ReallyAnInt


class PowerWatts(BaseModel):
    Watts: ReallyAnInt
    TypeName: Literal["power.watts"] = "power.watts"
    Version: Literal["000"] = "000"

    @classmethod
    def type_name_value(cls) -> str:
        return "power.watts"
