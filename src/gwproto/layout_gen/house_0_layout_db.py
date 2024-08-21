# Node Ids are going to become the immutable identifiers.
#
import typing
import uuid
from dataclasses import dataclass
from typing import Dict, List, Optional

from pydantic import BaseModel

from gwproto.data_classes.house_0_names import House0RequiredNames
from gwproto.enums import ActorClass, MakeModel, TelemetryName, Unit
from gwproto.layout_gen.layout_db import LayoutDb, LayoutIDMap
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import (
    ChannelConfig,
    ComponentAttributeClassGt,
    ComponentGt,
    DataChannelGt,
    ElectricMeterCacGt,
    SpaceheatNodeGt,
)
from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGt

SCADA_2_NAME = "s2"
SCADA_START_HANDLE = "h.s"
ADMIN_NAME = "admin"
ADMIN_START_HANDLE = "h.admin"
KRIDA_MULTIPLEXER_NAME = "krida-multiplexer"
SCADA_STRATEGY = "House0"


class ChStub(BaseModel):
    ChannelName: str
    AboutName: str
    TelemetryName: TelemetryName
    InPowerMetering: Optional[bool] = None


class House0ChStubs:
    power: List[ChStub]
    core_temp: List[ChStub]
    flow: List[ChStub]
    zone: Dict[str, List[ChStub]]
    misc: List[ChStub]

    def __init__(self, total_store_tanks: int, zone_list: List[str]):
        required_names = House0RequiredNames(total_store_tanks, zone_list)

        self.misc = []
        self.power = [
            ChStub(
                ChannelName=f"{required_names.HP_ODU}-pwr",
                AboutName=required_names.HP_ODU,
                TelemetryName=TelemetryName.PowerW,
                DisplayName="HP ODU Power",
                InPowerMetering=True,
            ),
            ChStub(
                ChannelName=f"{required_names.HP_IDU}-pwr",
                AboutName=required_names.HP_IDU,
                TelemetryName=TelemetryName.PowerW,
                DisplayName="HP IDU Power",
                InPowerMetering=True,
            ),
            ChStub(
                ChannelName=f"{required_names.PRIMARY_PUMP}-pwr",
                AboutName=required_names.PRIMARY_PUMP,
                TelemetryName=TelemetryName.PowerW,
                DisplayName="Primary Pump Power",
            ),
            ChStub(
                ChannelName=f"{required_names.STORE_PUMP}-pwr",
                AboutName=required_names.STORE_PUMP,
                TelemetryName=TelemetryName.PowerW,
                DisplayName="Store Pump Power",
            ),
        ]

        self.core_temp = (
            [
                ChStub(
                    ChannelName=required_names.TEMP.DIST_SWT,
                    AboutName=required_names.TEMP.DIST_SWT,
                    TelemetryName=TelemetryName.WaterTempCTimes1000,
                ),
                ChStub(
                    ChannelName=required_names.TEMP.DIST_RWT,
                    AboutName=required_names.TEMP.DIST_RWT,
                    TelemetryName=TelemetryName.WaterTempCTimes1000,
                ),
                ChStub(
                    ChannelName=required_names.TEMP.HP_LWT,
                    AboutName=required_names.TEMP.HP_LWT,
                    TelemetryName=TelemetryName.WaterTempCTimes1000,
                ),
                ChStub(
                    ChannelName=required_names.TEMP.HP_EWT,
                    AboutName=required_names.TEMP.HP_EWT,
                    TelemetryName=TelemetryName.WaterTempCTimes1000,
                ),
                ChStub(
                    ChannelName=required_names.TEMP.STORE_HOT_PIPE,
                    AboutName=required_names.TEMP.STORE_HOT_PIPE,
                    TelemetryName=TelemetryName.WaterTempCTimes1000,
                ),
                ChStub(
                    ChannelName=required_names.TEMP.STORE_COLD_PIPE,
                    AboutName=required_names.TEMP.STORE_COLD_PIPE,
                    TelemetryName=TelemetryName.WaterTempCTimes1000,
                ),
                ChStub(
                    ChannelName=required_names.TEMP.BUFFER_HOT_PIPE,
                    AboutName=required_names.TEMP.BUFFER_HOT_PIPE,
                    TelemetryName=TelemetryName.WaterTempCTimes1000,
                ),
                ChStub(
                    ChannelName=required_names.TEMP.BUFFER_COLD_PIPE,
                    AboutName=required_names.TEMP.BUFFER_COLD_PIPE,
                    TelemetryName=TelemetryName.WaterTempCTimes1000,
                ),
                ChStub(
                    ChannelName=required_names.TEMP.OAT,
                    AboutName=required_names.TEMP.OAT,
                    TelemetryName=TelemetryName.AirTempCTimes1000,
                ),
            ],
        )
        self.flow = [
            ChStub(
                ChannelName=required_names.DIST_FLOW,
                AboutName=required_names.DIST_FLOW,
                TelemetryName=TelemetryName.GpmTimes100,
            ),
            ChStub(
                ChannelName=required_names.PRIMARY_FLOW,
                AboutName=required_names.PRIMARY_FLOW,
                TelemetryName=TelemetryName.GpmTimes100,
            ),
            ChStub(
                ChannelName=required_names.STORE_FLOW,
                AboutName=required_names.STORE_FLOW,
                TelemetryName=TelemetryName.GpmTimes100,
            ),
        ]
        self.zone = {}
        for zone_name in required_names.TEMP.ZONE_LIST:  # e.g. zone1-downstairs
            self.zone[zone_name] = [
                ChStub(
                    ChannelName=f"{zone_name}-temp".lower(),
                    AboutName=zone_name,
                    TelemetryName=TelemetryName.AirTempFTimes1000,
                ),
                ChStub(
                    ChannelName=f"{zone_name}-set".lower(),
                    AboutName=zone_name,
                    TelemetryName=TelemetryName.AirTempFTimes1000,
                ),
            ]

    def __repr__(self):
        val = "Power Channels\n"
        for ch in self.power:
            val += f"  {ch.ChannelName}: reads {ch.TelemetryName.value} of ShNode {ch.AboutName}\n"
        val += "\n\nCore Temp Channels:\n"
        for ch in self.core_temp:
            val += f"  {ch.ChannelName}: reads {ch.TelemetryName.value} of ShNode {ch.AboutName}\n"
        val += "\n\nThermostat Zone Channels:\n"
        for zone_name in self.zone:
            for ch in self.zone[zone_name]:
                val += f"    {ch.ChannelName}: reads {ch.TelemetryName.value} of ShNode {ch.AboutName}\n"

        return val


