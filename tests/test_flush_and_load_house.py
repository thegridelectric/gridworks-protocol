"""Test load_house module"""

# from actors.config import ScadaSettings
from gwproto.data_classes.sh_node import ShNode
from gwproto.enums import MakeModel, TelemetryName
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import (
    ElectricMeterCacGt,
    ElectricMeterCacGtMaker,
    SpaceheatNodeGtMaker,
)
from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGtMaker

from tests.utils import flush_all


def test_flush_and_load_house():
    """Verify that flush_house() successfully removes all dictionary data from relevant dataclasses, and
    load_house() successfully loads test objects"""
    flush_all()

    cac_gt = ElectricMeterCacGt(
        ComponentAttributeClassId=CACS_BY_MAKE_MODEL[MakeModel.EGAUGE__4030],
        MakeModel=MakeModel.EGAUGE__4030,
        DisplayName="Egauge 4030",
        MinPollPeriodMs=1000,
        TelemetryNameList=[TelemetryName.PowerW, TelemetryName.CurrentRmsMicroAmps],
    )
    ElectricMeterCacGtMaker.tuple_to_dc(cac_gt)

    electric_meter_component_dict = {
        "ComponentId": "04ceb282-d7e8-4293-80b5-72455e1a5db3",
        "ComponentAttributeClassId": "739a6e32-bb9c-43bc-a28d-fb61be665522",
        "DisplayName": "HP IDU Pwr",
        "ConfigList": [
            {
                "ChannelName": "hp-idu-pwr",
                "PollPeriodMs": 1000,
                "CapturePeriodS": 60,
                "AsyncCapture": True,
                "AsyncCaptureDelta": 20,
                "Exponent": 1,
                "TypeName": "channel.config",
                "Version": "000",
                "UnitGtEnumSymbol": "f459a9c3",
            }
        ],
        "HwUid": "35941_308",
        "ModbusHost": "eGauge4922.local",
        "ModbusPort": 502,
        "EgaugeIoList": [
            {
                "ChannelName": "hp-idu-pwr",
                "InputConfig": {
                    "Address": 9000,
                    "Name": "",
                    "Description": "change in value",
                    "Type": "f32",
                    "Denominator": 1,
                    "Unit": "W",
                    "TypeName": "egauge.register.config",
                    "Version": "000",
                },
                "TypeName": "egauge.io",
                "Version": "001",
            }
        ],
        "TypeName": "electric.meter.component.gt",
        "Version": "001",
    }

    meter_node_dict = {
        "ShNodeId": "92091523-4fa7-4a3e-820b-fddee089222f",
        "Name": "primary-pwr-meter",
        "ActorHierarchyName": "s.primary-pwr-meter",
        "ActorClassGtEnumSymbol": "2ea112b9",
        "DisplayName": "EGauge4922 Power Meter",
        "ComponentId": "04ceb282-d7e8-4293-80b5-72455e1a5db3",
        "TypeName": "spaceheat.node.gt",
        "Version": "200",
    }

    ElectricMeterComponentGtMaker.dict_to_dc(electric_meter_component_dict)
    SpaceheatNodeGtMaker.dict_to_dc(meter_node_dict)
    assert (
        ShNode.by_id["92091523-4fa7-4a3e-820b-fddee089222f"].name == "primary-pwr-meter"
    )
    flush_all()

    # layout = HardwareLayout.load(ScadaSettings().paths.hardware_layout)
    # assert layout.node("a.m").sh_node_id == "0dd8a803-4724-4f49-b845-14ff57bdb3e6"
    # for node in layout.nodes.values():
    #     layout.parent_node(node.alias)
    # all_nodes = list(layout.nodes.values())
    # assert len(all_nodes) == 26
    # aliases = list(layout.nodes.keys())
    # for i in range(len(aliases)):
    #     alias = aliases[i]
    #     assert layout.node(alias) is not None
    # nodes_w_components = list(
    #     filter(lambda x: x.component_id is not None, layout.nodes.values())
    # )
    # assert len(nodes_w_components) == 20
    # actor_nodes_w_components = list(filter(lambda x: x.has_actor, nodes_w_components))
    # assert len(actor_nodes_w_components) == 13
    # tank_water_temp_sensor_nodes = list(
    #     filter(lambda x: x.role == Role.TankWaterTempSensor, all_nodes)
    # )
    # assert len(tank_water_temp_sensor_nodes) == 5
    # for node in tank_water_temp_sensor_nodes:
    #     assert node.reporting_sample_period_s is not None
    #
    # flush_all()
    # assert I2cMultichannelDtRelayComponent.by_id == {}
    # assert ElectricMeterComponent.by_id == {}
    # assert I2cFlowTotalizerComponent.by_id == {}
    # assert ResistiveHeaterComponent.by_id == {}
    # assert Component.by_id == {}
    #
    # assert RelayCac.by_id == {}
    # assert ElectricMeterCac.by_id == {}
    # assert PipeFlowSensorCac.by_id == {}
    # assert ResistiveHeaterCac.by_id == {}
    # assert ComponentAttributeClass.by_id == {}
    # assert ShNode.by_id == {}


# def test_load_real_house():
#     layout = HardwareLayout(
#         {}
#     )
#     for node in layout.nodes.values():
#         layout.parent_node(node.alias)
