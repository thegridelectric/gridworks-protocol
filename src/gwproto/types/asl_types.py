"""List of all the types used by the actor."""

from typing import Dict, List, no_type_check

from gwproto.gs import DispatchMaker, PowerMaker
from gwproto.types.ads111x_based_cac_gt import Ads111xBasedCacGtMaker
from gwproto.types.ads111x_based_component_gt import Ads111xBasedComponentGtMaker
from gwproto.types.batched_readings import BatchedReadingsMaker
from gwproto.types.channel_config import ChannelConfigMaker
from gwproto.types.channel_readings import ChannelReadingsMaker
from gwproto.types.component_attribute_class_gt import ComponentAttributeClassGtMaker
from gwproto.types.component_gt import ComponentGtMaker
from gwproto.types.data_channel_gt import DataChannelGtMaker
from gwproto.types.egauge_io import EgaugeIoMaker
from gwproto.types.egauge_register_config import EgaugeRegisterConfigMaker
from gwproto.types.electric_meter_cac_gt import ElectricMeterCacGtMaker
from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGtMaker
from gwproto.types.fibaro_smart_implant_component_gt import (
    FibaroSmartImplantComponentGtMaker,
)
from gwproto.types.fsm_atomic_report import FsmAtomicReportMaker
from gwproto.types.fsm_event import FsmEventMaker
from gwproto.types.fsm_full_report import FsmFullReportMaker
from gwproto.types.fsm_trigger_from_atn import FsmTriggerFromAtnMaker
from gwproto.types.gt_sh_cli_atn_cmd import GtShCliAtnCmdMaker
from gwproto.types.heartbeat_b import HeartbeatBMaker
from gwproto.types.hubitat_component_gt import HubitatComponentGtMaker
from gwproto.types.hubitat_poller_component_gt import HubitatPollerComponentGtMaker
from gwproto.types.hubitat_tank_component_gt import HubitatTankComponentGtMaker
from gwproto.types.i2c_flow_totalizer_component_gt import (
    I2cFlowTotalizerComponentGtMaker,
)
from gwproto.types.i2c_multichannel_dt_relay_component_gt import (
    I2cMultichannelDtRelayComponentGtMaker,
)
from gwproto.types.keyparam_change_log import KeyparamChangeLogMaker
from gwproto.types.power_watts import PowerWattsMaker
from gwproto.types.relay_actor_config import RelayActorConfigMaker
from gwproto.types.resistive_heater_cac_gt import ResistiveHeaterCacGtMaker
from gwproto.types.resistive_heater_component_gt import ResistiveHeaterComponentGtMaker
from gwproto.types.rest_poller_component_gt import RestPollerComponentGtMaker
from gwproto.types.single_reading import SingleReadingMaker
from gwproto.types.snapshot_spaceheat import SnapshotSpaceheatMaker
from gwproto.types.spaceheat_node_gt import SpaceheatNodeGtMaker
from gwproto.types.synced_readings import SyncedReadingsMaker
from gwproto.types.thermistor_data_processing_config import (
    ThermistorDataProcessingConfigMaker,
)
from gwproto.types.web_server_component_gt import WebServerComponentGtMaker

TypeMakerByName: Dict[str, PowerMaker] = {}


@no_type_check
def type_makers() -> List[PowerMaker]:
    return [
        DispatchMaker,  # special non-json serialization
        PowerMaker,  # special non-json serialization
        Ads111xBasedCacGtMaker,
        Ads111xBasedComponentGtMaker,
        BatchedReadingsMaker,
        ChannelConfigMaker,
        ChannelReadingsMaker,
        ComponentAttributeClassGtMaker,
        ComponentGtMaker,
        DataChannelGtMaker,
        EgaugeIoMaker,
        EgaugeRegisterConfigMaker,
        ElectricMeterCacGtMaker,
        ElectricMeterComponentGtMaker,
        FibaroSmartImplantComponentGtMaker,
        FsmAtomicReportMaker,
        FsmEventMaker,
        FsmFullReportMaker,
        FsmTriggerFromAtnMaker,
        GtShCliAtnCmdMaker,
        HeartbeatBMaker,
        HubitatComponentGtMaker,
        HubitatPollerComponentGtMaker,
        HubitatTankComponentGtMaker,
        I2cFlowTotalizerComponentGtMaker,
        I2cMultichannelDtRelayComponentGtMaker,
        KeyparamChangeLogMaker,
        PowerWattsMaker,
        RelayActorConfigMaker,
        ResistiveHeaterCacGtMaker,
        ResistiveHeaterComponentGtMaker,
        RestPollerComponentGtMaker,
        SingleReadingMaker,
        SnapshotSpaceheatMaker,
        SpaceheatNodeGtMaker,
        SyncedReadingsMaker,
        ThermistorDataProcessingConfigMaker,
        WebServerComponentGtMaker,
    ]


