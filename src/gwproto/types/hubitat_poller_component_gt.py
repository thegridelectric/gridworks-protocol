import copy
import json
import typing
from typing import Any, Literal

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.hubitat_poller_component import (
    HubitatPollerComponent,
)
from gwproto.types.component_gt import ComponentGt
from gwproto.types.hubitat_poller_gt import HubitatPollerGt


class HubitatPollerComponentGt(ComponentGt):
    poller: HubitatPollerGt
    type_name: Literal["hubitat.poller.component.gt"] = "hubitat.poller.component.gt"
    version: Literal["000"] = "000"

    @classmethod
    def from_data_class(
        cls, component: HubitatPollerComponent
    ) -> "HubitatPollerComponentGt":
        return HubitatPollerComponentGt(
            component_id=component.component_id,
            component_attribute_class_id=component.component_attribute_class_id,
            poller=copy.deepcopy(component.poller_gt),
            display_name=component.display_name,
            hw_uid=component.hw_uid,
        )

    def to_data_class(self) -> HubitatPollerComponent:
        component = Component.by_id.get(self.component_id, None)
        if component is not None:
            return typing.cast(HubitatPollerComponent, component)
        return HubitatPollerComponent(
            component_id=self.component_id,
            component_attribute_class_id=self.component_attribute_class_id,
            poller_gt=copy.deepcopy(self.poller),
            display_name=self.display_name,
            hw_uid=self.hw_uid,
        )


class HubitatPollerComponentGtMaker:
    type_name = "hubitat.poller.component.gt"
    version = "000"

    @classmethod
    def tuple_to_type(cls, tpl: HubitatPollerComponentGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> HubitatPollerComponentGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> HubitatPollerComponentGt:
        return HubitatPollerComponentGt(**d)
