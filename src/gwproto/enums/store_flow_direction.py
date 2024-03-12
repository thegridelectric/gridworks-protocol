from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class StoreFlowDirection(StrEnum):
    """
    Used for a double-throw relay that can toggle between a thermal store heating up (flow is
    in the charging direction) or cooling down (flow is in the discharging direction). Events
    in the StoreFlowDirection finite state machine
    """
    Discharging = auto()
    ValveMovingToCharging = auto()
    Charging = auto()
    ValveMovingToDischarging = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "StoreFlowDirection":
        return cls.Discharging

    @classmethod
    def enum_name(cls) -> str:
        return "store.flow.direction.state"
