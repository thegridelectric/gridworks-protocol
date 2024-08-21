from typing import Optional, cast

from pydantic import BaseModel

from gwproto.enums import ActorClass, MakeModel, TelemetryName
from gwproto.enums import Unit as UnitEnum
from gwproto.layout_gen.house_0_layout_db import House0LayoutDb
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import (
    ChannelConfig,
    ComponentAttributeClassGt,
    ComponentGt,
    DataChannelGt,
    EgaugeIo,
    EgaugeRegisterConfig,
    ElectricMeterCacGt,
    SpaceheatNodeGt,
)
from gwproto.types.electric_meter_component_gt import ElectricMeterComponentGt


class EGaugeIOGenCfg(BaseModel):
    AboutNodeName: str
    NodeDisplayName: str
    EGaugeAddress: int
    AsyncCaptureDelta: int = 10
    InPowerMetering: bool = False
    NameplatePowerW: Optional[int] = None

    def output_config(self, **kwargs) -> ChannelConfig:
        kwargs_used = dict(
            channel_name=f"{self.AboutNodeName}-pwr",
            poll_period_ms=1000,
            capture_period_s=300,
            async_capture=True,
            async_capture_delta=self.AsyncCaptureDelta,
            exponent=0,
            unit=UnitEnum.W,
        )
        kwargs_used.update(kwargs)
        return ChannelConfig(**kwargs_used)

    def egauge_register_config(self, **kwargs) -> EgaugeRegisterConfig:
        kwargs_used = dict(
            address=self.EGaugeAddress,
            name="",
            description="change in value",
            type="f32",
            denominator=1,
            unit="W",
        )
        kwargs_used.update(kwargs)
        return EgaugeRegisterConfig(**kwargs_used)

    def node(self, db: House0LayoutDb) -> SpaceheatNodeGt:
        return SpaceheatNodeGt(
            sh_node_id=db.make_node_id(self.AboutNodeName),
            name=self.AboutNodeName,
            actor_class=ActorClass.NoActor,
            display_name=self.NodeDisplayName,
            in_power_metering=self.InPowerMetering,
            nameplate_power_w=self.NameplatePowerW,
        )

    def egauge_io(
        self,
        egauge_kwargs: Optional[dict] = None,
    ) -> EgaugeIo:
        if egauge_kwargs is None:
            egauge_kwargs = {}
        return EgaugeIo(
            channel_name=f"{self.AboutNodeName}-pwr",
            input_config=self.egauge_register_config(**egauge_kwargs),
        )


class EGaugeGenCfg(BaseModel):
    TerminalAssetAlias: str
    NodeName: str
    HwUid: str
    ModbusHost: str
    ModbusPort: int = 502
    IOs: list[EGaugeIOGenCfg]

    def egauge_ios(
        self,
        egauge_kwargs: Optional[dict] = None,
    ) -> list[EgaugeIo]:
        if egauge_kwargs is None:
            egauge_kwargs = {}

        return [io.egauge_io(egauge_kwargs=egauge_kwargs) for io in self.IOs]

    def config_list(self, **kwargs):
        return [io.output_config(**kwargs) for io in self.IOs]


def add_house0_egauge(
    db: House0LayoutDb,
    egauge: EGaugeGenCfg,
) -> None:
    if not db.cac_id_by_make_model(MakeModel.EGAUGE__4030):
        db.add_cacs(
            [
                cast(
                    ComponentAttributeClassGt,
                    ElectricMeterCacGt(
                        component_attribute_class_id=CACS_BY_MAKE_MODEL[
                            MakeModel.EGAUGE__4030
                        ],
                        make_model=MakeModel.EGAUGE__4030,
                        min_poll_period_ms=1000,
                        display_name="EGauge 4030",
                        telemetry_name_list=[
                            TelemetryName.PowerW,
                            TelemetryName.MilliWattHours,
                            TelemetryName.VoltageRmsMilliVolts,
                            TelemetryName.CurrentRmsMicroAmps,
                            TelemetryName.FrequencyMicroHz,
                        ],
                        default_baud=9600,
                    ),
                )
            ],
            "ElectricMeterCacs",
        )
    io_list = egauge.egauge_ios()

    db.add_components(
        [
            cast(
                ComponentGt,
                ElectricMeterComponentGt(
                    ComponentId=db.make_component_id(egauge.ModbusHost),
                    ComponentAttributeClassId=CACS_BY_MAKE_MODEL[
                        MakeModel.EGAUGE__4030
                    ],
                    DisplayName=egauge.ModbusHost,
                    ConfigList=egauge.config_list(),
                    HwUid=egauge.HwUid,
                    ModbusHost=egauge.ModbusHost,
                    ModbusPort=egauge.ModbusPort,
                    EgaugeIoList=io_list,
                ),
            )
        ],
        "ElectricMeterComponents",
    )
    db.add_nodes(
        [
            SpaceheatNodeGt(
                ShNodeId=db.make_node_id(egauge.NodeName),
                Name=egauge.NodeName,
                ActorClass=ActorClass.PowerMeter,
                DisplayName="Primary Power Meter",
                ComponentId=db.component_id_by_display_name(egauge.ModbusHost),
            )
        ]
        + [io.node(db) for io in egauge.IOs]
    )

    db.add_channels([
        DataChannelGt(
            name=stub.ChannelName,
            about_node_name=stub.AboutName,
            telemetry_name=stub.TelemetryName,
            captured_by_node_name=db.names.PRIMARY_POWER_METER,
            display_name=stub.ChannelName,
            terminal_asset_alias=egauge.TerminalAssetAlias,
            in_power_metering=stub.InPowerMetering,
            id=db.make_channel_id(stub.ChannelName),
        )
        for stub in db.channel_stubs.power
    ])

    given_names = set(map(lambda x: x.AboutNodeName, egauge.IOs))
    required_names = set(map(lambda x: x.AboutName, db.channel_stubs.power))
    missing_names = required_names - given_names
    if missing_names:
        raise ValueError(
            f"EGauge config is missing these node names:  {', '.join(missing_names)} "
        )

    db.add_channels([
        DataChannelGt(
            name=f"{node_name}-pwr",
            about_node_name=node_name,
            telemetry_name=TelemetryName.PowerW,
            captured_by_node_name=db.names.PRIMARY_POWER_METER,
            terminal_asset_alias=egauge.TerminalAssetAlias,
            display_name=f"{node_name} Power",
            id=db.make_channel_id(f"{node_name}-pwr"),
        )
        for node_name in (given_names - required_names)
    ])
