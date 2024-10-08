from enum import auto
from typing import Optional

from gw.enums import GwStrEnum


class FsmActionType(GwStrEnum):
    """
    A list of the finite state machine Actions that a spaceheat node might take. An Action,
    in this context, is a side-effect of a state machine transition that impacts the real world
    (i.e., a relay is actuated).

    Enum sh.fsm.action.type version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shfsmactiontype)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)

    Values:
      - RelayPinSet
      - Analog010VSignalSet
      - Analog420maSignalSet
    """

    RelayPinSet = auto()
    Analog010VSignalSet = auto()
    Analog420maSignalSet = auto()

    @classmethod
    def default(cls) -> "FsmActionType":
        """
        Returns default value (in this case RelayPinSet)
        """
        return cls.RelayPinSet

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
        The name in the GridWorks Type Registry (sh.fsm.action.type)
        """
        return "sh.fsm.action.type"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"


value_to_version = {
    "RelayPinSet": "000",
    "Analog010VSignalSet": "000",
    "Analog420maSignalSet": "000",
}
