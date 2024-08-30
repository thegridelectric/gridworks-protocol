"""ShNode definition"""

from typing import Dict, Optional

from gwproto.data_classes.component import Component
from gwproto.data_classes.errors import DataClassLoadingError
from gwproto.enums import ActorClass, Role


class ShNode:
    """
    A SpaceheatNode, or ShNode, is an organizing principal for the SCADA software.
    ShNodes can represent both underlying physical objects (water tank), measurements of these
    objects (temperature sensing at the top of a water tank), and actors within the code
    (an actor measuring multiple temperatures, or an actor responsible for filtering/smoothing
    temperature data for the purposes of thermostatic control).
    """

    by_id: Dict[str, "ShNode"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        sh_node_id: str,
        alias: str,
        actor_class: ActorClass,
        role: Role,
        display_name: Optional[str] = None,
        component_id: Optional[str] = None,
        reporting_sample_period_s: Optional[int] = None,
        rated_voltage_v: Optional[int] = None,
        typical_voltage_v: Optional[int] = None,
        in_power_metering: Optional[bool] = None,
    ) -> None:
        self.sh_node_id = sh_node_id
        self.alias = alias
        self.actor_class = actor_class
        self.role = role
        self.display_name = display_name
        self.component_id = component_id
        self.reporting_sample_period_s = reporting_sample_period_s
        self.rated_voltage_v = rated_voltage_v
        self.typical_voltage_v = typical_voltage_v
        self.in_power_metering = in_power_metering
        ShNode.by_id[self.sh_node_id] = self

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

    @property
    def component(self) -> Optional[Component]:
        if self.component_id is None:
            return None
        if self.component_id not in Component.by_id:
            raise DataClassLoadingError(
                f"{self.alias} component {self.component_id} not loaded!"
            )
        return Component.by_id[self.component_id]
