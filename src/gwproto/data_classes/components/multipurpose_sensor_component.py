"""MutlipurposeSensorComponent definition"""

from typing import Dict, List, Optional

from gwproto.data_classes.cacs.multipurpose_sensor_cac import MultipurposeSensorCac
from gwproto.data_classes.component import Component
from gwproto.enums import MakeModel
from gwproto.types import TelemetryReportingConfig


class MultipurposeSensorComponent(Component):
    by_id: Dict[str, "MultipurposeSensorComponent"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        component_id: str,
        component_attribute_class_id: str,
        channel_list: List[int],
        config_list: List[TelemetryReportingConfig],
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ) -> None:
        super(self.__class__, self).__init__(
            display_name=display_name,
            component_id=component_id,
            hw_uid=hw_uid,
            component_attribute_class_id=component_attribute_class_id,
        )
        self.channel_list = channel_list
        self.config_list = config_list
        MultipurposeSensorComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    @property
    def cac(self) -> MultipurposeSensorCac:
        return MultipurposeSensorCac.by_id[self.component_attribute_class_id]

    @property
    def make_model(self) -> MakeModel:
        return self.cac.make_model

    def __repr__(self) -> str:
        return f"{self.display_name}  ({self.cac.make_model.value})"
