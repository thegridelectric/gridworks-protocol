"""MutlipurposeSensorComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import MultipurposeSensorCacGt
from gwproto.types.multipurpose_sensor_component_gt import MultipurposeSensorComponentGt


class MultipurposeSensorComponent(
    Component[MultipurposeSensorComponentGt, MultipurposeSensorCacGt]
): ...
