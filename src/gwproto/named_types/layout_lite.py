"""Type layout.lite, version 000"""

from typing import List, Literal

from pydantic import BaseModel, PositiveInt

from gwproto.named_types.data_channel_gt import DataChannelGt
from gwproto.named_types.pico_flow_module_component_gt import PicoFlowModuleComponentGt
from gwproto.named_types.pico_tank_module_component_gt import PicoTankModuleComponentGt
from gwproto.property_format import (
    LeftRightDotStr,
    UTCMilliseconds,
    UUID4Str,
)


class LayoutLite(BaseModel):
    """
    Layout Lite.

    A light-weight version of the layout for a Spaceheat Node, with key parameters about how
    the SCADA operates.
    """

    FromGNodeAlias: LeftRightDotStr
    FromGNodeInstanceId: UUID4Str
    MessageCreatedMs: UTCMilliseconds
    MessageId: UUID4Str
    Strategy: str
    ZoneList: List[str]
    TotalStoreTanks: PositiveInt
    DataChannels: List[DataChannelGt]
    TankModuleComponents: List[PicoTankModuleComponentGt]
    FlowModuleComponents: List[PicoFlowModuleComponentGt]
    TypeName: Literal["layout.lite"] = "layout.lite"
    Version: Literal["000"] = "000"
