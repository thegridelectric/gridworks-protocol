from typing import Optional, cast

from gwproto.enums import ActorClass, MakeModel, TelemetryName
from gwproto.enums import Unit as UnitEnum
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
from pydantic import BaseModel

from layout_gen.house_0 import House0LayoutDb


class EGaugeIOGenCfg(BaseModel):
    AboutNodeName: str
    NodeDisplayName: str
    EGaugeAddress: int
    AsyncCaptureDelta: int = 10
    InPowerMetering: bool = False

    def output_config(self, **kwargs) -> ChannelConfig:
        kwargs_used = dict(
            ChannelName=f"{self.AboutNodeName}-pwr",
            PollPeriodMs=1000,
            CapturePeriodS=300,
            AsyncCapture=True,
            AsyncCaptureDelta=self.AsyncCaptureDelta,
            Exponent=0,
            Unit=UnitEnum.W,
        )
        kwargs_used.update(kwargs)
        return ChannelConfig(**kwargs_used)

    def egauge_register_config(self, **kwargs) -> EgaugeRegisterConfig:
        kwargs_used = dict(
            Address=self.EGaugeAddress,
            Name="",
            Description="change in value",
            Type="f32",
            Denominator=1,
            Unit="W",
        )
        kwargs_used.update(kwargs)
        return EgaugeRegisterConfig(**kwargs_used)

    def node(self, db: House0LayoutDb) -> SpaceheatNodeGt:
        return SpaceheatNodeGt(
            ShNodeId=db.make_node_id(self.AboutNodeName),
            Name=self.AboutNodeName,
            ActorClass=ActorClass.NoActor,
            DisplayName=self.NodeDisplayName,
            InPowerMetering=self.InPowerMetering,
        )

    def egauge_io(
        self,
        egauge_kwargs: Optional[dict] = None,
    ) -> EgaugeIo:
        if egauge_kwargs is None:
            egauge_kwargs = {}
        return EgaugeIo(
            ChannelName=f"{self.AboutNodeName}-pwr",
            InputConfig=self.egauge_register_config(**egauge_kwargs),
        )


class EGaugeGenCfg(BaseModel):
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
                        ComponentAttributeClassId=CACS_BY_MAKE_MODEL[
                            MakeModel.EGAUGE__4030
                        ],
                        MakeModel=MakeModel.EGAUGE__4030,
                        PollPeriodMs=1000,
                        DisplayName="EGauge 4030",
                        TelemetryNameList=[
                            TelemetryName.PowerW,
                            TelemetryName.MilliWattHours,
                            TelemetryName.VoltageRmsMilliVolts,
                            TelemetryName.CurrentRmsMicroAmps,
                            TelemetryName.FrequencyMicroHz,
                        ],
                        MinPollPeriodMs=1000,
                        DefaultBaud=9600,
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

    db.add_channels(
        [
            DataChannelGt(
                Name=stub.ChannelName,
                AboutNodeName=stub.AboutName,
                TelemetryName=stub.TelemetryName,
                CapturedByNodeName=f"s.{db.short_names.REV_GRADE_POWER_METER}",
                DisplayName=stub.DisplayName,
                Id=db.make_channel_id(stub.ChannelName),
            )
            for stub in db.channel_stubs.power
        ]
    )

    given_names = set(map(lambda x: x.AboutNodeName, egauge.IOs))
    required_names= set(map(lambda x: x.AboutName, db.channel_stubs.power))
    missing_names = required_names - given_names
    if missing_names:
        raise ValueError(f"EGauge config is missing these node names:  {', '.join(missing_names)} ")
    
    db.add_channels(
        [
            DataChannelGt(
                Name=f"{node_name}-pwr",
                AboutNodeName=node_name,
                TelemetryName=TelemetryName.PowerW,
                CapturedByNodeName=f"s.{db.short_names.REV_GRADE_POWER_METER}",
                DisplayName=f"{node_name} Power",
                Id=db.make_channel_id(f"{node_name}-pwr"),
            )
            for node_name in (given_names - required_names)
        ]
    )
