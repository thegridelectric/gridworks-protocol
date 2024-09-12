"""ShNode definition"""

from typing import Optional

from pydantic import ConfigDict

from gwproto.data_classes.components.component import Component
from gwproto.enums import ActorClass, Role
from gwproto.types import SpaceheatNodeGt


class ShNode(SpaceheatNodeGt):
    """
    A SpaceheatNode, or ShNode, is an organizing principal for the SCADA software.
    ShNodes can represent both underlying physical objects (water tank), measurements of these
    objects (temperature sensing at the top of a water tank), and actors within the code
    (an actor measuring multiple temperatures, or an actor responsible for filtering/smoothing
    temperature data for the purposes of thermostatic control).
    """

    component: Optional[Component] = None
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __hash__(self) -> int:
        return hash((type(self), *self.__dict__.values()))

    @property
    def sh_node_id(self) -> str:
        return self.ShNodeId

    @property
    def alias(self) -> str:
        return self.Alias

    @property
    def actor_class(self) -> ActorClass:
        return self.ActorClass

    @property
    def role(self) -> Role:
        return self.Role

    @property
    def display_name(self) -> Optional[str]:
        return self.DisplayName

    @property
    def component_id(self) -> Optional[str]:
        return self.ComponentId

    @property
    def reporting_sample_period_s(self) -> Optional[int]:
        return self.ReportingSamplePeriodS

    @property
    def in_power_metering(self) -> Optional[bool]:
        return self.InPowerMetering

    def __repr__(self) -> str:
        rs = f"ShNode {self.display_name} => {self.role.value} {self.alias}, "
        if self.has_actor:
            rs += " (has actor)"
        else:
            rs += " (passive, no actor)"
        return rs

    @property
    def has_actor(self) -> bool:
        return self.actor_class != ActorClass.NoActor
