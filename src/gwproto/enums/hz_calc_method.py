from enum import auto
from typing import List

from gw.enums import GwStrEnum


class HzCalcMethod(GwStrEnum):
    """

    Values:
      - BasicExpWeightedAvg
      - BasicButterWorth

    For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#hzcalcmethod)
    """

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
        return "hz.calc.method"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
