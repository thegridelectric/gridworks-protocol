from typing import Optional

import yarl
from gw.utils import snake_to_pascal
from pydantic import BaseModel

from gwproto.types.rest_poller_gt import URLArgs, URLConfig
from gwproto.utils import has_mac_address_format, predicate_validator


class HubitatGt(BaseModel):
    host: str
    maker_api_id: int
    access_token: str
    mac_address: str
    web_listen_enabled: bool = True

    class Config:
        extra = "allow"
        populate_by_name = True
        alias_generator = snake_to_pascal

    _is_mac_address = predicate_validator("mac_address", has_mac_address_format)

    @property
    def listen_path(self) -> str:
        return self.mac_address.replace(":", "-")

    def listen_url(self, url: yarl.URL) -> yarl.URL:
        return url / self.listen_path

    def url_config(self) -> URLConfig:
        return URLConfig(
            url_args=URLArgs(
                scheme="http",
                host=self.host,
            ),
        )

    def maker_api_url_config(self) -> URLConfig:
        config = self.url_config()
        if config.url_args.query is None:
            config.url_args.query = []
        config.url_args.query.append(("access_token", self.access_token))
        if config.url_path_format is None:
            config.url_path_format = ""
        config.url_path_format += "/apps/api/{app_id}"
        if config.url_path_args is None:
            config.url_path_args = {}
        config.url_path_args.update({"app_id": self.maker_api_id})
        return config

    def devices_url_config(self) -> URLConfig:
        config = self.maker_api_url_config()
        config.url_path_format += "/devices"
        return config

    def url_configs(self) -> dict[str, URLConfig]:
        return dict(
            base=self.url_config(),
            maker_api=self.maker_api_url_config(),
            devices=self.devices_url_config(),
        )

    def urls(self) -> dict[str, Optional[yarl.URL]]:
        return {
            name: URLConfig.make_url(config)
            for name, config in self.url_configs().items()
        }

    def refresh_url_config(self, device_id: int) -> URLConfig:
        config = self.maker_api_url_config()
        config.url_path_format += "/devices/{device_id}/refresh"
        config.url_path_args["device_id"] = device_id
        return config

    def refresh_url(self, device_id: int) -> yarl.URL:
        return URLConfig.make_url(self.refresh_url_config(device_id))
