from enum import auto
from typing import Optional

from gw.enums import GwStrEnum


class FsmName(GwStrEnum):
    """
    The name of a specific Spaceheat finite state machine. That name is used as a literal enum
    for a set of staets.

    Enum sh.fsm.name version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shfsmname)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/house-0.html)

    Values:
      - Unknown
      - StoreFlowDirection
      - RelayState: Finite State Machine for a normally open or normally closed relay
        whose states (Closed, Open) are enumerated by RelayClosedOrOpen.
      - RelayPinState: Finite State Machine for a relay pin with states enumerated by
        RelayEnergizationState (Energized and DeEnergized).
    """

    Unknown = auto()
    StoreFlowDirection = auto()
    RelayState = auto()
    RelayPinState = auto()

    @classmethod
    def default(cls) -> "FsmName":
        """
        Returns default value (in this case StoreFlowDirection)
        """
        return cls.StoreFlowDirection

    @classmethod
    def version(cls, value: Optional[str] = None) -> str:
        if value is None:
            return "000"
        if not isinstance(value, str):
            raise TypeError("This method applies to strings, not enums")
        if value not in value_to_version:
            raise ValueError(f"Unknown enum value: {value}")
        return value_to_version[value]

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (sh.fsm.name)
        """
        return "sh.fsm.name"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"


value_to_version = {
    "Unknown": "000",
    "StoreFlowDirection": "000",
    "RelayState": "000",
    "RelayPinState": "000",
}
