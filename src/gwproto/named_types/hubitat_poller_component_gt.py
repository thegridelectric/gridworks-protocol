from typing import Literal

from gwproto.named_types.component_gt import ComponentGt
from gwproto.named_types.hubitat_poller_gt import HubitatPollerGt


class HubitatPollerComponentGt(ComponentGt):
    poller: HubitatPollerGt
    type_name: Literal["hubitat.poller.component.gt"] = "hubitat.poller.component.gt"
