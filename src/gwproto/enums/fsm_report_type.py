from enum import auto
from typing import Optional

from gw.enums import GwStrEnum


class FsmReportType(GwStrEnum):
    """


    Enum fsm.report.type version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#fsmreporttype)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)

    Values:
      - Other
      - Event
      - Action
    """

    Other = auto()
    Event = auto()
    Action = auto()

    @classmethod
    def default(cls) -> "FsmReportType":
        """
        Returns default value (in this case Other)
        """
        return cls.Other

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
        The name in the GridWorks Type Registry (fsm.report.type)
        """
        return "fsm.report.type"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"


value_to_version = {
    "Other": "000",
    "Event": "000",
    "Action": "000",
}
