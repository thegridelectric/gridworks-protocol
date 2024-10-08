"""I2cMultichannelDtRelayComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import ComponentAttributeClassGt, I2cMultichannelDtRelayComponentGt


class I2cMultichannelDtRelayComponent(
    Component[I2cMultichannelDtRelayComponentGt, ComponentAttributeClassGt]
): ...
