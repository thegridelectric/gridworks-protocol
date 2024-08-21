from typing import Dict, cast

from pydantic import BaseModel

from gwproto.enums import (
    ActorClass,
    MakeModel,
    TelemetryName,
    ThermistorDataMethod,
    Unit,
)
from gwproto.layout_gen.layout_db import LayoutDb
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import (
    Ads111xBasedCacGt,
    DataChannelGt,
    SpaceheatNodeGt,
    ThermistorDataProcessingConfig,
)
from gwproto.types.ads111x_based_component_gt import Ads111xBasedComponentGt
from gwproto.types.channel_config import (
    ChannelConfig,
)  # Replaces TelemetryReportingConfig
from gwproto.types.component_gt import ComponentGt

# add_tsnap_multipurpose -> add_ads1115_b98_v1


class AdsSensorCfg(BaseModel):
    ChannelName: str
    TerminalBlockIdx: int
    ThermistorMakeModel: MakeModel = MakeModel.TEWA__TT0P10KC3T1051500
    TName: TelemetryName = TelemetryName.WaterTempCTimes1000
    AsyncCapture: bool = True
    AsyncCaptureDelta: int = 250
    CapturePeriodS: int = 60
    DisplayName: str
    MakeNode: bool = True
    # Using a forward reference here resolves a pydantic exception generated when this field
    # is actually set, as in tlayouts/gen_oak.py. I don't know why we should need a forward
    # reference, since MakeModel is imported above. The generated error is:
    #
    # pydantic.errors.ConfigError: field "MakeModel" not yet prepared so
    #   type is still a ForwardRef, you might need to call
    #  AdsSensorCfg.update_forward_refs().


class AdsGenCfg(BaseModel):
    NodeName: str
    NodeDisplayName: str = "GridWorks MultiTemp1"
    ComponentDisplayName: str = "GridWorks 12-Channel Ads-1115 based I2c Temp Sensor"
    AdsMakeModel: MakeModel = MakeModel.GRIDWORKS__MULTITEMP1
    CfgByAboutName: Dict[str, AdsSensorCfg]
    TerminalAssetAlias: str


def add_ads1115(db: LayoutDb, tsnap: AdsGenCfg) -> None:
    make_model = tsnap.AdsMakeModel
    if make_model not in {
        MakeModel.GRIDWORKS__MULTITEMP1,
        MakeModel.GRIDWORKS__SIMMULTITEMP,
    }:
        raise Exception(
            f"make_model {make_model} is not a known Ads111xBased MakeModel!"
        )
    if not db.cac_id_by_make_model(make_model):
        db.add_cacs(
            [
                cast(
                    ComponentGt,
                    Ads111xBasedCacGt(
                        component_attribute_class_id=CACS_BY_MAKE_MODEL[make_model],
                        min_poll_period_ms=200,
                        make_model=make_model,
                        ads_i2c_address_list=["0x4b", "0x49", "0x48"],
                        total_terminal_blocks=12,
                        telemetry_name_list=[
                            TelemetryName.WaterTempCTimes1000,
                            TelemetryName.AirTempCTimes1000,
                        ],
                        display_name=tsnap.ComponentDisplayName,
                    ),
                )
            ],
            "Ads111xBasedCacs",
        )
    cac = db.cacs_by_id[CACS_BY_MAKE_MODEL[make_model]]

    db.add_components(
        [
            cast(
                ComponentGt,
                Ads111xBasedComponentGt(
                    component_id=db.make_component_id(tsnap.ComponentDisplayName),
                    component_attribute_class_id=cac.component_attribute_class_id,
                    display_name=tsnap.ComponentDisplayName,
                    open_voltage_by_ads=[4.95, 4.95, 4.95],
                    config_list=[
                        ChannelConfig(
                            channel_name=tsnap.CfgByAboutName[about_node].ChannelName,
                            poll_period_ms=cac.min_poll_period_ms,
                            capture_period_s=tsnap.CfgByAboutName[
                                about_node
                            ].CapturePeriodS,
                            async_capture=tsnap.CfgByAboutName[about_node].AsyncCapture,
                            async_capture_delta=tsnap.CfgByAboutName[
                                about_node
                            ].AsyncCaptureDelta,
                            exponent=3,
                            unit=Unit.Celcius,
                        )
                        for about_node in tsnap.CfgByAboutName
                    ],
                    ThermistorConfigList=[
                        ThermistorDataProcessingConfig(
                            channel_name=tsnap.CfgByAboutName[about_node].ChannelName,
                            terminal_block_idx=tsnap.CfgByAboutName[
                                about_node
                            ].TerminalBlockIdx,
                            thermistor_make_model=tsnap.CfgByAboutName[
                                about_node
                            ].ThermistorMakeModel,
                            data_processing_method=ThermistorDataMethod.SimpleBeta,
                            data_processing_description="Using beta of 3977",
                        )
                        for about_node in tsnap.CfgByAboutName
                    ],
                ),
            )
        ],
        "Ads111xBasedComponents",
    )

    db.add_nodes(
        [
            SpaceheatNodeGt(
                sh_node_id=db.make_node_id(tsnap.NodeName),
                name=tsnap.NodeName,
                actor_class=ActorClass.MultipurposeSensor,
                display_name=tsnap.NodeDisplayName,
                component_id=db.component_id_by_display_name(
                    tsnap.ComponentDisplayName
                ),
            )
        ]
        + [
            SpaceheatNodeGt(
                sh_node_id=db.make_node_id(ch_name),
                name=ch_name,
                actor_class=ActorClass.NoActor,
                display_name=f"{tsnap.CfgByAboutName[ch_name].DisplayName} (Ch {tsnap.CfgByAboutName[ch_name].TerminalBlockIdx}, {tsnap.CfgByAboutName[ch_name].ThermistorMakeModel.value})",
            )
            for ch_name in tsnap.CfgByAboutName
            if tsnap.CfgByAboutName[ch_name].MakeNode
        ]
    )

    db.add_channels(
        [
            DataChannelGt(
                name=v.ChannelName,
                display_name=f"{v.DisplayName} Temperature",
                about_node_name=k,
                captured_by_node_name=tsnap.NodeName,
                telemetry_name=v.TName,
                terminal_asset_alias=tsnap.TerminalAssetAlias,
                id=db.make_channel_id(v.ChannelName),
            )
            for k, v in tsnap.CfgByAboutName.items()
        ]
    )
