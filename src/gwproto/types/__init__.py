"""List of all the types"""

from gwproto.types.ads111x_based_cac_gt import Ads111xBasedCacGt, Ads111xBasedCacGtMaker
from gwproto.types.batched_readings import BatchedReadings, BatchedReadingsMaker
from gwproto.types.channel_config import ChannelConfig, ChannelConfigMaker
from gwproto.types.channel_readings import ChannelReadings, ChannelReadingsMaker
from gwproto.types.component_attribute_class_gt import (
    ComponentAttributeClassGt,
    ComponentAttributeClassGtMaker,
)
from gwproto.types.component_gt import ComponentGt, ComponentGtMaker
from gwproto.types.data_channel_gt import DataChannelGt, DataChannelGtMaker
from gwproto.types.egauge_io import EgaugeIo, EgaugeIoMaker
from gwproto.types.egauge_register_config import (
    EgaugeRegisterConfig,
    EgaugeRegisterConfigMaker,
)
from gwproto.types.electric_meter_cac_gt import (
    ElectricMeterCacGt,
    ElectricMeterCacGtMaker,
)
from gwproto.types.fsm_atomic_report import FsmAtomicReport, FsmAtomicReportMaker
from gwproto.types.fsm_event import FsmEvent, FsmEventMaker
from gwproto.types.fsm_full_report import FsmFullReport, FsmFullReportMaker
from gwproto.types.fsm_trigger_from_atn import FsmTriggerFromAtn, FsmTriggerFromAtnMaker
from gwproto.types.gt_sh_cli_atn_cmd import GtShCliAtnCmd, GtShCliAtnCmdMaker
from gwproto.types.heartbeat_b import HeartbeatB, HeartbeatBMaker
from gwproto.types.keyparam_change_log import KeyparamChangeLog, KeyparamChangeLogMaker
from gwproto.types.power_watts import PowerWatts, PowerWattsMaker
from gwproto.types.relay_actor_config import RelayActorConfig, RelayActorConfigMaker
from gwproto.types.resistive_heater_cac_gt import (
    ResistiveHeaterCacGt,
    ResistiveHeaterCacGtMaker,
)
from gwproto.types.single_reading import SingleReading, SingleReadingMaker
from gwproto.types.snapshot_spaceheat import SnapshotSpaceheat, SnapshotSpaceheatMaker
from gwproto.types.spaceheat_node_gt import SpaceheatNodeGt, SpaceheatNodeGtMaker
from gwproto.types.synced_readings import SyncedReadings, SyncedReadingsMaker
from gwproto.types.thermistor_data_processing_config import (
    ThermistorDataProcessingConfig,
    ThermistorDataProcessingConfigMaker,
)
from gwproto.types.web_server_component_gt import (
    WebServerComponentGt,
    WebServerComponentGtMaker,
)
from gwproto.types.web_server_gt import WebServerGt

__all__ = [
    "Ads111xBasedCacGt",
    "Ads111xBasedCacGtMaker",
    # "Ads111xBasedComponentGt",
    # "Ads111xBasedComponentGtMaker",
    "BatchedReadings",
    "BatchedReadingsMaker",
    "ChannelConfig",
    "ChannelConfigMaker",
    "ChannelReadings",
    "ChannelReadingsMaker",
    "ComponentAttributeClassGt",
    "ComponentAttributeClassGtMaker",
    "ComponentGt",
    "ComponentGtMaker",
    "DataChannelGt",
    "DataChannelGtMaker",
    "EgaugeIo",
    "EgaugeIoMaker",
    "EgaugeRegisterConfig",
    "EgaugeRegisterConfigMaker",
    "ElectricMeterCacGt",
    "ElectricMeterCacGtMaker",
    # "ElectricMeterComponentGt",
    # "ElectricMeterComponentGtMaker",
    # "FibaroSmartImplantComponentGt",
    # "FibaroSmartImplantComponentGtMaker",
    "FsmAtomicReport",
    "FsmAtomicReportMaker",
    "FsmEvent",
    "FsmEventMaker",
    "FsmFullReport",
    "FsmFullReportMaker",
    "FsmTriggerFromAtn",
    "FsmTriggerFromAtnMaker",
    "GtShCliAtnCmd",
    "GtShCliAtnCmdMaker",
    "HeartbeatB",
    "HeartbeatBMaker",
    # "HubitatComponentGt",
    # "HubitatComponentGtMaker",
    # "HubitatPollerComponentGt",
    # "HubitatPollerComponentGtMaker",
    # "HubitatTankComponentGt",
    # "HubitatTankComponentGtMaker",
    # "I2cFlowTotalizerComponentGt",
    # "I2cFlowTotalizerComponentGtMaker",
    # "I2cMultichannelDtRelayComponentGt",
    # "I2cMultichannelDtRelayComponentGtMaker",
    "KeyparamChangeLog",
    "KeyparamChangeLogMaker",
    "PowerWatts",
    "PowerWattsMaker",
    "RelayActorConfig",
    "RelayActorConfigMaker",
    "ResistiveHeaterCacGt",
    "ResistiveHeaterCacGtMaker",
    # "ResistiveHeaterComponentGt",
    # "ResistiveHeaterComponentGtMaker",
    # "RESTPollerComponentGt",
    # "RESTPollerComponentGtMaker",
    "SingleReading",
    "SingleReadingMaker",
    "SnapshotSpaceheat",
    "SnapshotSpaceheatMaker",
    "SpaceheatNodeGt",
    "SpaceheatNodeGtMaker",
    "SyncedReadings",
    "SyncedReadingsMaker",
    "ThermistorDataProcessingConfig",
    "ThermistorDataProcessingConfigMaker",
    "WebServerComponentGt",
    "WebServerComponentGtMaker",
    "WebServerGt",
]
