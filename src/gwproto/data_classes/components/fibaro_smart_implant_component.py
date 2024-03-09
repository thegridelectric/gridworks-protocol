from typing import Optional

from gwproto.data_classes.component import Component
from gwproto.data_classes.component_attribute_class import (
    ComponentAttributeClass as Cac,
)


class FibaroSmartImplantComponent(Component):
    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ):
        super().__init__(
            component_id=component_id,
            component_attribute_class_id=component_attribute_class_id,
            display_name=display_name,
            hw_uid=hw_uid,
        )

    @property
    def cac(self) -> Cac:
        return Cac.by_id[self.component_attribute_class_id]