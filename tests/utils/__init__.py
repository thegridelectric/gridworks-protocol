from gwproto.data_classes.component import Component
from gwproto.data_classes.component_attribute_class import ComponentAttributeClass
from gwproto.data_classes.components.ads111x_based_component import Ads111xBasedCac
from gwproto.data_classes.components.ads111x_based_component import (
    Ads111xBasedComponent,
)
from gwproto.data_classes.components.electric_meter_component import ElectricMeterCac
from gwproto.data_classes.components.electric_meter_component import (
    ElectricMeterComponent,
)
from gwproto.data_classes.components.i2c_flow_totalizer_component import (
    I2cFlowTotalizerComponent,
)
from gwproto.data_classes.components.i2c_multichannel_dt_relay_component import (
    I2cMultichannelDtRelayComponent,
)
from gwproto.data_classes.components.resistive_heater_component import (
    ResistiveHeaterCac,
)
from gwproto.data_classes.components.resistive_heater_component import (
    ResistiveHeaterComponent,
)
from gwproto.data_classes.sh_node import ShNode


def flush_components():
    Ads111xBasedComponent.by_id = {}
    ElectricMeterComponent.by_id = {}
    I2cFlowTotalizerComponent.by_id = {}
    I2cMultichannelDtRelayComponent.by_id = {}
    ResistiveHeaterComponent.by_id = {}
    Component.by_id = {}


def flush_cacs():
    ElectricMeterCac.by_id = {}
    Ads111xBasedCac.by_id = {}
    ResistiveHeaterCac.by_id = {}
    ComponentAttributeClass.by_id = {}


def flush_spaceheat_nodes():
    ShNode.by_id = {}


def flush_all():
    flush_components()
    flush_cacs()
    flush_spaceheat_nodes()
