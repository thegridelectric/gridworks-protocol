from enum import auto

from gw.enums import GwStrEnum


class KindOfParam(GwStrEnum):
    """
    Supports tracking and updating various key parameters for Spaceheat SCADA and AtomicTNodes.
    This is meant in particular for by-hand updates meant to be made and later reviewed by humans,
    as opposed to a careful and precise database update process.
    Values:
      - Other: A kind of parameter other than others articulated in the enumeration. This
        can of course change depending on the version of the enum. For version 000, it means
        any kind of parameter other than those in a .env file or in the hardware layout of a
        SCADA.
      - HardwareLayout: A key parameter embedded with the hardware layout object of a
        spaceheat SCADA. See for example https://github.com/thegridelectric/gw-scada-spaceheat-python.
      - DotEnv: A key parameter from the .env file of a spaceheat SCADA, or a spaceheat
        AtomicTNode.

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/spaceheat.kind.of.param.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    Other = auto()
    HardwareLayout = auto()
    DotEnv = auto()

    @classmethod
    def default(cls) -> "KindOfParam":
        return cls.Other

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "spaceheat.kind.of.param"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
