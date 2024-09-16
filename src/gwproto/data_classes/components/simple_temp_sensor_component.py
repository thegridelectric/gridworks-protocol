"""SimpleTempSensorComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import SimpleTempSensorCacGt, SimpleTempSensorComponentGt


class SimpleTempSensorComponent(
    Component[SimpleTempSensorComponentGt, SimpleTempSensorCacGt]
): ...
