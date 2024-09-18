"""Type spaceheat.node.gt, version 200"""

from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict, model_validator
from typing_extensions import Self

from gwproto.enums import ActorClass
from gwproto.property_format import (
    HandleName,
    ReallyAnInt,
    SpaceheatName,
    UUID4Str,
)


class SpaceheatNodeGt(BaseModel):
    Name: SpaceheatName
    ActorHierarchyName: Optional[HandleName] = None
    Handle: Optional[HandleName] = None
    ActorClass: ActorClass
    DisplayName: Optional[str] = None
    ComponentId: Optional[str] = None
    NameplatePowerW: Optional[ReallyAnInt] = None
    InPowerMetering: Optional[bool] = None
    ShNodeId: UUID4Str
    TypeName: Literal["spaceheat.node.gt"] = "spaceheat.node.gt"
    Version: Literal["200"] = "200"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: InPowerMetering requirements.
        If InPowerMetering exists and is true, then NameplatePowerW must exist
        """
        # Implement check for axiom 1"
        return self

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["ActorClass"] = self.ActorClass.value
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "spaceheat.node.gt"
