""" SCADA Component Class Definition """

from abc import ABC
from typing import Dict
from typing import List
from typing import Optional

from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.data_classes.mixin import StreamlinedSerializerMixin
from gwproto.enums import TelemetryName


class DataChannel(ABC, StreamlinedSerializerMixin):
    by_id: Dict[str, "DataChannel"] = {}
    by_name: Dict[str, "DataChannel"] = {}
    base_props = []
    base_props.append("name")
    base_props.append("display_name")
    base_props.append("about_node_name")
    base_props.append("captured_by_node_name")
    base_props.append("telemetry_name")
    base_props.append("id")

    def __new__(cls, display_name, id, *args, **kwargs):
        try:
            return cls.by_name[display_name]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[id] = instance
            cls.by_name[display_name] = instance
            return instance

    def __init__(
        self,
        name: str,
        display_name: str,
        about_node_name: str,
        captured_by_node_name: str,
        telemetry_name: TelemetryName,
        id: str,
    ):
        self.name = name
        self.display_name = display_name
        self.about_node_name = about_node_name
        self.captured_by_node_name = captured_by_node_name
        self.telemetry_name = telemetry_name
        self.id = id

    def __repr__(self):
        return self.display_name
