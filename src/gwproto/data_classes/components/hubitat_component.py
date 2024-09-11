from typing import Optional

import yarl

from gwproto.data_classes.components.component import Component
from gwproto.types import HubitatCacGt, HubitatComponentGt


class HubitatComponent(Component[HubitatComponentGt, HubitatCacGt]):
    web_listener_nodes: set[str]

    def __init__(self, gt: HubitatComponentGt, cac: HubitatCacGt) -> None:
        super().__init__(gt, cac)
        self.web_listener_nodes = set()

    def urls(self) -> dict[str, Optional[yarl.URL]]:
        return self.gt.urls()

    def add_web_listener(self, web_listener_node: str) -> None:
        self.web_listener_nodes.add(web_listener_node)
