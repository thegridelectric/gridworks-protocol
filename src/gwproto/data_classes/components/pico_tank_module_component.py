"""ResistiveHeaterComponent definition"""

from gwproto.data_classes.components.component import Component
from gwproto.types import ComponentAttributeClassGt, PicoTankModuleComponentGt


class PicoTankModuleComponent(
    Component[PicoTankModuleComponentGt, ComponentAttributeClassGt]
): ...
