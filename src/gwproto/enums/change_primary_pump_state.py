
# Literal Enum: 
#  - no additional values can be added over time.
#  - Sent as-is, not in hex symbol
from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangePrimaryPumpState(StrEnum):
    """
    Either forces the heat pump's primary circulator pump off, or allows the heat pump to turn
    on its circulatory pumpprimary pump
    """

    TurnPumpOn = auto()
    TurnPumpOff = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangePrimaryPumpState":
        return cls.TurnPumpOn

    @classmethod
    def enum_name(cls) -> str:
        return "change.primary.pump.state"
