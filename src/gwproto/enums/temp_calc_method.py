from enum import auto

from gw.enums import GwStrEnum


class TempCalcMethod(GwStrEnum):
    """
    What method is used to calculate temperature as a function of voltage?
    Values:
      - SimpleBetaForPico: Use the Beta method for an NTC thermistor, with the (flawed)
        assumption that the pico which the thermistor is attached to has a fixed resistance.
        Requires parameters PicoResistance and ThermistorBeta.
      - SimpleBeta: Use the Beta method for an NTC thermistor. Requires ThermistorBeta
        as a parameter.

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/temp.calc.method.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    SimpleBetaForPico = auto()
    SimpleBeta = auto()

    @classmethod
    def default(cls) -> "TempCalcMethod":
        return cls.SimpleBeta

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "temp.calc.method"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
