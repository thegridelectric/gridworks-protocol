from enum import auto
from typing import Optional

from gw.enums import GwStrEnum


class FsmEventType(GwStrEnum):
    """
    The name of a set of events for a particular Spaceheat finite state machine.

    Enum sh.fsm.event.type version 000 in the GridWorks Type registry.

    Used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shfsmeventtype)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)

    Values:
      - ChangeRelayPin: Meant to be used between a single relay actor and a multiplexer
        (for example, an i2c relay actor and an i2c relay multiplexer). The associated values
        are DeEnergized and Energized. Note that the multiplexer does not concern itself with
        the configuration of the relay (NormallyOpen, NormallyClosed, DoubleThrow). Instead,
        it just makes sure it is receiving a ChangeRelayPin command from one of its known relays.
      - ChangeRelayState: Meant to be used for a relay whose RelayConfig is NormallyOpen
        or NormallyClosed (not DoubleThrow). Associated values are CloseRelay and OpenRelay
        - so it is meant to be a layer up in abstraction from sending energization/de-energization
        commands to the pin. The sender indeed does not need to know whether the relay is normally
        open or normally closed (although obviously the receiver must know).
      - SetAnalog010V
      - SetAnalog420mA
      - ChangeValveState
      - ChangeStoreFlowDirection
      - ChangeHeatcallSource
      - ChangeAquastatControl
      - ChangeHeatPumpControl
      - ChangeLgOperatingMode
      - TimerFinished
      - ChangePrimaryPumpState
      - ChangePrimaryPumpControl: Change control of the primary pump between the Heat
        pump and the SCADA
    """

    ChangeRelayPin = auto()
    ChangeRelayState = auto()
    SetAnalog010V = auto()
    SetAnalog420mA = auto()
    ChangeValveState = auto()
    ChangeStoreFlowDirection = auto()
    ChangeHeatcallSource = auto()
    ChangeAquastatControl = auto()
    ChangeHeatPumpControl = auto()
    ChangeLgOperatingMode = auto()
    TimerFinished = auto()
    ChangePrimaryPumpState = auto()
    ChangePrimaryPumpControl = auto()

    @classmethod
    def default(cls) -> "FsmEventType":
        """
        Returns default value (in this case ChangeRelayState)
        """
        return cls.ChangeRelayState

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
        The name in the GridWorks Type Registry (sh.fsm.event.type)
        """
        return "sh.fsm.event.type"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"


value_to_version = {
    "ChangeRelayPin": "000",
    "ChangeRelayState": "000",
    "SetAnalog010V": "000",
    "SetAnalog420mA": "000",
    "ChangeValveState": "000",
    "ChangeStoreFlowDirection": "000",
    "ChangeHeatcallSource": "000",
    "ChangeAquastatControl": "000",
    "ChangeHeatPumpControl": "000",
    "ChangeLgOperatingMode": "000",
    "TimerFinished": "000",
    "ChangePrimaryPumpState": "000",
    "ChangePrimaryPumpControl": "000",
}
