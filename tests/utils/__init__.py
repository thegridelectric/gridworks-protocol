from gwproto.data_classes.component import Component
from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.data_classes.components.electric_meter_component import (
    ElectricMeterCac,
    ElectricMeterComponent,
)
from gwproto.data_classes.components.multipurpose_sensor_component import (
    MultipurposeSensorCac,
    MultipurposeSensorComponent,
)
from gwproto.data_classes.components.pipe_flow_sensor_component import (
    PipeFlowSensorCac,
    PipeFlowSensorComponent,
)
from gwproto.data_classes.components.relay_component import RelayCac, RelayComponent
from gwproto.data_classes.components.resistive_heater_component import (
    ResistiveHeaterCac,
    ResistiveHeaterComponent,
)
from gwproto.data_classes.components.simple_temp_sensor_component import (
    SimpleTempSensorCac,
    SimpleTempSensorComponent,
)
from gwproto.data_classes.sh_node import ShNode


def flush_components():
    RelayComponent.by_id = {}
    ElectricMeterComponent.by_id = {}
    PipeFlowSensorComponent.by_id = {}
    MultipurposeSensorComponent.by_id = {}
    ResistiveHeaterComponent.by_id = {}
    SimpleTempSensorComponent.by_id = {}
    Component.by_id = {}


def flush_cacs():
    RelayCac.by_id = {}
    ElectricMeterCac.by_id = {}
    MultipurposeSensorCac.by_id = {}
    PipeFlowSensorCac.by_id = {}
    ResistiveHeaterCac.by_id = {}
    SimpleTempSensorCac.by_id = {}
    ComponentAttributeClass.by_id = {}


def flush_spaceheat_nodes():
    ShNode.by_id = {}


def flush_all():
    flush_components()
    flush_cacs()
    flush_spaceheat_nodes()
