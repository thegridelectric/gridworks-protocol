import json
import typing
from typing import Any
from typing import Dict
from typing import Literal

from gridworks.property_format import predicate_validator

from gwproto.data_classes.component import Component
from gwproto.data_classes.components.hubitat_component import HubitatComponent
from gwproto.types.component_gt import ComponentGt
from gwproto.types.rest_poller_gt import URLArgs
from gwproto.types.rest_poller_gt import URLConfig
from gwproto.utils import has_mac_address_format


class HubitatComponentGt(ComponentGt):
    Host: str
    MakerApiId: int
    AccessToken: str
    MacAddress: str
    TypeName: Literal["hubitat.component.gt"] = "hubitat.component.gt"

    _is_mac_address = predicate_validator("MacAddress", has_mac_address_format)

    def as_dict(self) -> Dict[str, Any]:
        return self.dict(exclude_unset=True)

    def as_type(self) -> str:
        return json.dumps(self.as_dict())

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

    def url_config(self) -> URLConfig:
        return URLConfig(
            url_args=URLArgs(
                scheme="http",
                host=self.Host,
                query=[("access_token", self.AccessToken)],
            ),
            url_path_format="/apps/api/{app_id}",
            url_path_args={"app_id": self.MakerApiId},
        )

    def maker_api_url_config(self) -> URLConfig:
        config = self.url_config()
        if config.url_args.query is None:
            config.url_args.query = []
        config.url_args.query.append(("access_token", self.AccessToken))
        if config.url_path_format is None:
            config.url_path_format = ""
        config.url_path_format += "/apps/api/{app_id}"
        if config.url_path_args is None:
            config.url_path_args = {}
        config.url_path_args.update({"app_id": self.MakerApiId})
        return config

    @classmethod
    def from_data_class(cls, component: HubitatComponent) -> "HubitatComponentGt":
        return HubitatComponentGt(
            ComponentId=component.component_id,
            ComponentAttributeClassId=component.component_attribute_class_id,
            Host=component.host,
            MakerApiId=component.maker_api_id,
            AccessToken=component.access_token,
            DisplayName=component.display_name,
            HwUid=component.hw_uid,
            MacAddress=component.mac_address,
        )

    def to_data_class(self) -> HubitatComponent:
        component = Component.by_id.get(self.ComponentId, None)
        if component is not None:
            return typing.cast(HubitatComponent, component)
        return HubitatComponent(
            component_id=self.ComponentId,
            component_attribute_class_id=self.ComponentAttributeClassId,
            host=self.Host,
            maker_api_id=self.MakerApiId,
            access_token=self.AccessToken,
            display_name=self.DisplayName,
            hw_uid=self.HwUid,
            mac_address=self.MacAddress,
        )


class HubitatRESTResolutionSettings:
    component_gt: HubitatComponentGt
    maker_api_url_config: URLConfig

    def __init__(self, component_gt: HubitatComponentGt):
        self.component_gt = component_gt
        self.maker_api_url_config = self.component_gt.maker_api_url_config()


class HubitatComponentGt_Maker:
    type_name: str = HubitatComponentGt.__fields__["TypeName"].default
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
