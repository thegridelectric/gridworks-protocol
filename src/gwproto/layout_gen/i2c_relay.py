from typing import Any, Dict, List, cast

from pydantic import BaseModel

from gwproto.enums import (
    ActorClass,
    FsmEventType,
    MakeModel,
    RelayWiringConfig,
    TelemetryName,
    Unit,
)
from gwproto.layout_gen.house_0_layout_db import (
    ADMIN_NAME,
    ADMIN_START_HANDLE,
    KRIDA_MULTIPLEXER_NAME,
)
from gwproto.layout_gen.layout_db import LayoutDb
from gwproto.type_helpers import CACS_BY_MAKE_MODEL
from gwproto.types import (
    ChannelConfig,
    ComponentAttributeClassGt,
    ComponentGt,
    DataChannelGt,
    RelayActorConfig,
    SpaceheatNodeGt,
)
from gwproto.types.i2c_multichannel_dt_relay_component_gt import (
    I2cMultichannelDtRelayComponentGt,
)


class I2cRelayPinCfg(BaseModel):
    RelayIdx: int
    DisplayName: str
    WiringConfig: RelayWiringConfig
    EventType: FsmEventType
    DeEnergizingEvent: Any
    PollPeriodMs: int = 5000
    CapturePeriodS: int = 300
    Boss: str = ADMIN_START_HANDLE


class I2cRelayBoardCfg(BaseModel):
    TerminalAssetAlias: str
    NodeDisplayName: str = "Krida Board Multiplexer"
    ComponentDisplayName: str = "GSCADA double 16-pin Krida I2c Relay boards"
    I2cAddressList: List[int] = [0x20, 0x21]
    RelayMakeModel: MakeModel = MakeModel.KRIDA__DOUBLEEMR16I2CV3
    PinCfgByName: Dict[str, I2cRelayPinCfg]


def add_i2c_relay_board(
    db: LayoutDb,
    board: I2cRelayBoardCfg,
) -> None:
    if board.RelayMakeModel not in {
        MakeModel.KRIDA__DOUBLEEMR16I2CV3,
        MakeModel.KRIDA__EMR16I2CV3,
        MakeModel.GRIDWORKS__SIMDOUBLE16PINI2CRELAY,
    }:
        raise Exception(
            f"make_model {board.RelayMakeModel} is not a I2cMultichannelDtRelayComponentGt MakeModel"
        )
    if board.RelayMakeModel == MakeModel.KRIDA__EMR16I2CV3:
        raise Exception(f"{MakeModel.KRIDA__EMR16I2CV3.value} not implemented yet!!")
    db.add_cacs(
        [
            ComponentAttributeClassGt(
                component_attribute_class_id=CACS_BY_MAKE_MODEL[board.RelayMakeModel],
                make_model=board.RelayMakeModel,
                display_name=board.ComponentDisplayName,
                min_poll_period_ms=200,
            )
        ],
        "OtherCacs",
    )

    db.add_components(
        [
            cast(
                ComponentGt,
                I2cMultichannelDtRelayComponentGt(
                    component_id=db.make_component_id(board.ComponentDisplayName),
                    component_attribute_class_id=CACS_BY_MAKE_MODEL[
                        board.RelayMakeModel
                    ],
                    i2c_address_list=[0x20, 0x21],
                    config_list=[
                        ChannelConfig(
                            channel_name=f"{v}-energization",
                            poll_period_ms=board.PinCfgByName[v].PollPeriodMs,
                            capture_period_s=board.PinCfgByName[v].CapturePeriodS,
                            async_capture=True,
                            async_capture_delta=1,
                            exponent=0,
                            unit=Unit.Unitless,
                        )
                        for v in board.PinCfgByName
                    ],
                    relay_config_list=[
                        RelayActorConfig(
                            relay_idx=board.PinCfgByName[v].RelayIdx,
                            actor_name=v,
                            wiring_config=board.PinCfgByName[v].WiringConfig,
                            event_type=board.PinCfgByName[v].EventType,
                            de_energizing_event=board.PinCfgByName[v].DeEnergizingEvent,
                        )
                        for v in board.PinCfgByName
                    ],
                    display_name=f"{board.ComponentDisplayName}, as component",
                ),
            )
        ],
        "I2cMultichannelDtRelayComponents",
    )

    db.add_nodes(
        [
            SpaceheatNodeGt(
                sh_node_id=db.make_node_id(KRIDA_MULTIPLEXER_NAME),
                name=KRIDA_MULTIPLEXER_NAME,
                actor_class=ActorClass.I2cRelayMultiplexer,
                display_name=board.NodeDisplayName,
                component_id=db.component_id_by_display_name(
                    f"{board.ComponentDisplayName}, as component"
                ),
            ),
            SpaceheatNodeGt(
                sh_node_id=db.make_node_id(ADMIN_NAME),
                name=ADMIN_NAME,
                handle=ADMIN_START_HANDLE,
                actor_class=ActorClass.Admin,
                display_name="Admin GNode",
            ),
        ]
        + [
            SpaceheatNodeGt(
                sh_node_id=db.make_node_id(name),
                name=name,
                handle=f"{board.PinCfgByName[name].Boss}.{name}",
                actor_class=ActorClass.Relay,
                display_name=board.PinCfgByName[name].DisplayName,
                component_id=db.component_id_by_display_name(
                    f"{board.ComponentDisplayName}, as component"
                ),
            )
            for name in board.PinCfgByName
        ]
    )

    db.add_channels(
        [
            DataChannelGt(
                name=f"{name}-energization",
                display_name=f"{v.DisplayName}",
                about_node_name=name,
                captured_by_node_name=KRIDA_MULTIPLEXER_NAME,
                telemetry_name=TelemetryName.RelayState,
                terminal_asset_alias=board.TerminalAssetAlias,
                id=db.make_channel_id(f"{name}-energization"),
            )
            for name, v in board.PinCfgByName.items()
        ]
    )
