import json
import typing
from typing import Any, Literal

from gw.utils import snake_to_pascal

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.web_server_component import WebServerComponent
from gwproto.types.component_gt import ComponentGt
from gwproto.types.web_server_gt import WebServerGt


class WebServerComponentGt(ComponentGt):
    web_server: WebServerGt
    type_name: Literal["web.server.component.gt"] = "web.server.component.gt"
    version: Literal["000"] = "000"

    class Config:
        extra = "allow"
        populate_by_name = True
        alias_generator = snake_to_pascal

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa

    @classmethod
    def from_data_class(cls, component: WebServerComponent) -> "WebServerComponentGt":
        return WebServerComponentGt(
            component_id=component.component_id,
            component_attribute_class_id=component.component_attribute_class_id,
            web_server=component.web_server_gt,
            display_name=component.display_name,
            hw_uid=component.hw_uid,
        )

    def to_data_class(self) -> WebServerComponent:
        component = Component.by_id.get(self.component_id, None)
        if component is not None:
            return typing.cast(WebServerComponent, component)
        return WebServerComponent(
            component_id=self.component_id,
            component_attribute_class_id=self.component_attribute_class_id,
            web_server_gt=self.web_server,
            display_name=self.display_name,
            hw_uid=self.hw_uid,
        )


class WebServerComponentGtMaker:
    type_name = "web.server.component.gt"
    version = "001"

    @classmethod
    def tuple_to_type(cls, tpl: WebServerComponentGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> WebServerComponentGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> WebServerComponentGt:
        return WebServerComponentGt(**d)
