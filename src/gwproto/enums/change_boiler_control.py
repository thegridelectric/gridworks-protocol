from fastapi_utils.enums import StrEnum
from enum import auto


class ChangeBoilerControl(StrEnum):
    """
    
    """
    SwitchToTankAquastat = auto()
    SwitchToScada = auto()

    @classmethod
    def default(cls) -> "ChangeBoilerControl":
        return cls.SwitchToTankAquastat

    @classmethod
    def enum_name(cls) -> str:
        return "change.boiler.control"
