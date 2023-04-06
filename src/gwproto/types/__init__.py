""" List of all the schema types """

from gwproto.types.component_attribute_class_gt import ComponentAttributeClassGt
from gwproto.types.component_attribute_class_gt import ComponentAttributeClassGt_Maker
from gwproto.types.component_gt import ComponentGt
from gwproto.types.component_gt import ComponentGt_Maker
from gwproto.types.data_channel import DataChannel
from gwproto.types.data_channel import DataChannel_Maker
from gwproto.types.egauge_io import EgaugeIo
from gwproto.types.egauge_io import EgaugeIo_Maker
from gwproto.types.egauge_register_config import EgaugeRegisterConfig
from gwproto.types.egauge_register_config import EgaugeRegisterConfig_Maker
from gwproto.types.electric_meter_cac_gt import ElectricMeterCacGt
from gwproto.types.electric_meter_cac_gt import ElectricMeterCacGt_Maker
from gwproto.types.gt_boolean_actuator_cac import GtBooleanActuatorCac
from gwproto.types.gt_boolean_actuator_cac import GtBooleanActuatorCac_Maker
from gwproto.types.gt_boolean_actuator_component import GtBooleanActuatorComponent
from gwproto.types.gt_boolean_actuator_component import GtBooleanActuatorComponent_Maker
from gwproto.types.gt_dispatch_boolean import GtDispatchBoolean
from gwproto.types.gt_dispatch_boolean import GtDispatchBoolean_Maker
from gwproto.types.gt_dispatch_boolean_local import GtDispatchBooleanLocal
from gwproto.types.gt_dispatch_boolean_local import GtDispatchBooleanLocal_Maker
from gwproto.types.gt_driver_booleanactuator_cmd import GtDriverBooleanactuatorCmd
from gwproto.types.gt_driver_booleanactuator_cmd import GtDriverBooleanactuatorCmd_Maker
from gwproto.types.gt_sh_booleanactuator_cmd_status import GtShBooleanactuatorCmdStatus
from gwproto.types.gt_sh_booleanactuator_cmd_status import (
    GtShBooleanactuatorCmdStatus_Maker,
)
from gwproto.types.gt_sh_cli_atn_cmd import GtShCliAtnCmd
from gwproto.types.gt_sh_cli_atn_cmd import GtShCliAtnCmd_Maker
from gwproto.types.gt_sh_multipurpose_telemetry_status import (
    GtShMultipurposeTelemetryStatus,
)
from gwproto.types.gt_sh_multipurpose_telemetry_status import (
    GtShMultipurposeTelemetryStatus_Maker,
)
from gwproto.types.gt_sh_simple_telemetry_status import GtShSimpleTelemetryStatus
from gwproto.types.gt_sh_simple_telemetry_status import GtShSimpleTelemetryStatus_Maker
from gwproto.types.gt_sh_status import GtShStatus
from gwproto.types.gt_sh_status import GtShStatus_Maker
from gwproto.types.gt_sh_telemetry_from_multipurpose_sensor import (
    GtShTelemetryFromMultipurposeSensor,
)
from gwproto.types.gt_sh_telemetry_from_multipurpose_sensor import (
    GtShTelemetryFromMultipurposeSensor_Maker,
)
from gwproto.types.gt_telemetry import GtTelemetry
from gwproto.types.gt_telemetry import GtTelemetry_Maker
from gwproto.types.heartbeat_b import HeartbeatB
from gwproto.types.heartbeat_b import HeartbeatB_Maker
from gwproto.types.multipurpose_sensor_cac_gt import MultipurposeSensorCacGt
from gwproto.types.multipurpose_sensor_cac_gt import MultipurposeSensorCacGt_Maker
from gwproto.types.pipe_flow_sensor_cac_gt import PipeFlowSensorCacGt
from gwproto.types.pipe_flow_sensor_cac_gt import PipeFlowSensorCacGt_Maker
from gwproto.types.pipe_flow_sensor_component_gt import PipeFlowSensorComponentGt
from gwproto.types.pipe_flow_sensor_component_gt import PipeFlowSensorComponentGt_Maker
from gwproto.types.power_watts import PowerWatts
from gwproto.types.power_watts import PowerWatts_Maker
from gwproto.types.resistive_heater_cac_gt import ResistiveHeaterCacGt
from gwproto.types.resistive_heater_cac_gt import ResistiveHeaterCacGt_Maker
from gwproto.types.resistive_heater_component_gt import ResistiveHeaterComponentGt
from gwproto.types.resistive_heater_component_gt import ResistiveHeaterComponentGt_Maker
from gwproto.types.simple_temp_sensor_cac_gt import SimpleTempSensorCacGt
from gwproto.types.simple_temp_sensor_cac_gt import SimpleTempSensorCacGt_Maker
from gwproto.types.simple_temp_sensor_component_gt import SimpleTempSensorComponentGt
from gwproto.types.simple_temp_sensor_component_gt import (
    SimpleTempSensorComponentGt_Maker,
)
from gwproto.types.snapshot_spaceheat import SnapshotSpaceheat
from gwproto.types.snapshot_spaceheat import SnapshotSpaceheat_Maker
from gwproto.types.spaceheat_node_gt import SpaceheatNodeGt
from gwproto.types.spaceheat_node_gt import SpaceheatNodeGt_Maker
from gwproto.types.telemetry_reporting_config import TelemetryReportingConfig
from gwproto.types.telemetry_reporting_config import TelemetryReportingConfig_Maker
from gwproto.types.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat
from gwproto.types.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat_Maker


