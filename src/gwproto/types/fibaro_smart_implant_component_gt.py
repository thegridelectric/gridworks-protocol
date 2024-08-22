import json
import typing
from typing import Any, Literal

from gw.utils import snake_to_pascal
from pydantic import ConfigDict

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.fibaro_smart_implant_component import (
    FibaroSmartImplantComponent,
)
from gwproto.types import ComponentGt


class FibaroSmartImplantComponentGt(ComponentGt):
    z_wave_dsk: str = ""
    type_name: Literal["fibaro.smart.implant.component.gt"] = (
        "fibaro.smart.implant.component.gt"
    )
    version: Literal["000"] = "000"
    model_config = ConfigDict(populate_by_name=True, alias_generator=snake_to_pascal)

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

    @classmethod
    def from_data_class(
        cls, component: FibaroSmartImplantComponent
    ) -> "FibaroSmartImplantComponentGt":
        return FibaroSmartImplantComponentGt(
            component_id=component.component_id,
            component_attribute_class_id=component.component_attribute_class_id,
            display_name=component.display_name,
            hw_uid=component.hw_uid,
        )

    def to_data_class(self) -> FibaroSmartImplantComponent:
        component = Component.by_id.get(self.component_id, None)
        if component is not None:
            return typing.cast(FibaroSmartImplantComponent, component)
        return FibaroSmartImplantComponent(
            component_id=self.component_id,
            component_attribute_class_id=self.component_attribute_class_id,
            display_name=self.display_name,
            hw_uid=self.hw_uid,
        )


class FibaroSmartImplantComponentGtMaker:
    type_name: str = FibaroSmartImplantComponentGt.model_fields["type_name"].default
    version = "000"
    tuple: FibaroSmartImplantComponentGt

    def __init__(self, component: FibaroSmartImplantComponent):
        self.tuple = FibaroSmartImplantComponentGt.from_data_class(component)

    @classmethod
    def tuple_to_type(cls, tpl: FibaroSmartImplantComponentGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> FibaroSmartImplantComponentGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> FibaroSmartImplantComponentGt:
        return FibaroSmartImplantComponentGt(**d)

    @classmethod
    def tuple_to_dc(
        cls, t: FibaroSmartImplantComponentGt
    ) -> FibaroSmartImplantComponent:
        return t.to_data_class()

    @classmethod
    def dc_to_tuple(
        cls, dc: FibaroSmartImplantComponent
    ) -> FibaroSmartImplantComponentGt:
        return FibaroSmartImplantComponentGt.from_data_class(dc)

    @classmethod
    def type_to_dc(cls, t: str) -> FibaroSmartImplantComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: FibaroSmartImplantComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> FibaroSmartImplantComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
