from enum import auto

from gw.enums import GwStrEnum


class HzCalcMethod(GwStrEnum):
    """

    Values:
      - BasicExpWeightedAvg
      - BasicButterWorth

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/hz.calc.method.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    BasicExpWeightedAvg = auto()
    BasicButterWorth = auto()

    @classmethod
    def default(cls) -> "HzCalcMethod":
        return cls.BasicExpWeightedAvg

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "hz.calc.method"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
