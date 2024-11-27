from enum import auto
from typing import List

from gw.enums import GwStrEnum


class MainAutoEvent(GwStrEnum):
    """

    Values:
      - AtnLinkDead
      - AtnLinkAlive
      - GoDormant
      - WakeUp

    For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#mainautoevent)
    """

    AtnLinkDead = auto()
    AtnLinkAlive = auto()
    GoDormant = auto()
    WakeUp = auto()

    @classmethod
    def default(cls) -> "MainAutoEvent":
        return cls.GoDormant

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "main.auto.event"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
