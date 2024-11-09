from enum import auto
from typing import List

from gw.enums import GwStrEnum


class PicoCyclerState(GwStrEnum):
    """

    Values:
      - PicosLive
      - RelayOpening
      - RelayOpen
      - RelayClosing
      - PicosRebooting

    For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#picocyclerstate)
    """

    PicosLive = auto()
    RelayOpening = auto()
    RelayOpen = auto()
    RelayClosing = auto()
    PicosRebooting = auto()

    @classmethod
    def default(cls) -> "PicoCyclerState":
        return cls.PicosLive

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "pico.cycler.state"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
