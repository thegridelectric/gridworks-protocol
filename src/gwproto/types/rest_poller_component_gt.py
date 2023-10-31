"""Code for actors that use a simple rest interaction, converting the response to one or more
REST commands into a message posted to main processing thread.

"""
import json
import typing
from typing import Any
from typing import Dict
from typing import Optional

from pydantic import UUID4
from pydantic import BaseModel
from pydantic import validator

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.rest_poller_component import RESTPollerComponent
from gwproto.types.rest_poller_gt import RESTPollerSettings


class RESTPollerComponentGt(BaseModel):
    ComponentId: str
    ComponentAttributeClassId: str
    DisplayName: Optional[str] = None
    HwUid: Optional[str] = None
    Rest: RESTPollerSettings
    TypeName: typing.Literal["rest.poller.component.gt"] = "rest.poller.component.gt"

    @validator("ComponentId")
    def _check_component_id(cls, v: str) -> str:
        return str(UUID4(v))

    @validator("ComponentAttributeClassId")
    def _check_component_attribute_class_id(cls, v: str) -> str:
        return str(UUID4(v))

    def as_dict(self) -> Dict[str, Any]:
        return self.dict(exclude_unset=True)

    def as_type(self) -> str:
        return json.dumps(self.as_dict())

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

    @classmethod
    def from_data_class(cls, component: RESTPollerComponent) -> "RESTPollerComponentGt":
        return RESTPollerComponentGt(
            ComponentId=component.component_id,
            ComponentAttributeClassId=component.component_attribute_class_id,
            DisplayName=component.display_name,
            HwUid=component.hw_uid,
            Rest=component.rest,
        )

    def to_data_class(self) -> RESTPollerComponent:
        component = Component.by_id.get(self.ComponentId, None)
        if component is not None:
            return typing.cast(RESTPollerComponent, component)
        return RESTPollerComponent(
            component_id=self.ComponentId,
            component_attribute_class_id=self.ComponentAttributeClassId,
            rest=self.Rest,
            display_name=self.DisplayName,
            hw_uid=self.HwUid,
        )


class RESTPollerComponentGt_Maker:
    type_name: str = RESTPollerComponentGt.__fields__["TypeName"].default
    version = "000"
    tuple: RESTPollerComponentGt

    def __init__(self, component: RESTPollerComponent):
        self.tuple = RESTPollerComponentGt.from_data_class(component)

    @classmethod
    def tuple_to_type(cls, tpl: RESTPollerComponentGt) -> str:
        return tpl.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> RESTPollerComponentGt:
        return cls.dict_to_tuple(json.loads(t))

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> RESTPollerComponentGt:
        return RESTPollerComponentGt(**d)

    @classmethod
    def tuple_to_dc(cls, t: RESTPollerComponentGt) -> RESTPollerComponent:
        return t.to_data_class()

    @classmethod
    def dc_to_tuple(cls, dc: RESTPollerComponent) -> RESTPollerComponentGt:
        return RESTPollerComponentGt.from_data_class(dc)

    @classmethod
    def type_to_dc(cls, t: str) -> RESTPollerComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: RESTPollerComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> RESTPollerComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
