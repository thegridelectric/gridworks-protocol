from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangePrimaryPumpControl(StrEnum):
    """
    Change control between a fallback analog system and SCADA
    """

    SwitchToHeatPump = auto()
    SwitchToScada = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangePrimaryPumpControl":
        return cls.SwitchToHeatPump

    @classmethod
    def enum_name(cls) -> str:
        return "change.primary.pump.control"
