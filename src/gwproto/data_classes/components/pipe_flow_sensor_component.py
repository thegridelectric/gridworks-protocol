"""PipeFlowSensorComponent definition"""

from typing import Dict, Optional

from gwproto.data_classes.component import Component


class PipeFlowSensorComponent(Component):
    by_id: Dict[str, "PipeFlowSensorComponent"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        component_id: str,
        component_attribute_class_id: str,
        conversion_factor: float,
        i2c_address: int,
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
        expected_max_gpm_times100: Optional[int] = None,
    ) -> None:
        super(self.__class__, self).__init__(
            display_name=display_name,
            component_id=component_id,
            hw_uid=hw_uid,
            component_attribute_class_id=component_attribute_class_id,
        )
        self.i2c_address = i2c_address
        self.conversion_factor = conversion_factor
        self.expected_max_gpm_times100 = expected_max_gpm_times100
        PipeFlowSensorComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    def __repr__(self) -> str:
        return f"{self.display_name}  ({self.cac.make_model.value})"
