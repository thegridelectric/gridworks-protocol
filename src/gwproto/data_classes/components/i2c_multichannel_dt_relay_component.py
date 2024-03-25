"""RelayComponent definition"""
from typing import Dict
from typing import List
from typing import Optional

from gwproto.data_classes.component import Component
from gwproto.data_classes.component_attribute_class import (
    ComponentAttributeClass as Cac,
)
from gwproto.enums import MakeModel
from gwproto.types.channel_config import ChannelConfig
from gwproto.types.relay_actor_config import RelayActorConfig


class I2cMultichannelDtRelayComponent(Component):
    by_id: Dict[str, "I2cMultichannelDtRelayComponent"] = {}

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        i2c_address_list: List[int],
        config_list: List[ChannelConfig],
        relay_config_list: List[RelayActorConfig],
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ):
        super(self.__class__, self).__init__(
            component_id=component_id,
            component_attribute_class_id=component_attribute_class_id,
            config_list=config_list,
            hw_uid=hw_uid,
            display_name=display_name,
        )
        self.i2c_address_list = i2c_address_list
        self.relay_config_list=relay_config_list
        I2cMultichannelDtRelayComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    @property
    def cac(self) -> Cac:
        return Cac.by_id[self.component_attribute_class_id]

    @property
    def make_model(self) -> MakeModel:
        return self.cac.make_model

    def __repr__(self):
        return f"{self.display_name}  ({self.cac.make_model.value})"
