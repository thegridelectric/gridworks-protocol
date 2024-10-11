from enum import auto
from typing import List

from gw.enums import GwStrEnum


class FsmEventType(GwStrEnum):
    """
    The name of a set of events for a particular Spaceheat finite state machine.
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

    For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shfsmeventtype)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
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
        return cls.ChangeRelayState

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "sh.fsm.event.type"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
