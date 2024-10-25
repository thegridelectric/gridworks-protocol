from typing import Literal, Optional

from gwproto.enums import GpmFromHzMethod, HzCalcMethod, MakeModel
from gwproto.property_format import SpaceheatName
from gwproto.types.component_gt import ComponentGt


class PicoFlowModuleComponentGt(ComponentGt):
    Enabled: bool
    PicoHwUid: str
    FlowNodeName: SpaceheatName
    FlowMeterType: MakeModel = MakeModel.SAIER__SENHZG1WA
    HzCalcMethod: HzCalcMethod
    GpmFromHzMethod: GpmFromHzMethod
    ConstantGallonsPerTick: float
    SendHz: bool = True
    SendGallons: bool = False
    SendTickLists: bool = False
    NoFlowMs: int
    PublishEmptyTicklistAfterS: int
    AsyncCaptureThresholdGpmTimes10: int
    PublishTicklistPeriodS: Optional[int] = 10  # Required for Hall Params
    PublishTicklistLength: Optional[int] = 300  # required for Reed Params
    ExpAlpha: Optional[float] = 0.5
    CutoffFrequency: Optional[float] = 1.25
    TypeName: Literal["pico.flow.module.component.gt"] = "pico.flow.module.component.gt"
    Version: Literal["000"] = "000"
