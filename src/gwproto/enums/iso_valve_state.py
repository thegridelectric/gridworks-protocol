from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class IsoValveState(StrEnum):
    """
    The list of states associated to the House 0 "IsoValve" Finite State Machine.
    """
    Open = auto()
    Closing = auto()
    Closed = auto()
    Opening = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "IsoValveState":
        return cls.Open

    @classmethod
    def enum_name(cls) -> str:
        return "iso.valve.state"
