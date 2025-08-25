from enum import auto

from gw.enums import GwStrEnum


class GpmFromHzMethod(GwStrEnum):
    """

    Values:
      - Constant

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/gpm.from.hz.method.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    Constant = auto()

    @classmethod
    def default(cls) -> "GpmFromHzMethod":
        return cls.Constant

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "gpm.from.hz.method"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
