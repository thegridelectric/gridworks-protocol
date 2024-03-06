from fastapi_utils.enums import StrEnum
from enum import auto


class ChangeHeatcallSource(StrEnum):
    """
    Used for dispatch/actions between the two states of a double-throw failsafe relay that toggles
    between the SCADA and a Thermostat for controlling the heat call to a zone.
    """
    SwitchToWallThermostat = auto()
    SwitchToScada = auto()

    @classmethod
    def default(cls) -> "ChangeHeatcallSource":
        return cls.SwitchToWallThermostat

    @classmethod
    def enum_name(cls) -> str:
        return "change.heatcall.source"
