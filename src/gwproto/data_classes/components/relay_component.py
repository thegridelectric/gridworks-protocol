"""RelayComponent definition"""

from typing import Dict, Optional

from gwproto.data_classes.cacs.relay_cac import RelayCac
from gwproto.data_classes.component import Component
from gwproto.enums import MakeModel


class RelayComponent(Component):
    by_id: Dict[str, "RelayComponent"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        component_id: str,
        component_attribute_class_id: str,
        normally_open: bool,
        display_name: Optional[str] = None,
        gpio: Optional[int] = None,
        hw_uid: Optional[str] = None,
    ) -> None:
        super(self.__class__, self).__init__(
            display_name=display_name,
            component_id=component_id,
            hw_uid=hw_uid,
            component_attribute_class_id=component_attribute_class_id,
        )
        self.normally_open = normally_open
        self.gpio = gpio

        RelayComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    @property
    def cac(self) -> RelayCac:
        return RelayCac.by_id[self.component_attribute_class_id]

    @property
    def make_model(self) -> MakeModel:
        return self.cac.make_model

    def __repr__(self) -> str:
        return f"{self.display_name}  ({self.cac.make_model.value})"
