"""Type component.attribute.class.gt, version 000"""

from typing import Literal, Optional

from pydantic import BaseModel

from gwproto.enums import MakeModel
from gwproto.property_format import UUID4Str


class ComponentAttributeClassGt(BaseModel):
    ComponentAttributeClassId: UUID4Str
    DisplayName: Optional[str] = None
    MakeModel: MakeModel
    TypeName: Literal["component.attribute.class.gt"] = "component.attribute.class.gt"
    Version: Literal["000"] = "000"
