"""ElectricMeterComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import ElectricMeterCacGt, ElectricMeterComponentGt


class ElectricMeterComponent(
    Component[ElectricMeterComponentGt, ElectricMeterCacGt]
): ...
