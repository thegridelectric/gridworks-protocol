"""Type pico.btu.meter.component.gt, version 000"""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, StrictInt

from gwproto.enums import GpmFromHzMethod, HzCalcMethod, MakeModel, TempCalcMethod
from gwproto.property_format import (
    SpaceheatName,
)


class PicoBtuMeterComponentGt(BaseModel):
    Enabled: bool
    SerialNumber: str
    FlowNodeName: SpaceheatName
    HotNodeName: SpaceheatName
    ColdNodeName: SpaceheatName
    ReadCt: bool
    CtNodeName: Optional[SpaceheatName] = None
    FlowMeterType: MakeModel
    HzCalcMethod: HzCalcMethod
    TempCalcMethod: TempCalcMethod
    ThermistorBeta: StrictInt
    GpmFromHzMethod: GpmFromHzMethod
    GallonsPerPulse: float
    AsyncCaptureDeltaGpmX100: StrictInt
    AsyncCaptureDeltaCelsiusX100: StrictInt
    AsyncCaptureDeltaCtVoltsX100: Optional[StrictInt] = None
    TypeName: Literal["pico.btu.meter.component.gt"] = "pico.btu.meter.component.gt"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(use_enum_values=True)
