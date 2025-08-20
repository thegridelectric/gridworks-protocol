from enum import auto

from gw.enums import GwStrEnum


class AquastatControl(GwStrEnum):
    """

    Values:
      - Boiler
      - Scada

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/aquastat.control.state.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    Boiler = auto()
    Scada = auto()

    @classmethod
    def default(cls) -> "AquastatControl":
        return cls.Boiler

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "aquastat.control.state"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
