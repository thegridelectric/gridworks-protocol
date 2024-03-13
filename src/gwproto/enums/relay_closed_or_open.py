from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class RelayClosedOrOpen(StrEnum):
    """
    These are fsm states (as opposed to readings from a pin).
    """

    RelayClosed = auto()
    RelayOpen = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "RelayClosedOrOpen":
        return cls.RelayClosed

    @classmethod
    def enum_name(cls) -> str:
        return "relay.closed.or.open"
