"""ElectricMeterComponent definition"""
from typing import Dict
from typing import List
from typing import Optional

from gwproto.data_classes.cacs.electric_meter_cac import ElectricMeterCac
from gwproto.data_classes.component import Component
from gwproto.enums import MakeModel
from gwproto.types import EgaugeIo
from gwproto.types.channel_config import ChannelConfig


class ElectricMeterComponent(Component):
    by_id: Dict[str, "ElectricMeterComponent"] = {}

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        config_list: List[ChannelConfig] = [],
        egauge_io_list: List[EgaugeIo] = [],
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
        modbus_host: Optional[str] = None,
        modbus_port: Optional[int] = None,
    ):
        super(self.__class__, self).__init__(
            component_id=component_id,
            component_attribute_class_id=component_attribute_class_id,
            config_list=config_list,
            display_name=display_name,
            hw_uid=hw_uid,
            
        )
        self.modbus_host = modbus_host
        self.modbus_port = modbus_port
        self.egauge_io_list = egauge_io_list
        ElectricMeterComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    @property
    def cac(self) -> ElectricMeterCac:
        return ElectricMeterCac.by_id[self.component_attribute_class_id]

    @property
    def make_model(self) -> MakeModel:
        return self.cac.make_model

    def __repr__(self):
        return f"{self.display_name}  ({self.cac.make_model.value})"