@dataclass
class House0StubConfig:
    add_stub_scada: bool = True
    add_stub_george_hack: bool = False
    george_hack_display_name: str = "George Hack: First automated control node"
    atn_gnode_alias: str = "atn.gnode"
    scada_gnode_alias: str = "dummy.scada.gnode"
    scada_display_name: str = "Dummy Scada"
    add_stub_power_meter: bool = True
    power_meter_cac_display_name: str = "Dummy Power Meter Cac"
    power_meter_component_display_name: str = "Dummy Power Meter Component"
    power_meter_node_display_name: str = "Dummy Power Meter"
    hp_pwr_display_name: str = "Dummy Heat Pump"


class House0LayoutDb(LayoutDb):
    names: House0RequiredNames
    channel_stubs: House0ChStubs

    def __init__(
        self,
        existing_layout: Optional[LayoutIDMap] = None,
        cacs: Optional[list[ComponentAttributeClassGt]] = None,
        components: Optional[list[ComponentGt]] = None,
        nodes: Optional[list[SpaceheatNodeGt]] = None,
        channels: Optional[list[DataChannelGt]] = None,
        add_stubs: bool = False,
        stub_config: Optional[House0StubConfig] = None,
        total_store_tanks: int = 3,
        zone_list: List[str] = ["single"],
    ):
        super().__init__(
            existing_layout=existing_layout,
            cacs=cacs,
            components=components,
            nodes=nodes,
            channels=channels,
        )
        self.total_store_tanks = total_store_tanks
        self.zone_list = zone_list
        self.names = House0RequiredNames(total_store_tanks, zone_list)
        self.channel_stubs = House0ChStubs(total_store_tanks, zone_list)
        if add_stubs:
            self.add_stubs(stub_config)

    def add_stubs(self, cfg: Optional[House0StubConfig] = None):
        if cfg is None:
            cfg = House0StubConfig()
        if cfg.add_stub_scada:
            self.add_stub_scada(cfg)
        if cfg.add_stub_power_meter:
            self.add_stub_power_meter(cfg)

    def add_stub_scada(self, cfg: Optional[House0StubConfig] = None):
        if cfg is None:
            cfg = House0StubConfig()
        if self.loaded.gnodes:
            self.misc.update(self.loaded.gnodes)
        else:
            self.misc["MyAtomicTNodeGNode"] = {
                "GNodeId": str(uuid.uuid4()),
                "Alias": cfg.atn_gnode_alias,
                "DisplayName": "ATN GNode",
                "GNodeStatusValue": "Active",
                "PrimaryGNodeRoleAlias": "AtomicTNode",
            }
            self.misc["MyScadaGNode"] = {
                "GNodeId": str(uuid.uuid4()),
                "Alias": cfg.atn_gnode_alias + ".scada",
                "DisplayName": "Scada GNode",
                "GNodeStatusValue": "Active",
                "PrimaryGNodeRoleAlias": "Scada",
            }
            self.misc["MyTerminalAssetGNode"] = {
                "GNodeId": str(uuid.uuid4()),
                "Alias": cfg.atn_gnode_alias + ".ta",
                "DisplayName": "Dummy TerminalAsset",
                "GNodeStatusValue": "Active",
                "PrimaryGNodeRoleAlias": "TerminalAsset",
            }

        self.add_nodes([
            SpaceheatNodeGt(
                sh_node_id=self.make_node_id(self.names.SCADA),
                name=self.names.SCADA,
                handle=SCADA_START_HANDLE,
                actor_class=ActorClass.Scada,
                display_name=cfg.scada_display_name,
                strategy=SCADA_STRATEGY,
                zone_list=self.zone_list,
                total_store_tanks=self.total_store_tanks,
            ),
            SpaceheatNodeGt(
                ShNodeId=self.make_node_id(self.names.HOME_ALONE),
                Name=self.names.HOME_ALONE,
                Handle=self.names.HOME_ALONE,
                ActorClass=ActorClass.HomeAlone,
                DisplayName="HomeAlone",
            ),
            SpaceheatNodeGt(
                ShNodeId=self.make_node_id(SCADA_2_NAME),
                Name=SCADA_2_NAME,
                Handle=SCADA_2_NAME,
                ActorClass=ActorClass.Parentless,
                DisplayName="Scada 2",
            ),
        ])

    def add_stub_power_meter(self, cfg: Optional[House0StubConfig] = None):
        if cfg is None:
            cfg = House0StubConfig()
        if not self.cac_id_by_make_model(MakeModel.GRIDWORKS__SIMPM1):
            self.add_cacs(
                [
                    typing.cast(
                        ComponentAttributeClassGt,
                        ElectricMeterCacGt(
                            ComponentAttributeClassId=CACS_BY_MAKE_MODEL[
                                MakeModel.GRIDWORKS__SIMPM1
                            ],
                            MakeModel=MakeModel.GRIDWORKS__SIMPM1,
                            DisplayName=cfg.power_meter_cac_display_name,
                            TelemetryNameList=[TelemetryName.PowerW],
                            MinPollPeriodMs=1000,
                        ),
                    ),
                ],
                "ElectricMeterCacs",
            )
        self.add_components(
            [
                typing.cast(
                    ComponentGt,
                    ElectricMeterComponentGt(
                        ComponentId=self.make_component_id(
                            cfg.power_meter_component_display_name
                        ),
                        ComponentAttributeClassId=CACS_BY_MAKE_MODEL[
                            MakeModel.GRIDWORKS__SIMPM1
                        ],
                        DisplayName=cfg.power_meter_component_display_name,
                        ConfigList=[
                            ChannelConfig(
                                ChannelName="hp-idu-pwr",
                                PollPeriodMs=1000,
                                CapturePeriodS=60,
                                AsyncCapture=True,
                                AsyncCaptureDelta=20,
                                Exponent=1,
                                Unit=Unit.W,
                            )
                        ],
                        EgaugeIoList=[],
                    ),
                )
            ],
            "ElectricMeterComponents",
        )

        self.add_nodes([
            SpaceheatNodeGt(
                ShNodeId=self.make_node_id(f"s.{self.names.PRIMARY_POWER_METER}"),
                Name=self.names.PRIMARY_POWER_METER,
                ActorClass=ActorClass.PowerMeter,
                DisplayName=cfg.power_meter_node_display_name,
                ComponentId=self.component_id_by_display_name(
                    cfg.power_meter_component_display_name
                ),
            ),
            SpaceheatNodeGt(
                ShNodeId=self.make_node_id(self.names.HP_IDU),
                Name=self.names.HP_IDU,
                ActorClass=ActorClass.NoActor,
                DisplayName=cfg.hp_pwr_display_name,
                InPowerMetering=True,
            ),
        ])