__all__ = [
    "ComponentAttributeClassGt",
    "ComponentAttributeClassGt_Maker",
    "ComponentGt",
    "ComponentGt_Maker",
    "DataChannel",
    "DataChannel_Maker",
    "EgaugeIo",
    "EgaugeIo_Maker",
    "EgaugeRegisterConfig",
    "EgaugeRegisterConfig_Maker",
    "ElectricMeterCacGt",
    "ElectricMeterCacGt_Maker",
    # "ElectricMeterComponentGt",
    # "ElectricMeterComponentGt_Maker",
    "GtBooleanActuatorCac",
    "GtBooleanActuatorCac_Maker",
    "GtBooleanActuatorComponent",
    "GtBooleanActuatorComponent_Maker",
    "GtDispatchBoolean",
    "GtDispatchBoolean_Maker",
    "GtDispatchBooleanLocal",
    "GtDispatchBooleanLocal_Maker",
    "GtDriverBooleanactuatorCmd",
    "GtDriverBooleanactuatorCmd_Maker",
    "GtShBooleanactuatorCmdStatus",
    "GtShBooleanactuatorCmdStatus_Maker",
    "GtShCliAtnCmd",
    "GtShCliAtnCmd_Maker",
    "GtShMultipurposeTelemetryStatus",
    "GtShMultipurposeTelemetryStatus_Maker",
    "GtShSimpleTelemetryStatus",
    "GtShSimpleTelemetryStatus_Maker",
    "GtShStatus",
    "GtShStatus_Maker",
    "GtShTelemetryFromMultipurposeSensor",
    "GtShTelemetryFromMultipurposeSensor_Maker",
    "GtTelemetry",
    "GtTelemetry_Maker",
    "HeartbeatB",
    "HeartbeatB_Maker",
    "MultipurposeSensorCacGt",
    "MultipurposeSensorCacGt_Maker",
    # "MultipurposeSensorComponentGt",
    # "MultipurposeSensorComponentGt_Maker",
    "PipeFlowSensorCacGt",
    "PipeFlowSensorCacGt_Maker",
    "PipeFlowSensorComponentGt",
    "PipeFlowSensorComponentGt_Maker",
    "PowerWatts",
    "PowerWatts_Maker",
    "ResistiveHeaterCacGt",
    "ResistiveHeaterCacGt_Maker",
    "ResistiveHeaterComponentGt",
    "ResistiveHeaterComponentGt_Maker",
    "SimpleTempSensorCacGt",
    "SimpleTempSensorCacGt_Maker",
    "SimpleTempSensorComponentGt",
    "SimpleTempSensorComponentGt_Maker",
    "SnapshotSpaceheat",
    "SnapshotSpaceheat_Maker",
    "SpaceheatNodeGt",
    "SpaceheatNodeGt_Maker",
    "TelemetryReportingConfig",
    "TelemetryReportingConfig_Maker",
    "TelemetrySnapshotSpaceheat",
    "TelemetrySnapshotSpaceheat_Maker",
]
