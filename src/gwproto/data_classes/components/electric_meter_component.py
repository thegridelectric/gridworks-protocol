"""ElectricMeterComponent definition"""

from typing import Dict, List, Optional

from gwproto.data_classes.cacs.electric_meter_cac import ElectricMeterCac
from gwproto.data_classes.component import Component
from gwproto.enums import MakeModel
from gwproto.types import EgaugeIo, TelemetryReportingConfig


class ElectricMeterComponent(Component):
    by_id: Dict[str, "ElectricMeterComponent"] = {}  # noqa: RUF012

    def __init__(  # noqa: PLR0913, PLR0917, RUF100
        self,
        component_id: str,
        component_attribute_class_id: str,
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
        modbus_host: Optional[str] = None,
        modbus_port: Optional[int] = None,
        config_list: Optional[List[TelemetryReportingConfig]] = None,
        egauge_io_list: Optional[List[EgaugeIo]] = None,
    ) -> None:
        if egauge_io_list is None:
            egauge_io_list = []
        if config_list is None:
            config_list = []
        super(self.__class__, self).__init__(
            display_name=display_name,
            component_id=component_id,
            hw_uid=hw_uid,
            component_attribute_class_id=component_attribute_class_id,
        )
        self.modbus_host = modbus_host
        self.modbus_port = modbus_port
        self.config_list = config_list
        self.egauge_io_list = egauge_io_list
        ElectricMeterComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    @property
    def cac(self) -> ElectricMeterCac:
        return ElectricMeterCac.by_id[self.component_attribute_class_id]

    @property
    def make_model(self) -> MakeModel:
        return self.cac.make_model

    def __repr__(self) -> str:
        return f"{self.display_name}  ({self.cac.make_model.value})"
