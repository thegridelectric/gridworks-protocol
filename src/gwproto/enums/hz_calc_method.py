from enum import auto
from typing import List

from gw.enums import GwStrEnum


class HzCalcMethod(GwStrEnum):
    BasicExpWeightedAvg = auto()
    BasicButterWorth = auto()

    @classmethod
    def default(cls) -> "HzCalcMethod":
        return cls.BasicExpWeightedAvg

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "temp.calc.method"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
