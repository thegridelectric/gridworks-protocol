"""ShNode definition"""

from typing import Any, Optional

from pydantic import ConfigDict

from gwproto.data_classes.components.component import Component
from gwproto.enums import ActorClass as ActorClassEnum
from gwproto.named_types import SpaceheatNodeGt


def parent_hierarchy_name(hierarchy_name: str) -> str:
    last_delimiter = hierarchy_name.rfind(".")
    if last_delimiter == -1:
        return hierarchy_name
    return hierarchy_name[:last_delimiter]


class ShNode(SpaceheatNodeGt):
    """
    A SpaceheatNode, or ShNode, is an organizing principal for the SCADA software.
    ShNodes can represent both underlying physical objects (water tank), measurements of these
    objects (temperature sensing at the top of a water tank), and actors within the code
    (an actor measuring multiple temperatures, or an actor responsible for filtering/smoothing
    temperature data for the purposes of thermostatic control).
    """

    component: Optional[Component[Any, Any]] = None
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __hash__(self) -> int:
        return hash(self.sh_node_id)

    def __repr__(self) -> str:
        rs = f"ShNode {self.display_name} => {self.name}, "
        if self.has_actor:
            rs += f" ({self.actor_class})"
        else:
            rs += " (passive, no actor)"
        return rs

    @property
    def has_actor(self) -> bool:
        return self.actor_class != ActorClassEnum.NoActor

    def to_gt(self) -> SpaceheatNodeGt:
        return SpaceheatNodeGt.from_dict(self.to_dict(exclude={"component"}))
