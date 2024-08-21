from typing import Dict, cast

from pydantic import BaseModel

from gwproto.enums import ActorClass, MakeModel, TelemetryName, Unit
from gwproto.layout_gen.layout_db import LayoutDb
from gwproto.type_helpers import CACS_BY_MAKE_MODEL, CONVERSION_FACTOR_BY_MODEL
from gwproto.types import (
    ChannelConfig,
    ComponentAttributeClassGt,
    ComponentGt,
    DataChannelGt,
    SpaceheatNodeGt,
)
from gwproto.types.i2c_flow_totalizer_component_gt import I2cFlowTotalizerComponentGt


class I2cFlowSensorCfg(BaseModel):
    I2cAddress: int
    PulseFlowMeterMakeModel: MakeModel
    PollPeriodMs: int = 1000
    DisplayNamePrefix: str


class I2cFlowMeterGenCfg(BaseModel):
    NodeName: str
    NodeDisplayName: str = "GSCADA Atlas EZFLO I2c Pulse Counter Reader"
    ComponentDisplayName: str = "GSCADA Atlas EZFLO I2c Pulse Counter Reader Component"
    TotalizerMakeModel: MakeModel = MakeModel.ATLAS__EZFLO
    CfgByChannelNamePrefix: Dict[str, I2cFlowSensorCfg]


def add_i2c_flow_totalizer(
    db: LayoutDb,
    meter: I2cFlowMeterGenCfg,
) -> None:
    if meter.TotalizerMakeModel not in {
        MakeModel.ATLAS__EZFLO,
        MakeModel.GRIDWORKS__SIMTOTALIZER,
    }:
        raise Exception(
            f"make_model {meter.TotalizerMakeModel} is not a known  I2cFlowTotalizer MakeModel!"
        )
    db.add_cacs(
        [
            ComponentAttributeClassGt(
                ComponentAttributeClassId=CACS_BY_MAKE_MODEL[meter.TotalizerMakeModel],
                MakeModel=meter.TotalizerMakeModel,
                DisplayName=meter.ComponentDisplayName,
                MinPollPeriodMs=300,
            )
        ],
        "OtherCacs",
    )

    configs = [
        [
            ChannelConfig(
                ChannelName=v,
                PollPeriodMs=meter.CfgByChannelNamePrefix[v].PollPeriodMs,
                CapturePeriodS=30,
                AsyncCapture=True,
                AsyncCaptureDelta=20,
                Exponent=2,
                Unit=Unit.Gpm,
            ),
            ChannelConfig(
                ChannelName=f"{v}-integrated",
                PollPeriodMs=meter.CfgByChannelNamePrefix[v].PollPeriodMs,
                CapturePeriodS=30,
                AsyncCapture=True,
                AsyncCaptureDelta=5,
                Exponent=2,
                Unit=Unit.Gallons,
            ),
        ]
        for v in meter.CfgByChannelNamePrefix
    ]

    db.add_components(
        [
            cast(
                ComponentGt,
                I2cFlowTotalizerComponentGt(
                    ComponentId=db.make_component_id(meter.ComponentDisplayName),
                    ComponentAttributeClassId=CACS_BY_MAKE_MODEL[
                        meter.TotalizerMakeModel
                    ],
                    I2cAddressList=[
                        meter.CfgByChannelNamePrefix[v].I2cAddress
                        for v in meter.CfgByChannelNamePrefix
                    ],
                    ConfigList=[elt for sublist in configs for elt in sublist],
                    PulseFlowMeterMakeModelList=[
                        meter.CfgByChannelNamePrefix[v].PulseFlowMeterMakeModel
                        for v in meter.CfgByChannelNamePrefix
                    ],
                    ConversionFactorList=[
                        CONVERSION_FACTOR_BY_MODEL[
                            meter.CfgByChannelNamePrefix[v].PulseFlowMeterMakeModel
                        ]
                        for v in meter.CfgByChannelNamePrefix
                    ],
                    DisplayName=meter.ComponentDisplayName,
                ),
            )
        ],
        "I2cFlowTotalizerComponents",
    )

    extra_nodes = [
        [
            SpaceheatNodeGt(
                ShNodeId=db.make_node_id(ch_prefix),
                Name=ch_prefix,
                ActorClass=ActorClass.NoActor,
                DisplayName=f"{meter.CfgByChannelNamePrefix[ch_prefix].DisplayNamePrefix} "
                f"({meter.CfgByChannelNamePrefix[ch_prefix].PulseFlowMeterMakeModel.value} on i2c {meter.CfgByChannelNamePrefix[ch_prefix].I2cAddress})",
            ),
            # SpaceheatNodeGt(
            #     ShNodeId=db.make_node_id(f"{ch_prefix}-integrated"),
            #     Name=f"{ch_prefix}-integrated",
            #     ActorClass=ActorClass.NoActor,
            #     DisplayName=f"Totalized {meter.CfgByChannelNamePrefix[ch_prefix].DisplayNamePrefix} "
            #     f"({meter.CfgByChannelNamePrefix[ch_prefix].PulseFlowMeterMakeModel.value} on i2c {meter.CfgByChannelNamePrefix[ch_prefix].I2cAddress})",
            # ),
        ]
        for ch_prefix in meter.CfgByChannelNamePrefix
    ]

    db.add_nodes(
        [
            SpaceheatNodeGt(
                ShNodeId=db.make_node_id(meter.NodeName),
                Name=meter.NodeName,
                ActorClass=ActorClass.FlowTotalizer,
                DisplayName=meter.NodeDisplayName,
                ComponentId=db.component_id_by_display_name(meter.ComponentDisplayName),
            )
        ]
        + [
             SpaceheatNodeGt(
                ShNodeId=db.make_node_id(ch_prefix),
                Name=ch_prefix,
                ActorClass=ActorClass.NoActor,
                DisplayName=f"{meter.CfgByChannelNamePrefix[ch_prefix].DisplayNamePrefix} "
                f"({meter.CfgByChannelNamePrefix[ch_prefix].PulseFlowMeterMakeModel.value} on i2c {meter.CfgByChannelNamePrefix[ch_prefix].I2cAddress})",
            )
            for ch_prefix in meter.CfgByChannelNamePrefix
        ]

    )

    db.add_channels(
        [
            DataChannelGt(
                Name=ch_prefix,
                AboutNodeName=ch_prefix,
                TelemetryName=TelemetryName.GpmTimes100,
                CapturedByNodeName=meter.NodeName,
                DisplayName=f"{ch_prefix}",
                Id=db.make_channel_id(ch_prefix),
            )
            for ch_prefix in meter.CfgByChannelNamePrefix
        ]
    )

    db.add_channels(
        [
            DataChannelGt(
                Name=f"{ch_prefix}-integrated",
                AboutNodeName=ch_prefix,
                TelemetryName=TelemetryName.GallonsTimes100,
                CapturedByNodeName=meter.NodeName,
                DisplayName=f"{ch_prefix}, totalized",
                Id=db.make_channel_id(f"{ch_prefix}-integrated"),
            )
            for ch_prefix in meter.CfgByChannelNamePrefix
        ]
    )
