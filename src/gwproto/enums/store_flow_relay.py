from enum import auto

from gw.enums import GwStrEnum


class StoreFlowRelay(GwStrEnum):
    """
    Used for a double-throw relay that can toggle between a thermal store heating up (flow is
    in the charging direction) or cooling down (flow is in the discharging direction). Events
    in the StoreFlowDirection finite state machine
    Values:
      - DischargingStore: Thermal store is discharging (and heating the building)
      - ChargingStore: Thermal store is charging from an external source (like a heat
        pump or oil boiler).

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/store.flow.relay.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    DischargingStore = auto()
    ChargingStore = auto()

    @classmethod
    def default(cls) -> "StoreFlowRelay":
        return cls.DischargingStore

    @classmethod
    def values(cls) -> list[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "store.flow.relay"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
