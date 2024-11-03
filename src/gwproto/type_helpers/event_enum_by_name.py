from typing import Dict

from gw.enums import GwStrEnum

from gwproto.enums import (
    ChangeAquastatControl,
    ChangeHeatcallSource,
    ChangeHeatPumpControl,
    ChangePrimaryPumpControl,
    ChangeRelayState,
    ChangeStoreFlowDirection,
)

EVENT_ENUM_BY_NAME: Dict[str, GwStrEnum] = {
    "ChangeAquastatControl": ChangeAquastatControl,
    "ChangeHeatPumpControl": ChangeHeatPumpControl,
    "ChangeHeatcallSource": ChangeHeatcallSource,
    "ChangePrimaryPumpControl": ChangePrimaryPumpControl,
    "ChangeRelayState": ChangeRelayState,
    "ChangeStoreFlowDirection": ChangeStoreFlowDirection,
}
