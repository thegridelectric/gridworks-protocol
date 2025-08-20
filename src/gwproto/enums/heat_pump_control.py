from enum import auto

from gw.enums import GwStrEnum


class HeatPumpControl(GwStrEnum):
    """

    Values:
      - BufferTankAquastat
      - Scada

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/heat.pump.control.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    BufferTankAquastat = auto()
    Scada = auto()

    @classmethod
    def default(cls) -> "HeatPumpControl":
        return cls.BufferTankAquastat

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "heat.pump.control"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
