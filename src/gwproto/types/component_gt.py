"""Type component.gt, version 001"""

from typing import Any, List, Literal, Optional

from pydantic import BaseModel, ConfigDict

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

    model_config = ConfigDict(extra="allow")

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["ConfigList"] = [elt.model_dump(**kwargs) for elt in self.ConfigList]
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "component.gt"
