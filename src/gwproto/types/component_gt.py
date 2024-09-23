"""Type component.gt, version 000"""

from typing import List, Literal, Optional

from pydantic import BaseModel

from gwproto.property_format import UUID4Str
from gwproto.types.channel_config import ChannelConfig


class ComponentGt(BaseModel):
    ComponentId: UUID4Str
    ComponentAttributeClassId: UUID4Str
    ConfigList: List[ChannelConfig]
    DisplayName: Optional[str] = None
    HwUid: Optional[str] = None
    TypeName: Literal["component.gt"] = "component.gt"
    Version: Literal["001"] = "001"
