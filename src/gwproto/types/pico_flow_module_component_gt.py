from typing import Literal, Optional

from gwproto.enums import MakeModel
from gwproto.types.component_gt import ComponentGt


class PicoFlowModuleComponentGt(ComponentGt):
    Enabled: bool
    PicoHwUid: str
    FlowMeterType: MakeModel = MakeModel.SAIER__SENHZG1WA
    ConstantGallonsPerTick: float
    SendHz: bool = True
    SendGallons: bool = False
    SendTickLists: bool = False
    NoFlowMs: int
    ExpAlpha: Optional[float] = 0.5
    CutoffFrequency: Optional[float] = 1.25
    TypeName: Literal["pico.flow.module.component.gt"] = "pico.flow.module.component.gt"
    Version: Literal["000"] = "000"
