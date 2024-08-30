"""SimpleTempSensorCac definition"""

from typing import Dict, Optional

from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.enums import MakeModel, TelemetryName, Unit


class SimpleTempSensorCac(ComponentAttributeClass):
    by_id: Dict[str, "SimpleTempSensorCac"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        component_attribute_class_id: str,
        exponent: int,
        typical_response_time_ms: int,
        temp_unit: Unit,
        make_model: MakeModel,
        telemetry_name: TelemetryName,
        display_name: Optional[str] = None,
        comms_method: Optional[str] = None,
    ) -> None:
        super(self.__class__, self).__init__(
            component_attribute_class_id=component_attribute_class_id,
            display_name=display_name,
        )

        self.exponent = exponent
        self.comms_method = comms_method
        self.typical_response_time_ms = typical_response_time_ms
        self.telemetry_name = telemetry_name
        self.temp_unit = temp_unit
        self.make_model = make_model

        SimpleTempSensorCac.by_id[self.component_attribute_class_id] = self
        ComponentAttributeClass.by_id[self.component_attribute_class_id] = self
        if self.temp_unit not in {Unit.Celcius, Unit.Fahrenheit, Unit.Unitless}:
            raise ValueError(
                "TempSensorCac units must be Fahrenheit, Celsius or Unitless"
            )

    def __repr__(self) -> str:
        return f"{self.make_model.value} {self.display_name}"
