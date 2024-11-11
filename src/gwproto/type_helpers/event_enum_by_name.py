from typing import Dict, Type

from gw.enums import GwStrEnum

from gwproto.enums import (
    ChangeAquastatControl,
    ChangeHeatcallSource,
    ChangeHeatPumpControl,
    ChangePrimaryPumpControl,
    ChangeRelayState,
    ChangeStoreFlowDirection,
)

EVENT_ENUM_BY_NAME: Dict[str, Type[GwStrEnum]] = {
    "ChangeAquastatControl": ChangeAquastatControl,
    "ChangeHeatPumpControl": ChangeHeatPumpControl,
    "ChangeHeatcallSource": ChangeHeatcallSource,
    "ChangePrimaryPumpControl": ChangePrimaryPumpControl,
    "ChangeRelayState": ChangeRelayState,
    "ChangeStoreFlowDirection": ChangeStoreFlowDirection,
}
