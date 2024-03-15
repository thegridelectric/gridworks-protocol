"""ShNode definition"""
from typing import Dict
from typing import Optional

from gwproto.data_classes.component import Component
from gwproto.data_classes.errors import DataClassLoadingError
from gwproto.enums import ActorClass


class ShNode:
    """
    A SpaceheatNode, or ShNode, is an organizing principal for the SCADA software.
    ShNodes can represent both underlying physical objects (water tank), measurements of these
    objects (temperature sensing at the top of a water tank), and actors within the code
    (an actor measuring multiple temperatures, or an actor responsible for filtering/smoothing
    temperature data for the purposes of thermostatic control).
    """

    by_id: Dict[str, "ShNode"] = {}
    by_name: Dict[str, "ShNode"] = {}

    def  __new__(cls, name, sh_node_id, *args, **kwargs):
        try:
            return cls.by_name[name]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_name[name] = instance
            cls.by_id[sh_node_id] = instance
            return instance

    def __init__(
        self,
        sh_node_id: str,
        name: str,
        handle: str,
        actor_class: ActorClass,
        display_name: Optional[str] = None,
        component_id: Optional[str] = None,
        in_power_metering: Optional[bool] = None,
    ):
        self.sh_node_id = sh_node_id
        self.name = name
        self.handle = handle
        self.actor_class = actor_class
        self.display_name = display_name
        self.component_id = component_id
        self.in_power_metering = in_power_metering
        ShNode.by_id[self.sh_node_id] = self
        ShNode.by_name[self.name] = self

    def __repr__(self):
        return f"ShNode {self.display_name} => {self.actor_class.value} {self.name}"

    @property
    def has_actor(self) -> bool:
        if self.actor_class == ActorClass.NoActor:
            return False
        return True

    @property
    def component(self) -> Optional[Component]:
        if self.component_id is None:
            return None
        if self.component_id not in Component.by_id.keys():
            raise DataClassLoadingError(
                f"{self.name} component {self.component_id} not loaded!"
            )
        return Component.by_id[self.component_id]
