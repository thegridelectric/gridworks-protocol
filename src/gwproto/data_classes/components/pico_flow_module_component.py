"""PicoFlowModuleComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import ComponentAttributeClassGt, PicoFlowModuleComponentGt


class PicoFlowModuleComponent(
    Component[PicoFlowModuleComponentGt, ComponentAttributeClassGt]
): ...
