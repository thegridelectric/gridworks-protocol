"""Type spaceheat.node.gt, version 110"""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, StrictInt, model_validator
from typing_extensions import Self

from gwproto.enums import ActorClass, Role
from gwproto.property_format import SpaceheatName, UUID4Str


class SpaceheatNodeGt(BaseModel):
    ShNodeId: UUID4Str
    Alias: SpaceheatName
    ActorClass: ActorClass
    Role: Role
    DisplayName: Optional[str] = None
    ComponentId: Optional[UUID4Str] = None
    ReportingSamplePeriodS: Optional[int] = None
    InPowerMetering: Optional[bool] = Field(
        title="InPowerMetering",
        default=None,
    )
    NameplatePowerW: Optional[StrictInt] = None
    TypeName: Literal["spaceheat.node.gt"] = "spaceheat.node.gt"
    Version: Literal["120"] = "120"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: InPowerMetering requirements.
        If InPowerMetering exists and is true, then NameplatePowerW must exist
        """
        if self.InPowerMetering and self.NameplatePowerW is None:
            raise ValueError(
                "Axiom 1 failed! "
                "If InPowerMetering exists and is true, then NameplatePowerW must exist"
            )
        return self

    model_config = ConfigDict(extra="allow", use_enum_values=True)
