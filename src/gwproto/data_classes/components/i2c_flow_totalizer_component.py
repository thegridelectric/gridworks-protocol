"""RelayComponent definition"""

from typing import Dict, List, Optional

from gwproto.data_classes.component import Component
from gwproto.data_classes.component_attribute_class import (
    ComponentAttributeClass as Cac,
)
from gwproto.enums import MakeModel
from gwproto.types.channel_config import ChannelConfig


class I2cFlowTotalizerComponent(Component):
    by_id: Dict[str, "I2cFlowTotalizerComponent"] = {}

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        i2c_address_list: List[int],
        config_list: List[ChannelConfig],
        pulse_flow_meter_make_model_list: List[MakeModel],
        conversion_factor_list: List[float],
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ):
        super(self.__class__, self).__init__(
            component_id=component_id,
            component_attribute_class_id=component_attribute_class_id,
            config_list=config_list,
            display_name=display_name,
            hw_uid=hw_uid,
        )
        self.config_list = config_list
        self.i2c_address_list = i2c_address_list
        self.pulse_flow_meter_make_model_list = pulse_flow_meter_make_model_list
        self.conversion_factor_list = conversion_factor_list

        I2cFlowTotalizerComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    @property
    def cac(self) -> Cac:
        return Cac.by_id[self.component_attribute_class_id]

    @property
    def make_model(self) -> MakeModel:
        return self.cac.make_model

    def __repr__(self):
        return f"{self.display_name}  ({self.cac.make_model.value})"
