"""ElectricMeterCac definition"""

from typing import Dict, List, Optional

from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.enums import LocalCommInterface, MakeModel, TelemetryName


class ElectricMeterCac(ComponentAttributeClass):
    by_id: Dict[str, "ElectricMeterCac"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        component_attribute_class_id: str,
        make_model: MakeModel,
        interface: LocalCommInterface,
        poll_period_ms: int,
        default_baud: int,
        display_name: Optional[str] = None,
        telemetry_name_list: Optional[List[TelemetryName]] = None,
    ) -> None:
        if telemetry_name_list is None:
            telemetry_name_list = []
        super(self.__class__, self).__init__(
            component_attribute_class_id=component_attribute_class_id,
            display_name=display_name,
        )
        self.default_baud = default_baud
        self.poll_period_ms = poll_period_ms
        self.interface = interface
        self.make_model = make_model
        self.telemetry_name_list = telemetry_name_list
        ElectricMeterCac.by_id[self.component_attribute_class_id] = self
        ComponentAttributeClass.by_id[self.component_attribute_class_id] = self

    def __repr__(self) -> str:
        return f"{self.make_model.value} {self.display_name}"
