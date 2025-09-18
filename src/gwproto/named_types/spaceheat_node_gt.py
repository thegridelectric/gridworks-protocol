"""Type spaceheat.node.gt, version 200"""

from typing import Literal, Optional

from gw.named_types import GwBase
from gw.utils import snake_to_pascal
from pydantic import ConfigDict, StrictInt, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    HandleName,
    SpaceheatName,
    UUID4Str,
)


class SpaceheatNodeGt(GwBase):
    """ASL schema of record [spaceheat.node.gt v200](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/spaceheat.node.gt.200.yaml)"""

    name: SpaceheatName
    actor_hierarchy_name: Optional[HandleName] = None
    handle: Optional[HandleName] = None
    actor_class: str  # ActorClass
    display_name: Optional[str] = None
    component_id: Optional[str] = None
    nameplate_power_w: Optional[StrictInt] = None
    in_power_metering: Optional[bool] = None
    sh_node_id: UUID4Str
    type_name: Literal["spaceheat.node.gt"] = "spaceheat.node.gt"
    version: Literal["200"] = "200"

    model_config = ConfigDict(
        alias_generator=snake_to_pascal,  # Keep this
        frozen=False,  # Change this
        populate_by_name=True,  # Keep this
    )

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: InPowerMetering requirements.
        If InPowerMetering exists and is true, then NameplatePowerW must exist
        """
        if self.in_power_metering and self.nameplate_power_w is None:
            raise ValueError(
                "Axiom 1 failed! "
                "If InPowerMetering exists and is true, then NameplatePowerW must exist"
            )
        return self
