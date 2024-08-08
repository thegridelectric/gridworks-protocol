import json
import typing
from typing import Any, Literal, Optional

import yarl
from gw.utils import snake_to_pascal

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.hubitat_component import HubitatComponent
from gwproto.types.component_gt import ComponentGt
from gwproto.types.hubitat_gt import HubitatGt
from gwproto.types.rest_poller_gt import URLConfig


class HubitatComponentGt(ComponentGt):
    hubitat: HubitatGt
    type_name: Literal["hubitat.component.gt"] = "hubitat.component.gt"
    version: Literal["000"] = "000"

    class Config:
        populate_by_name = True
        alias_generator = snake_to_pascal

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa

    def url_config(self) -> URLConfig:
        return self.hubitat.url_config()

    def maker_api_url_config(self) -> URLConfig:
        return self.hubitat.maker_api_url_config()

    def urls(self) -> dict[str, Optional[yarl.URL]]:
        return self.hubitat.urls()

    def refresh_url_config(self, device_id: int) -> URLConfig:
        return self.hubitat.refresh_url_config(device_id)

    def refresh_url(self, device_id: int) -> yarl.URL:
        return self.hubitat.refresh_url(device_id)

    @classmethod
    def from_data_class(cls, component: HubitatComponent) -> "HubitatComponentGt":
        return HubitatComponentGt(
            ComponentId=component.component_id,
            ComponentAttributeClassId=component.component_attribute_class_id,
            hubitat=component.hubitat_gt,
            DisplayName=component.display_name,
            HwUid=component.hw_uid,
        )

    def to_data_class(self) -> HubitatComponent:
        component = Component.by_id.get(self.component_id, None)
        if component is not None:
            return typing.cast(HubitatComponent, component)
        return HubitatComponent(
            component_id=self.component_id,
            component_attribute_class_id=self.component_attribute_class_id,
            hubitat_gt=self.hubitat,
            display_name=self.display_name,
            hw_uid=self.hw_uid,
        )

    @classmethod
    def make_stub(cls, component_id):
        return HubitatComponentGt(
            ComponentId=component_id,
            ComponentAttributeClassId="00000000-0000-0000-0000-000000000000",
            hubitat=HubitatGt(
                Host="",
                MakerApiId=-1,
                AccessToken="",
                MacAddress="000000000000",
            ),
        )

    @classmethod
    def from_component_id(
        cls, component_id: str, components: dict[str, Component]
    ) -> "HubitatComponent":
        hubitat_component = components.get(component_id, None)
        if hubitat_component is None:
            raise ValueError(
                "ERROR. No component found for "
                f"HubitatTankComponent.hubitat.CompnentId {component_id}"
            )
        if not isinstance(hubitat_component, HubitatComponent):
            raise ValueError(
                "ERROR. Referenced hubitat component has type "
                f"{type(hubitat_component)}; "
                "must be instance of HubitatComponent. "
                f"Hubitat component id: {component_id}"
            )
        return hubitat_component


class HubitatRESTResolutionSettings:
    component_gt: HubitatComponentGt
    maker_api_url_config: URLConfig

    def __init__(self, component_gt: HubitatComponentGt):
        self.component_gt = component_gt
        self.maker_api_url_config = self.component_gt.maker_api_url_config()


class HubitatComponentGtMaker:
    type_name: str = HubitatComponentGt.model_fields["type_name"].default
    version = "000"
    tuple: HubitatComponentGt

    def __init__(self, component: HubitatComponent):
        self.tuple = HubitatComponentGt.from_data_class(component)

    @classmethod
    def tuple_to_type(cls, tpl: HubitatComponentGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> HubitatComponentGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> HubitatComponentGt:
        return HubitatComponentGt(**d)

    @classmethod
    def tuple_to_dc(cls, t: HubitatComponentGt) -> HubitatComponent:
        return t.to_data_class()

    @classmethod
    def dc_to_tuple(cls, dc: HubitatComponent) -> HubitatComponentGt:
        return HubitatComponentGt.from_data_class(dc)

    @classmethod
    def type_to_dc(cls, t: str) -> HubitatComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: HubitatComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> HubitatComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
