"""Ads111xBasedCac definition"""

from typing import Dict
from typing import List
from typing import Optional

from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.enums import MakeModel
from gwproto.enums import TelemetryName


class Ads111xBasedCac(ComponentAttributeClass):
    by_id: Dict[str, "Ads111xBasedCac"] = {}

    def __init__(
        self,
        component_attribute_class_id: str,
        min_poll_period_ms: int,
        make_model: MakeModel,
        ads_i2c_address_list: List[str],
        total_terminal_blocks: int,
        telemetry_name_list: List[TelemetryName],
        display_name: Optional[str] = None,
    ):
        super(self.__class__, self).__init__(
            component_attribute_class_id=component_attribute_class_id,
            make_model=make_model,
            display_name=display_name,
        )
        self.min_poll_period_ms = min_poll_period_ms
        self.ads_i2c_address_list = ads_i2c_address_list
        self.total_terminal_blocks = total_terminal_blocks
        self.telemetry_name_list = telemetry_name_list

        Ads111xBasedCac.by_id[self.component_attribute_class_id] = self
        ComponentAttributeClass.by_id[self.component_attribute_class_id] = self

    def __repr__(self):
        return f"{self.make_model.value} {self.display_name}"
