from enum import auto
from typing import Optional

from gw.enums import GwStrEnum


class KindOfParam(GwStrEnum):
    """
    Supports tracking and updating various key parameters for Spaceheat SCADA and AtomicTNodes.
    This is meant in particular for by-hand updates meant to be made and later reviewed by humans,
    as opposed to a careful and precise database update process.

    Enum spaceheat.kind.of.param version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#spaceheatkindofparam)

    Values:
      - Other: A kind of parameter other than others articulated in the enumeration. This
        can of course change depending on the version of the enum. For version 000, it means
        any kind of parameter other than those in a .env file or in the hardware layout of a
        SCADA.
      - HardwareLayout: A key parameter embedded with the hardware layout object of a
        spaceheat SCADA. See for example https://github.com/thegridelectric/gw-scada-spaceheat-python.
      - DotEnv: A key parameter from the .env file of a spaceheat SCADA, or a spaceheat
        AtomicTNode.
    """

    Other = auto()
    HardwareLayout = auto()
    DotEnv = auto()

    @classmethod
    def default(cls) -> "KindOfParam":
        """
        Returns default value (in this case Other)
        """
        return cls.Other

    @classmethod
    def version(cls, value: Optional[str] = None) -> str:
        if value is None:
            return "000"
        if not isinstance(value, str):
            raise TypeError("This method applies to strings, not enums")
        if value not in value_to_version:
            raise ValueError(f"Unknown enum value: {value}")
        return value_to_version[value]

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (spaceheat.kind.of.param)
        """
        return "spaceheat.kind.of.param"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"


value_to_version = {
    "Other": "000",
    "HardwareLayout": "000",
    "DotEnv": "000",
}
