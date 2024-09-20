"""MutlipurposeSensorComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import MultipurposeSensorCacGt, MultipurposeSensorComponentGt


class MultipurposeSensorComponent(
    Component[MultipurposeSensorComponentGt, MultipurposeSensorCacGt]
): ...
