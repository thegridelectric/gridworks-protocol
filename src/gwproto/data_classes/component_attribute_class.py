""" ComponentAttributeClass"""

from abc import ABC
from typing import Dict
from typing import Optional

from gwproto.data_classes.mixin import StreamlinedSerializerMixin


class ComponentAttributeClass(ABC, StreamlinedSerializerMixin):
    by_id: Dict[str, "ComponentAttributeClass"] = {}

    base_props = ["component_attribute_class_id", "display_name"]

    def __new__(cls, component_attribute_class_id, *args, **kwargs):
        try:
            return cls.by_id[component_attribute_class_id]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[component_attribute_class_id] = instance
            return instance

    def __init__(
        self, component_attribute_class_id: str, display_name: Optional[str] = None
    ):
        self.component_attribute_class_id = component_attribute_class_id
        self.display_name = display_name

    def __repr__(self):
        return (
            self.display_name
            if self.display_name
            else self.component_attribute_class_id
        )
