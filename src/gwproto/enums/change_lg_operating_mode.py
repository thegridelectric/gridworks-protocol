from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangeLgOperatingMode(StrEnum):
    """
    Clarifies the request and the action in changing between lg.operating.modes
    """
    SwitchToDhw = auto()
    SwitchToHeat = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangeLgOperatingMode":
        return cls.SwitchToHeat

    @classmethod
    def enum_name(cls) -> str:
        return "change.lg.operating.mode"
