from typing import Dict
from typing import Optional

from gwproto.data_classes.component import Component
from gwproto.data_classes.component_attribute_class import (
    ComponentAttributeClass as Cac,
)
from gwproto.types.rest_poller_gt import RESTPollerSettings


class RESTPollerComponent(Component):
    by_id: Dict[str, "RESTPollerComponent"]
    rest: RESTPollerSettings

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        rest: RESTPollerSettings,
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ):
        self.rest = rest
        super().__init__(
            display_name=display_name,
            component_id=component_id,
            hw_uid=hw_uid,
            component_attribute_class_id=component_attribute_class_id,
        )
        RESTPollerComponent.by_id[self.component_id] = self

    @property
    def cac(self) -> Cac:
        return Cac.by_id[self.component_attribute_class_id]
