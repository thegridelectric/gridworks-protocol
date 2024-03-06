from fastapi_utils.enums import StrEnum
from enum import auto


class LgOperatingMode(StrEnum):
    """
    LG ThermaV and HydroKit heat pumps have the concept of being in different operating modes.
    This is used for a double-throw relay, so it can only ever have two states.
    """
    Dhw = auto()
    Heat = auto()

    @classmethod
    def default(cls) -> "LgOperatingMode":
        return cls.Heat

    @classmethod
    def enum_name(cls) -> str:
        return "lg.operating.mode"
