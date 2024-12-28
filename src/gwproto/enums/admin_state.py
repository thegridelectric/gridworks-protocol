from enum import auto
from typing import List

from gw.enums import GwStrEnum


class AdminState(GwStrEnum):
    """

    Values:
      - Awake
      - Dormant

    For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#adminstate)
    """

    Awake = auto()
    Dormant = auto()

    @classmethod
    def default(cls) -> "AdminState":
        return cls.Dormant

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "admin.state"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
