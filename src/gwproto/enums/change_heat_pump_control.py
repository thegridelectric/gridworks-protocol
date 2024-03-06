from fastapi_utils.enums import StrEnum
from enum import auto


class ChangeHeatPumpControl(StrEnum):
    """
    Change control between a fallback analog system and SCADA
    """
    SwitchToTankAquastat = auto()
    SwitchToScada = auto()

    @classmethod
    def default(cls) -> "ChangeHeatPumpControl":
        return cls.SwitchToTankAquastat

    @classmethod
    def enum_name(cls) -> str:
        return "change.heat.pump.control"
