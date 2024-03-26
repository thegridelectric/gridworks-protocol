"""Ads111xComponentComponent definition"""

from typing import Dict
from typing import List
from typing import Optional

from gwproto.data_classes.cacs.ads111x_based_cac import Ads111xBasedCac
from gwproto.data_classes.component import Component
from gwproto.enums import MakeModel
from gwproto.types import ThermistorDataProcessingConfig
from gwproto.types.channel_config import ChannelConfig


class Ads111xBasedComponent(Component):
    by_id: Dict[str, "Ads111xBasedComponent"] = {}

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        open_voltage_by_ads: List[float],
        config_list: List[ChannelConfig],
        thermistor_config_list: List[ThermistorDataProcessingConfig],
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
        self.open_voltage_by_ads = open_voltage_by_ads
        self.thermistor_config_list = thermistor_config_list
        Ads111xBasedComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    @property
    def cac(self) -> Ads111xBasedCac:
        return Ads111xBasedCac.by_id[self.component_attribute_class_id]

    @property
    def make_model(self) -> MakeModel:
        return self.cac.make_model

    def __repr__(self):
        return f"{self.display_name}  ({self.cac.make_model.value})"
