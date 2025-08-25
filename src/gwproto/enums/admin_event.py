from enum import auto

from gw.enums import GwStrEnum


class AdminEvent(GwStrEnum):
    """

    Values:
      - WakeUp
      - GoDormant

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/admin.event.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    WakeUp = auto()
    GoDormant = auto()

    @classmethod
    def default(cls) -> "AdminEvent":
        return cls.WakeUp

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "admin.event"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
