"""ResistiveHeaterComponent definition"""

from typing import Dict, Optional

from gwproto.data_classes.component import Component


class ResistiveHeaterComponent(Component):
    by_id: Dict[str, "ResistiveHeaterComponent"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        component_id: str,
        component_attribute_class_id: str,
        tested_max_hot_milli_ohms: Optional[int] = None,
        tested_max_cold_milli_ohms: Optional[int] = None,
        hw_uid: Optional[str] = None,
        display_name: Optional[str] = None,
    ) -> None:
        super(self.__class__, self).__init__(
            display_name=display_name,
            component_id=component_id,
            hw_uid=hw_uid,
            component_attribute_class_id=component_attribute_class_id,
        )
        self.tested_max_hot_milli_ohms = tested_max_hot_milli_ohms
        self.tested_max_cold_milli_ohms = tested_max_cold_milli_ohms
        ResistiveHeaterComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    def __repr__(self) -> str:
        return f"{self.display_name}  ({self.cac.make_model.value})"
