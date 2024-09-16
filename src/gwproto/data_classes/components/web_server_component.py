from gwproto.data_classes.components.component import Component
from gwproto.types.web_server_cac_gt import WebServerCacGt
from gwproto.types.web_server_component_gt import WebServerComponentGt
from gwproto.types.web_server_gt import WebServerGt


class WebServerComponent(Component[WebServerComponentGt, WebServerCacGt]):
    @property
    def web_server_gt(self) -> WebServerGt:
        return self.gt.WebServer
