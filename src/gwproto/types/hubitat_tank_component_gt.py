import copy
import json
import typing
from typing import Any, Literal

from gw.utils import snake_to_pascal

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.hubitat_tank_component import HubitatTankComponent
from gwproto.types.component_gt import ComponentGt
from gwproto.types.hubitat_tank_gt import HubitatTankSettingsGt


class HubitatTankComponentGt(ComponentGt):
    tank: HubitatTankSettingsGt
    type_name: Literal["hubitat.tank.component.gt"] = "hubitat.tank.component.gt"
    version: Literal["000"] = "000"

    class Config:
        populate_by_name = True
        alias_generator = snake_to_pascal

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

    @classmethod
    def from_data_class(
        cls, component: HubitatTankComponent
    ) -> "HubitatTankComponentGt":
        return HubitatTankComponentGt(
            component_id=component.component_id,
            component_attribute_class_id=component.component_attribute_class_id,
            tank=HubitatTankSettingsGt(
                hubitat_component_id=component.hubitat.component_id,
                devices=copy.deepcopy(component.devices),
            ),
            display_name=component.display_name,
            hw_uid=component.hw_uid,
        )

    def to_data_class(self) -> HubitatTankComponent:
        component = Component.by_id.get(self.component_id, None)
        if component is not None:
            return typing.cast(HubitatTankComponent, component)
        return HubitatTankComponent(
            component_id=self.component_id,
            component_attribute_class_id=self.component_attribute_class_id,
            tank_gt=self.tank,
            display_name=self.display_name,
            hw_uid=self.hw_uid,
        )


class HubitatTankComponentGtMaker:
    type_name: str = HubitatTankComponentGt.model_fields["type_name"].default
    version = "000"
    tuple: HubitatTankComponentGt

    def __init__(self, component: HubitatTankComponent):
        self.tuple = HubitatTankComponentGt.from_data_class(component)

    @classmethod
    def tuple_to_type(cls, tpl: HubitatTankComponentGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> HubitatTankComponentGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> HubitatTankComponentGt:
        return HubitatTankComponentGt(**d)

    @classmethod
    def tuple_to_dc(cls, t: HubitatTankComponentGt) -> HubitatTankComponent:
        return t.to_data_class()

    @classmethod
    def dc_to_tuple(cls, dc: HubitatTankComponent) -> HubitatTankComponentGt:
        return HubitatTankComponentGt.from_data_class(dc)

    @classmethod
    def type_to_dc(cls, t: str) -> HubitatTankComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: HubitatTankComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> HubitatTankComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
