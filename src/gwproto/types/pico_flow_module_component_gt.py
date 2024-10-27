import re
from typing import Literal, Optional

from pydantic import field_validator

from gwproto.enums import GpmFromHzMethod, HzCalcMethod, MakeModel
from gwproto.property_format import SpaceheatName
from gwproto.types.component_gt import ComponentGt


class PicoFlowModuleComponentGt(ComponentGt):
    Enabled: bool
    SerialNumber: str
    HwUid: str  # not optional - this is the pico HwUid
    FlowNodeName: SpaceheatName
    FlowMeterType: MakeModel = MakeModel.SAIER__SENHZG1WA
    HzCalcMethod: HzCalcMethod
    GpmFromHzMethod: GpmFromHzMethod
    ConstantGallonsPerTick: float
    SendHz: bool = True
    SendGallons: bool = False
    SendTickLists: bool = False
    NoFlowMs: int
    AsyncCaptureThresholdGpmTimes100: int
    PublishEmptyTicklistAfterS: Optional[int] = None  # Hall Params
    PublishAnyTicklistAfterS: Optional[int] = None  # Reed Params
    PublishTicklistPeriodS: Optional[int] = None  # Required for Hall Params
    PublishTicklistLength: Optional[int] = None  # required for Reed Params
    ExpAlpha: Optional[float] = 0.5
    CutoffFrequency: Optional[float] = 1.25
    TypeName: Literal["pico.flow.module.component.gt"] = "pico.flow.module.component.gt"
    Version: Literal["000"] = "000"

    @field_validator("HwUid")
    @classmethod
    def check_config_list(cls, v: str) -> str:
        """
        Axiom 1: HwUid is of the form 'pico_xxxxxx' where xxxxxx
        are lowercase hex (the last digits of its pico W hw id)
        """
        pattern = r"^pico_[0-9a-f]{6}$"
        if not bool(re.match(pattern, v)):
            raise ValueError("HwUid should be the pico hwuid, eg pico_60e352")
        return v
