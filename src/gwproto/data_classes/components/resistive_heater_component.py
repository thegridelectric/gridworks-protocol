"""ResistiveHeaterComponent definition"""

from typing import Dict, List, Optional

from gwproto.data_classes.cacs.resistive_heater_cac import ResistiveHeaterCac
from gwproto.data_classes.component import Component
from gwproto.enums import MakeModel
from gwproto.types.channel_config import ChannelConfig


class ResistiveHeaterComponent(Component):
    by_id: Dict[str, "ResistiveHeaterComponent"] = {}

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        config_list: List[ChannelConfig],
        tested_max_hot_milli_ohms: Optional[int] = None,
        tested_max_cold_milli_ohms: Optional[int] = None,
        hw_uid: Optional[str] = None,
        display_name: Optional[str] = None,
    ):
        super(self.__class__, self).__init__(
            display_name=display_name,
            component_id=component_id,
            config_list=config_list,
            hw_uid=hw_uid,
            component_attribute_class_id=component_attribute_class_id,
        )
        self.tested_max_hot_milli_ohms = tested_max_hot_milli_ohms
        self.tested_max_cold_milli_ohms = tested_max_cold_milli_ohms
        ResistiveHeaterComponent.by_id[self.component_id] = self
        Component.by_id[self.component_id] = self

    @property
    def cac(self) -> ResistiveHeaterCac:
        return ResistiveHeaterCac.by_id[self.component_attribute_class_id]

    @property
    def make_model(self) -> MakeModel:
        return self.cac.make_model

    def __repr__(self):
        return f"{self.display_name}  ({self.cac.make_model.value})"
