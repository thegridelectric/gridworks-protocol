from typing import Literal

from gwproto.named_types.component_gt import ComponentGt
from gwproto.named_types.web_server_gt import WebServerGt


class WebServerComponentGt(ComponentGt):
    web_server: WebServerGt
    type_name: Literal["web.server.component.gt"] = "web.server.component.gt"
