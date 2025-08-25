from enum import auto

from gw.enums import GwStrEnum


class FsmActionType(GwStrEnum):
    """
    A list of the finite state machine Actions that a spaceheat node might take. An Action,
    in this context, is a side-effect of a state machine transition that impacts the real world
    (i.e., a relay is actuated).
    Values:
      - RelayPinSet
      - Analog010VSignalSet
      - Analog420maSignalSet

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/sh.fsm.action.type.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
      - [More Info](https://gridworks-protocol.readthedocs.io/en/latest/finite-state-machines.html)
    """

    RelayPinSet = auto()
    Analog010VSignalSet = auto()
    Analog420maSignalSet = auto()

    @classmethod
    def default(cls) -> "FsmActionType":
        return cls.RelayPinSet

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "sh.fsm.action.type"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
