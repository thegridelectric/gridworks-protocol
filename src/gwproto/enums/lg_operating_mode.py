from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class LgOperatingMode(StrEnum):
    """
    LG ThermaV and HydroKit heat pumps have the concept of being in different operating modes.
    This is used for a double-throw relay, so it can only ever have two states.
    """

    Dhw = auto()
    Heat = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "LgOperatingMode":
        return cls.Heat

    @classmethod
    def enum_name(cls) -> str:
        return "lg.operating.mode"
