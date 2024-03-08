from fastapi_utils.enums import StrEnum
from enum import auto


class RelayClosedOrOpen(StrEnum):
    """
    These are fsm states (as opposed to readings from a pin).
    """
    RelayClosed = auto()
    RelayOpen = auto()

    @classmethod
    def default(cls) -> "RelayClosedOrOpen":
        return cls.RelayClosed

    @classmethod
    def enum_name(cls) -> str:
        return "relay.closed.or.open"
