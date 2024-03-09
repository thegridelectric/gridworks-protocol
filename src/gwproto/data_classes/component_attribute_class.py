""" ComponentAttributeClass"""
from abc import ABC
from typing import Dict
from typing import Optional

from gwproto.data_classes.mixin import StreamlinedSerializerMixin
from gwproto.enums import MakeModel


class ComponentAttributeClass(ABC, StreamlinedSerializerMixin):
    by_id: Dict[str, "ComponentAttributeClass"] = {}

    base_props = []
    base_props.append("component_attribute_class_id")
    base_props.append("make_model")
    base_props.append("display_name")
    base_props.append("min_poll_period_ms")

    def __new__(cls, component_attribute_class_id, *args, **kwargs):
        try:
            return cls.by_id[component_attribute_class_id]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[component_attribute_class_id] = instance
            return instance

    def __init__(self, 
                 component_attribute_class_id: str, 
                 make_model: MakeModel = MakeModel.UNKNOWNMAKE__UNKNOWNMODEL,
                 display_name: Optional[str] = None,
                 min_poll_period_ms: Optional[int] = None,
    ):
        self.component_attribute_class_id = component_attribute_class_id
        self.make_model = make_model
        self.display_name = display_name
        self.min_poll_period_ms = min_poll_period_ms

    def __repr__(self):
        if self.display_name:
            return f"{self.display_name} ({self.make_model.value})"
        else:
            return f"{self.make_model.value} ({self.component_attribute_class_id})"
