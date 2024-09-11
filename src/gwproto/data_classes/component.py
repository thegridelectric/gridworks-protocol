"""SCADA Component Class Definition"""

from abc import ABC
from typing import Any, Dict, Optional

from gwproto.data_classes.mixin import StreamlinedSerializerMixin
from gwproto.enums import MakeModel


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
        cac: Any = None,  # noqa: ANN401
    ) -> None:
        self.component_id = component_id
        self.display_name = display_name
        self.component_attribute_class_id = component_attribute_class_id
        self.hw_uid = hw_uid
        self.cac = cac

    @property
    def component_attribute_class(self) -> Any:  # noqa: ANN401
        return self.cac

    @property
    def make_model(self) -> MakeModel:
        return self.cac.MakeModel

    def __repr__(self) -> str:
        return self.display_name
