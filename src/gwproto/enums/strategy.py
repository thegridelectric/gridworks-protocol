from enum import auto

from gw.enums import GwStrEnum


class Strategy(GwStrEnum):
    """

    Values:
      - Ha2Oil: HomeAlone2 - Also a home alone strategy for House0. If the heat pump is
        not coming on, then switch to oil boiler. TODO: DESIGN, WRITE UP
      - Ha1: HomeAlone1 - the first home alone strategy for House0. TODO: WRITE UP

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/spaceheat.strategy.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    Ha2Oil = auto()
    Ha1 = auto()

    @classmethod
    def default(cls) -> "Strategy":
        return cls.Ha1

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "spaceheat.strategy"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
