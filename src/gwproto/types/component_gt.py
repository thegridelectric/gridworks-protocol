"""Type component.gt, version 000"""

from typing import Literal, Optional

from pydantic import BaseModel

from gwproto.property_format import UUID4Str


class ComponentGt(BaseModel):
    ComponentId: UUID4Str
    ComponentAttributeClassId: UUID4Str
    DisplayName: Optional[str] = None
    HwUid: Optional[str] = None
    TypeName: Literal["component.gt"] = "component.gt"
    Version: Literal["000"] = "000"
