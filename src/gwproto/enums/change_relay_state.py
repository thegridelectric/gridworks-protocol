from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class ChangeRelayState(StrEnum):
    """
    This is meant for relays in either NormallyOpen or NormallyClosed configuration (i.e. not
    configured as DoubleThrow). It provides the natural Finite State Machine actions that go
    along with simple.relay.state states of RelayOpen and RelayClosed. Open = PowerOff = 0 and
    Closed = PowerOn = 1
    """
    TurnOn = auto()
    TurnOff = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangeRelayState":
        return cls.TurnOff

    @classmethod
    def enum_name(cls) -> str:
        return "change.relay.state"
