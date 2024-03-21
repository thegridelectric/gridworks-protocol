from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangeAquastatControl(StrEnum):
    """
    
    """

    SwitchToBoiler = auto()
    SwitchToScada = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangeAquastatControl":
        return cls.SwitchToBoiler

    @classmethod
    def enum_name(cls) -> str:
        return "change.aquastat.control"
