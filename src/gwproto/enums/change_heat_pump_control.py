from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangeHeatPumpControl(StrEnum):
    """
    Change control between a fallback analog system and SCADA
    """

    SwitchToTankAquastat = auto()
    SwitchToScada = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangeHeatPumpControl":
        return cls.SwitchToTankAquastat

    @classmethod
    def enum_name(cls) -> str:
        return "change.heat.pump.control"
