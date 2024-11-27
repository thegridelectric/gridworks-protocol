from enum import auto

from gw.enums import GwStrEnum


class MainAutoEvent(GwStrEnum):
    AtnLinkDead = auto()
    GoDormant = auto()
    WakeUp = auto()

    @classmethod
    def enum_name(cls) -> str:
        return "top.event"
