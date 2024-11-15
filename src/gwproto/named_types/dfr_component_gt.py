"""Type dfr.component.gt, version 000"""

from typing import List, Literal, Optional

from pydantic import BaseModel, PositiveInt

from gwproto.named_types.dfr_config import DfrConfig
from gwproto.property_format import (
    UUID4Str,
)


class DfrComponentGt(BaseModel):
    ComponentId: UUID4Str
    ComponentAttributeClassId: UUID4Str
    ConfigList: List[DfrConfig]
    DisplayName: Optional[str] = None
    HwUid: Optional[str] = None
    I2cAddressList: List[PositiveInt]
    TypeName: Literal["dfr.component.gt"] = "dfr.component.gt"
    Version: Literal["000"] = "000"
