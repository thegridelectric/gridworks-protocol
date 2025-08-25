from enum import auto

from gw.enums import GwStrEnum


class AdminState(GwStrEnum):
    """

    Values:
      - Awake
      - Dormant

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/admin.state.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    Awake = auto()
    Dormant = auto()

    @classmethod
    def default(cls) -> "AdminState":
        return cls.Dormant

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "admin.state"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
