from enum import auto
from typing import List

from gw.enums import GwStrEnum


class PicoCyclerEvent(GwStrEnum):
    """

    Values:
      - PicoMissing
      - ConfirmOpened
      - StartClosing
      - ConfirmClosed
      - ConfirmRebooted
      - AllZombies
      - RebootDud

    For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#picocyclerevent)
    """

    PicoMissing = auto()
    ConfirmOpened = auto()
    StartClosing = auto()
    ConfirmClosed = auto()
    ConfirmRebooted = auto()
    AllZombies = auto()
    RebootDud = auto()

    @classmethod
    def default(cls) -> "PicoCyclerEvent":
        return cls.ConfirmRebooted

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "pico.cycler.event"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
