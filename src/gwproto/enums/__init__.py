"""
GridWorks Enums used in gwproto, the Application Shared Language (ASL) used by SCADA
devices and AtomicTNodes to communicate with each other. These enums play a specific structural
role as semantic "glue" within ASLs.

Key attributes:
  - Enum values are translated into "GridWorks Type Enum Symbols" (GtEnumSymbols) when embedded
  in a serialized type sent as a message from one Application and/or Actor to another.
  - Each Enum has a unique name in the type registry (like spaceheat.telemetry.name), along
  with a version (like 001).
  - That name are interpretted locally in the SDK and do not necessarily carry the larger
  context of the unique type registry name (for example gwproto uses TelemetryName, since
  the `spaceheat` context goes without saying).
  - Each Value/Symbol pair also has a version. Value/Symbol pairs cannot be changed or removed.
  The only adjustments that can be made to an enum are adding more Value/Symbols. This is to
  support forwards- and backwards- compatability in GridWorks Types that use these enums.

If Enums are "glue", then GridWorks Types are the building blocks of SALs. Every SAL is comprised
of a set of shared GridWorks Types.

Application Shared Languages are an evolution of the concept of Application Programming Interfaces.
In a nutshell, an API can be viewed as a rather restricted version of an SAL, where only one application
has anything complex/interesting to say and, in general, the developers/owners of that application
have sole responsibility for managing the versioning and changing of that API. Note also that SALs
do not make any a priori assumption about the relationship (i.e. the default client/server for an API)
or the message delivery mechanism (i.e. via default GET/POST to RESTful URLs). For more information
on these ideas:
  - [GridWorks Enums](https://gridwork-type-registry.readthedocs.io/en/latest/types.html)
  - [GridWorks Types](https://gridwork-type-registry.readthedocs.io/en/latest/types.html)
  - [ASLs](https://gridwork-type-registry.readthedocs.io/en/latest/asls.html)


 """
from gwproto.enums.actor_class import ActorClass
from gwproto.enums.change_aquastat_control import ChangeAquastatControl
from gwproto.enums.change_heat_pump_control import ChangeHeatPumpControl
from gwproto.enums.change_heatcall_source import ChangeHeatcallSource
from gwproto.enums.change_lg_operating_mode import ChangeLgOperatingMode
from gwproto.enums.change_relay_pin import ChangeRelayPin
from gwproto.enums.change_relay_state import ChangeRelayState
from gwproto.enums.change_store_flow_direction import ChangeStoreFlowDirection
from gwproto.enums.change_valve_state import ChangeValveState
from gwproto.enums.fsm_action_type import FsmActionType
from gwproto.enums.fsm_event_type import FsmEventType
from gwproto.enums.fsm_name import FsmName
from gwproto.enums.fsm_report_type import FsmReportType
from gwproto.enums.iso_valve_state import IsoValveState
from gwproto.enums.kind_of_param import KindOfParam
from gwproto.enums.lg_operating_mode import LgOperatingMode
from gwproto.enums.make_model import MakeModel
from gwproto.enums.relay_closed_or_open import RelayClosedOrOpen
from gwproto.enums.relay_energization_state import RelayEnergizationState
from gwproto.enums.relay_pin_set import RelayPinSet
from gwproto.enums.relay_wiring_config import RelayWiringConfig
from gwproto.enums.store_flow_direction import StoreFlowDirection
from gwproto.enums.telemetry_name import TelemetryName
from gwproto.enums.thermistor_data_method import ThermistorDataMethod
from gwproto.enums.unit import Unit


__all__ = [
    "ActorClass",  # [sh.actor.class.001](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shactorclass)
    "ChangeAquastatControl",  # [change.aquastat.control.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#changeboilercontrol)
    "ChangeHeatPumpControl",  # [change.heat.pump.control.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#changeheatpumpcontrol)
    "ChangeHeatcallSource",  # [change.heatcall.source.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#changeheatcallsource)
    "ChangeLgOperatingMode",  # [change.lg.operating.mode.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#changelgoperatingmode)
    "ChangeRelayState",  # [change.relay.state.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#changerelaystate)
    "ChangeRelayPin",
    "ChangeStoreFlowDirection",  # [change.store.flow.direction.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#changestoreflowdirection)
    "ChangeValveState",  # [change.valve.state.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#changevalvestate)
    "FsmActionType",  # [sh.fsm.action.type.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shfsmactiontype)
    "FsmEventType",  # [sh.fsm.event.type.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shfsmeventtype)
    "FsmName",  # [sh.fsm.name.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#shfsmname)
    "FsmReportType",  # [fsm.report.type.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#fsmreporttype)
    "IsoValveState",  # [iso.valve.state.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#isovalvestate)
    "KindOfParam",  # [spaceheat.kind.of.param.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#spaceheatkindofparam)
    "LgOperatingMode",  # [lg.operating.mode.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#lgoperatingmode)
    "MakeModel",  # [spaceheat.make.model.002](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#spaceheatmakemodel)
    "RelayClosedOrOpen",  # [relay.closed.or.open.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#relayclosedoropen)
    "RelayEnergizationState",  # [relay.energization.state.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#relayenergizationstate)
    "RelayPinSet",  # [relay.pin.set.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#relaypinset)
    "RelayWiringConfig",  # [relay.wiring.config.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#relaywiringconfig)
    "StoreFlowDirection",  # [store.flow.direction.state.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#storeflowdirectionstate)
    "TelemetryName",  # [spaceheat.telemetry.name.001](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#spaceheattelemetryname)
    "ThermistorDataMethod",  # [thermistor.data.method.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#thermistordatamethod)
    "Unit",  # [spaceheat.unit.000](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#spaceheatunit)
]
