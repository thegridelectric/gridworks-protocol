from enum import auto

from gw.enums import GwStrEnum


class ChangeStoreFlowRelay(GwStrEnum):
    """
    Events that trigger changing StoreFlowDirection finite state machine
    Values:
      - DischargeStore
      - ChargeStore

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/change.store.flow.relay.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    DischargeStore = auto()
    ChargeStore = auto()

    @classmethod
    def default(cls) -> "ChangeStoreFlowRelay":
        return cls.DischargeStore

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "change.store.flow.relay"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
