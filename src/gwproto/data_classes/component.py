""" SCADA Component Class Definition """

from abc import ABC
from typing import Dict
from typing import List
from typing import Optional

from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.data_classes.mixin import StreamlinedSerializerMixin


#from gwproto.types.channel_config import ChannelConfig


class Component(ABC, StreamlinedSerializerMixin):
    by_id: Dict[str, "Component"] = {}
    base_props = []
    base_props.append("component_id")
    base_props.append("component_attribute_class_id")
    base_props.append("config_list")
    base_props.append("display_name")
    base_props.append("hw_uid")

    def __new__(cls, component_id, *args, **kwargs):
        try:
            return cls.by_id[component_id]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[component_id] = instance
            return instance

    def __init__(
        self,
        component_id: str,
        component_attribute_class_id: str,
        config_list: Optional[List[str]] = None,
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ):
        self.component_id = component_id
        self.component_attribute_class_id = component_attribute_class_id
        self.config_list = config_list
        self.display_name = display_name
        self.hw_uid = hw_uid

    @property
    def component_attribute_class(self) -> ComponentAttributeClass:
        return ComponentAttributeClass.by_id[self.component_attribute_class_id]

    def __repr__(self):
        return self.display_name