for maker in type_makers():
    TypeMakerByName[maker.type_name] = maker


def version_by_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are TypeNames, values are versions
    """

    v: Dict[str, str] = {
        "ads111x.based.cac.gt": "000",
        "ads111x.based.component.gt": "000",
        "batched.readings": "000",
        "channel.config": "000",
        "channel.readings": "000",
        "component.attribute.class.gt": "001",
        "component.gt": "001",
        "data.channel.gt": "001",
        "egauge.io": "001",
        "egauge.register.config": "000",
        "electric.meter.cac.gt": "001",
        "electric.meter.component.gt": "001",
        "fibaro.smart.implant.component.gt": "000",
        "fsm.atomic.report": "000",
        "fsm.event": "000",
        "fsm.full.report": "000",
        "fsm.trigger.from.atn": "000",
        "gt.sh.cli.atn.cmd": "110",
        "heartbeat.b": "001",
        "hubitat.component.gt": "000",
        "hubitat.poller.component.gt": "000",
        "hubitat.tank.component.gt": "000",
        "i2c.flow.totalizer.component.gt": "000",
        "i2c.multichannel.dt.relay.component.gt": "000",
        "keyparam.change.log": "000",
        "power.watts": "000",
        "relay.actor.config": "000",
        "resistive.heater.cac.gt": "000",
        "resistive.heater.component.gt": "000",
        "rest.poller.component.gt": "000",
        "single.reading": "000",
        "snapshot.spaceheat": "001",
        "spaceheat.node.gt": "200",
        "synced.readings": "000",
        "thermistor.data.processing.config": "000",
        "web.server.component.gt": "000",
    }

    return v


def status_by_versioned_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are versioned TypeNames, values are type status
    """

    v: Dict[str, str] = {
        "ads111x.based.cac.gt.000": "Active",
        "ads111x.based.component.gt.000": "Active",
        "batched.readings.000": "Active",
        "channel.config.000": "Active",
        "channel.readings.000": "Active",
        "component.attribute.class.gt.001": "Active",
        "component.gt.001": "Active",
        "data.channel.gt.001": "Active",
        "egauge.io.001": "Active",
        "egauge.register.config.000": "Active",
        "electric.meter.cac.gt.001": "Active",
        "electric.meter.component.gt.001": "Active",
        "fibaro.smart.implant.component.gt.000": "Active",
        "fsm.atomic.report.000": "Active",
        "fsm.event.000": "Active",
        "fsm.full.report.000": "Active",
        "fsm.trigger.from.atn.000": "Active",
        "gt.sh.cli.atn.cmd.110": "Active",
        "heartbeat.b.001": "Active",
        "hubitat.component.gt.000": "Active",
        "hubitat.poller.component.gt.000": "Active",
        "hubitat.tank.component.gt.000": "Active",
        "i2c.flow.totalizer.component.gt.000": "Active",
        "i2c.multichannel.dt.relay.component.gt.000": "Active",
        "keyparam.change.log.000": "Active",
        "power.watts.000": "Active",
        "relay.actor.config.000": "Active",
        "resistive.heater.cac.gt.000": "Active",
        "resistive.heater.component.gt.000": "Active",
        "rest.poller.component.gt.000": "Active",
        "single.reading.000": "Active",
        "snapshot.spaceheat.001": "Active",
        "spaceheat.node.gt.200": "Active",
        "synced.readings.000": "Active",
        "thermistor.data.processing.config.000": "Active",
        "web.server.component.gt.000": "Active",
    }

    return v
