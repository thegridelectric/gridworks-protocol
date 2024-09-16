"""RelayComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import RelayCacGt, RelayComponentGt


class RelayComponent(Component[RelayComponentGt, RelayCacGt]): ...
