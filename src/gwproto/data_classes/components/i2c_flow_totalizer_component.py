"""RelayComponent definition"""
from typing import Dict
from typing import Optional
from typing import List


from gwproto.data_classes.component_attribute_class import ComponentAttributeClass as Cac
from gwproto.data_classes.component import Component
from gwproto.types.channel_config import ChannelConfig
from gwproto.enums import MakeModel


class I2cFlowTotalizerComponent(Component):
    by_id: Dict[str, "I2cFlowTotalizerComponent"] = {}

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        i2c_address: int,
        config_list: List[ChannelConfig],
        pulse_flow_meter_make_model: MakeModel,
        conversion_factor: float,
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
        self.i2c_address = i2c_address
        self.pulse_flow_meter_make_model = pulse_flow_meter_make_model
        self.conversion_factor = conversion_factor

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
