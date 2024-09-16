"""PipeFlowSensorComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import PipeFlowSensorCacGt, PipeFlowSensorComponentGt


class PipeFlowSensorComponent(
    Component[PipeFlowSensorComponentGt, PipeFlowSensorCacGt]
): ...
