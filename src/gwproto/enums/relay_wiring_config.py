from enum import auto
from typing import Optional

from gw.enums import GwStrEnum


class RelayWiringConfig(GwStrEnum):
    """
    While some relays come with only two terminals and a default configuration, many come with
    a common terminal (COM), normally open terminal (NO) and normally closed terminal (NC).
    When the relay is de-energized, the circuit between COM and Normally Closed is closed. When
    the relay is energized, the circuit between COM and Normally Open is closed. This enum is
    about how one wires such a relay into a circuit.

    Enum relay.wiring.config version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#relaywiringconfig)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/relays.html)

    Values:
      - NormallyClosed: When the relay is de-energized, the circuit is closed (circuit
        is wired through COM and NC).
      - NormallyOpen: When the relay is de-energized, the circuit is open (circuit is
        wired through COM and NC).
      - DoubleThrow: COM, NC, and NO are all connected to parts of the circuit. For example,
        NC could activate a heat pump and NO could activate a backup oil boiler. The Double
        Throw configuration allows for switching between these two.
    """

    NormallyClosed = auto()
    NormallyOpen = auto()
    DoubleThrow = auto()

    @classmethod
    def default(cls) -> "RelayWiringConfig":
        """
        Returns default value (in this case NormallyClosed)
        """
        return cls.NormallyClosed

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
        The name in the GridWorks Type Registry (relay.wiring.config)
        """
        return "relay.wiring.config"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"


value_to_version = {
    "NormallyClosed": "000",
    "NormallyOpen": "000",
    "DoubleThrow": "000",
}
