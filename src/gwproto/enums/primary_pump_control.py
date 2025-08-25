from enum import auto

from gw.enums import GwStrEnum


class PrimaryPumpControl(GwStrEnum):
    """

    Values:
      - HeatPump
      - Scada

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/primary.pump.control.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    HeatPump = auto()
    Scada = auto()

    @classmethod
    def default(cls) -> "PrimaryPumpControl":
        return cls.HeatPump

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "primary.pump.control"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
