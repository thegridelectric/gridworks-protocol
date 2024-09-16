"""Type spaceheat.node.gt, version 100"""

from typing import Literal, Optional

from pydantic import BaseModel, Field

from gwproto.enums import ActorClass, Role
from gwproto.property_format import LeftRightDotStr, UUID4Str


class SpaceheatNodeGt(BaseModel):
    ShNodeId: UUID4Str
    Alias: LeftRightDotStr
    ActorClass: ActorClass
    Role: Role
    DisplayName: Optional[str] = None
    ComponentId: Optional[UUID4Str] = None
    ReportingSamplePeriodS: Optional[int] = None
    InPowerMetering: Optional[bool] = Field(
        title="InPowerMetering",
        default=None,
    )
    TypeName: Literal["spaceheat.node.gt"] = "spaceheat.node.gt"
    Version: Literal["100"] = "100"
