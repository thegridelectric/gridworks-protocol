"""SCADA Component Class Definition"""

from abc import ABC
from typing import Dict, Optional

from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.data_classes.mixin import StreamlinedSerializerMixin


class Component(ABC, StreamlinedSerializerMixin):
    by_id: Dict[str, "Component"] = {}  # noqa: RUF012
    base_props = [  # noqa: RUF012
        "component_id",
        "display_name",
        "component_attribute_class_id",
        "hw_uid",
    ]

    def __new__(cls, component_id, *args, **kwargs) -> "Component":  # noqa: ANN001, ANN002, ANN003, ARG003
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
        display_name: Optional[str] = None,
        hw_uid: Optional[str] = None,
    ) -> None:
        self.component_id = component_id
        self.display_name = display_name
        self.component_attribute_class_id = component_attribute_class_id
        self.hw_uid = hw_uid

    @property
    def component_attribute_class(self) -> ComponentAttributeClass:
        return ComponentAttributeClass.by_id[self.component_attribute_class_id]

    def __repr__(self) -> str:
        return self.display_name
