from enum import auto

from gw.enums import GwStrEnum


class FsmReportType(GwStrEnum):
    """

    Values:
      - Other
      - Event
      - Action

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/fsm.report.type.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    Other = auto()
    Event = auto()
    Action = auto()

    @classmethod
    def default(cls) -> "FsmReportType":
        return cls.Other

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "fsm.report.type"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
