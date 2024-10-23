from enum import auto
from typing import List

from gw.enums import GwStrEnum


class GpmFromHzMethod(GwStrEnum):
    Constant = auto()

    @classmethod
    def default(cls) -> "GpmFromHzMethod":
        return cls.Constant

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "gpm.from.hz.method"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
