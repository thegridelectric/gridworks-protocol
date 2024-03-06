from fastapi_utils.enums import StrEnum
from enum import auto


class ChangeLgOperatingMode(StrEnum):
    """
    Clarifies the request and the action in changing between lg.operating.modes
    """
    SwitchToDhw = auto()
    SwitchToHeat = auto()

    @classmethod
    def default(cls) -> "ChangeLgOperatingMode":
        return cls.SwitchToHeat

    @classmethod
    def enum_name(cls) -> str:
        return "change.lg.operating.mode"
