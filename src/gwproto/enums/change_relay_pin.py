from enum import auto
from typing import List
from fastapi_utils.enums import StrEnum


class ChangeRelayPin(StrEnum):
    """
    Clarifies the request sent to an internal multiplexing  actor regarding
    a single relay on a relay board
    """
    DeEnergize = auto()
    Energize = auto()

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def default(cls) -> "ChangeRelayPin":
        return cls.DeEnergize

    @classmethod
    def enum_name(cls) -> str:
        return "change.relay.pin"
