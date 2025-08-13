"""
Enums from the GridWorks Application Shared Languages (ASL)

The GridWorks ASL enables peer-to-peer shared vocabulary between energy system actors like
SCADA devices, trading nodes, and market makers. Enums serve as the "controlled vocabulary"
foundation that ensures everyone speaks the same language.

Key characteristics:
 - Immutable evolution: Enum values can be added but never changed or removed, ensuring
   backwards compatibility across distributed systems
 - Transport-agnostic: Same enums work with RabbitMQ, HTTP APIs, Kafka, or any message delivery
 - Organizational autonomy: Each organization can build exactly the sophistication they need
   on top of shared foundations
 - Constitutional governance: Follow naming conventions (left.right.dot format) and
   ownership rules defined in the ASL registry

Enums are the semantic building blocks that enable organizations to collaborate without
compromising their independence. Unlike APIs where one party controls the vocabulary,
ASL enums evolve through community governance while maintaining stability.

Application Shared Languages represent an evolution beyond traditional APIs - enabling
true peer-to-peer collaboration where organizations maintain autonomy while sharing
vocabulary, rather than client/server relationships where one party dictates the interface.

For more information:
 - [Why GridWorks ASL Exists](https://gridworks-asl.readthedocs.io/motivation/)
 - [ASL Rules and Guidelines](https://gridworks-asl.readthedocs.io/rules-and-guidelines/)
 - [GridWorks ASL Overview](https://gridworks-asl.readthedocs.io/)
"""

from gwproto.enums.actor_class import ActorClass
from gwproto.enums.admin_event import AdminEvent
from gwproto.enums.admin_state import AdminState
from gwproto.enums.alert_priority import AlertPriority
from gwproto.enums.aquastat_control import AquastatControl
from gwproto.enums.change_aquastat_control import ChangeAquastatControl
from gwproto.enums.change_heat_pump_control import ChangeHeatPumpControl
from gwproto.enums.change_heatcall_source import ChangeHeatcallSource
from gwproto.enums.change_primary_pump_control import ChangePrimaryPumpControl
from gwproto.enums.change_relay_pin import ChangeRelayPin
from gwproto.enums.change_relay_state import ChangeRelayState
from gwproto.enums.change_store_flow_relay import ChangeStoreFlowRelay
from gwproto.enums.change_valve_state import ChangeValveState
from gwproto.enums.fsm_action_type import FsmActionType
from gwproto.enums.fsm_name import FsmName
from gwproto.enums.fsm_report_type import FsmReportType
from gwproto.enums.gpm_from_hz_method import GpmFromHzMethod
from gwproto.enums.heat_pump_control import HeatPumpControl
from gwproto.enums.heatcall_source import HeatcallSource
from gwproto.enums.hz_calc_method import HzCalcMethod
from gwproto.enums.kind_of_param import KindOfParam
from gwproto.enums.make_model import MakeModel
from gwproto.enums.primary_pump_control import PrimaryPumpControl
from gwproto.enums.relay_closed_or_open import RelayClosedOrOpen
from gwproto.enums.relay_energization_state import RelayEnergizationState
from gwproto.enums.relay_pin_set import RelayPinSet
from gwproto.enums.relay_wiring_config import RelayWiringConfig
from gwproto.enums.store_flow_relay import StoreFlowRelay
from gwproto.enums.strategy import Strategy
from gwproto.enums.telemetry_name import TelemetryName
from gwproto.enums.temp_calc_method import TempCalcMethod
from gwproto.enums.thermistor_data_method import ThermistorDataMethod
from gwproto.enums.unit import Unit

__all__ = [
    "ActorClass",
    "AdminEvent",
    "AdminState",
    "AlertPriority",
    "AquastatControl",
    "ChangeAquastatControl",
    "ChangeHeatPumpControl",
    "ChangeHeatcallSource",
    "ChangePrimaryPumpControl",
    "ChangeRelayPin",
    "ChangeRelayState",
    "ChangeStoreFlowRelay",
    "ChangeValveState",
    "FsmActionType",
    "FsmName",
    "FsmReportType",
    "GpmFromHzMethod",
    "HeatPumpControl",
    "HeatcallSource",
    "HzCalcMethod",
    "KindOfParam",
    "MakeModel",
    "PrimaryPumpControl",
    "RelayClosedOrOpen",
    "RelayEnergizationState",
    "RelayPinSet",
    "RelayWiringConfig",
    "StoreFlowRelay",
    "Strategy",
    "TelemetryName",
    "TempCalcMethod",
    "ThermistorDataMethod",
    "Unit",
]
