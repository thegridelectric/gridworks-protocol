from enum import auto

from gw.enums import GwStrEnum


class MainAutoState(GwStrEnum):
    Atn = auto()
    HomeAlone = auto()
    Dormant = auto()

    @classmethod
    def enum_name(cls) -> str:
        return "main.auto.state"
