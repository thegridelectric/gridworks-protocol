from typing import Literal

from gwproto.named_types.component_gt import ComponentGt
from gwproto.named_types.hubitat_tank_gt import HubitatTankSettingsGt


class HubitatTankComponentGt(ComponentGt):
    tank: HubitatTankSettingsGt
    type_name: Literal["hubitat.tank.component.gt"] = "hubitat.tank.component.gt"
