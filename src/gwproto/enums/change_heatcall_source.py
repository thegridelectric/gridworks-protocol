from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangeHeatcallSource(StrEnum):
    """
    Used for dispatch/actions between the two states of a double-throw failsafe relay that toggles
    between the SCADA and a Thermostat for controlling the heat call to a zone.
    """

    SwitchToWallThermostat = auto()
    SwitchToScada = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangeHeatcallSource":
        return cls.SwitchToWallThermostat

    @classmethod
    def enum_name(cls) -> str:
        return "change.heatcall.source"