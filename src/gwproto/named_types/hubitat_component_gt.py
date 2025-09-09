from typing import Literal, Optional

import yarl
from pydantic_extra_types.mac_address import MacAddress

from gwproto.named_types.component_gt import ComponentGt
from gwproto.named_types.hubitat_gt import HubitatGt
from gwproto.named_types.rest_poller_gt import URLConfig


class HubitatComponentGt(ComponentGt):
    hubitat: HubitatGt
    type_name: Literal["hubitat.component.gt"] = "hubitat.component.gt"

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
    def make_stub(cls, component_id: str) -> "HubitatComponentGt":
        return HubitatComponentGt(
            component_id=component_id,
            component_attribute_class_id="00000000-0000-4000-8000-000000000000",
            hubitat=HubitatGt(
                Host="",
                MakerApiId=-1,
                AccessToken="",
                MacAddress=MacAddress("00:00:00:00:00:00"),
            ),
            ConfigList=[],
        )


class HubitatRESTResolutionSettings:
    component_gt: HubitatComponentGt
    maker_api_url_config: URLConfig

    def __init__(self, component_gt: HubitatComponentGt) -> None:
        self.component_gt = component_gt
        self.maker_api_url_config = self.component_gt.maker_api_url_config()
