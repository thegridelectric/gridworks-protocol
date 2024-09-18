"""Type resistive.heater.component.gt, version 000"""

from typing import List, Literal, Optional

from pydantic import BaseModel

from gwproto.property_format import (
    ReallyAnInt,
    UUID4Str,
)
from gwproto.types.channel_config import ChannelConfig


class ResistiveHeaterComponentGt(BaseModel):
    ComponentId: UUID4Str
    ComponentAttributeClassId: UUID4Str
    DisplayName: Optional[str] = None
    HwUid: Optional[str] = None
    TestedMaxHotMilliOhms: Optional[ReallyAnInt] = None
    TestedMaxColdMilliOhms: Optional[ReallyAnInt] = None
    ConfigList: List[ChannelConfig]
    TypeName: Literal["resistive.heater.component.gt"] = "resistive.heater.component.gt"
    Version: Literal["000"] = "000"

    @classmethod
    def type_name_value(cls) -> str:
        return "resistive.heater.component.gt"
