"""Code for actors that use a simple rest interaction, converting the response to one or more
REST commands into a message posted to main processing thread.

"""

import json
import typing
from typing import Any, Literal, Optional

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.rest_poller_component import RESTPollerComponent
from gwproto.types import ComponentGt
from gwproto.types.rest_poller_gt import RESTPollerSettings


class RestPollerComponentGt(ComponentGt):
    ComponentId: str
    ComponentAttributeClassId: str
    DisplayName: Optional[str] = None
    HwUid: Optional[str] = None
    Rest: RESTPollerSettings
    TypeName: Literal["rest.poller.component.gt"] = "rest.poller.component.gt"
    Version: Literal["000"] = "000"

    @classmethod
    def from_data_class(cls, component: RESTPollerComponent) -> "RestPollerComponentGt":
        return RestPollerComponentGt(
            component_id=component.component_id,
            component_attribute_class_id=component.component_attribute_class_id,
            display_name=component.display_name,
            hw_uid=component.hw_uid,
            rest=component.rest,
        )

    def to_data_class(self) -> RESTPollerComponent:
        component = Component.by_id.get(self.component_id, None)
        if component is not None:
            return typing.cast(RESTPollerComponent, component)
        return RESTPollerComponent(
            component_id=self.component_id,
            component_attribute_class_id=self.component_attribute_class_id,
            rest=self.rest,
            display_name=self.display_name,
            hw_uid=self.hw_uid,
        )


class RestPollerComponentGtMaker:
    type_name: str = RestPollerComponentGt.model_fields["TypeName"].default
    version = "000"
    tuple: RestPollerComponentGt

    def __init__(self, component: RESTPollerComponent):
        self.tuple = RestPollerComponentGt.from_data_class(component)

    @classmethod
    def tuple_to_type(cls, tpl: RestPollerComponentGt) -> str:
        return tpl.as_type()  # noqa

    @classmethod
    def type_to_tuple(cls, t: str) -> RestPollerComponentGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> RestPollerComponentGt:
        return RestPollerComponentGt(**d)

    @classmethod
    def tuple_to_dc(cls, t: RestPollerComponentGt) -> RESTPollerComponent:
        return t.to_data_class()

    @classmethod
    def dc_to_tuple(cls, dc: RESTPollerComponent) -> RestPollerComponentGt:
        return RestPollerComponentGt.from_data_class(dc)

    @classmethod
    def type_to_dc(cls, t: str) -> RESTPollerComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: RESTPollerComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()  # noqa

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> RESTPollerComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
