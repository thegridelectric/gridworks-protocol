"""MultipurposeSensorCac definition"""

from typing import Dict, List, Optional

from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.enums import MakeModel, TelemetryName, Unit


class MultipurposeSensorCac(ComponentAttributeClass):
    by_id: Dict[str, "MultipurposeSensorCac"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        component_attribute_class_id: str,
        exponent: int,
        poll_period_ms: int,
        temp_unit: Unit,
        make_model: MakeModel,
        telemetry_name_list: List[TelemetryName],
        max_thermistors: Optional[int],
        display_name: Optional[str] = None,
        comms_method: Optional[str] = None,
    ) -> None:
        super(self.__class__, self).__init__(
            component_attribute_class_id=component_attribute_class_id,
            display_name=display_name,
        )

        self.exponent = exponent
        self.comms_method = comms_method
        self.poll_period_ms = poll_period_ms
        self.max_thermistors = max_thermistors
        self.telemetry_name_list = telemetry_name_list
        self.temp_unit = temp_unit
        self.make_model = make_model

        MultipurposeSensorCac.by_id[self.component_attribute_class_id] = self
        ComponentAttributeClass.by_id[self.component_attribute_class_id] = self

    def __repr__(self) -> str:
        return f"{self.make_model.value} {self.display_name}"
