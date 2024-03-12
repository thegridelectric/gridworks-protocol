from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangeValveState(StrEnum):
    """
    Events used in the IsoValve finite state machine.
    """
    OpenValve = auto()
    CloseValve = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangeValveState":
        return cls.OpenValve

    @classmethod
    def enum_name(cls) -> str:
        return "change.valve.state"
