"""Type pipe.flow.sensor.component.gt, version 000"""

from typing import Literal, Optional

from gwproto.types import ComponentGt


class PipeFlowSensorComponentGt(ComponentGt):
    I2cAddress: int
    ConversionFactor: float
    ExpectedMaxGpmTimes100: Optional[int] = None
    TypeName: Literal["pipe.flow.sensor.component.gt"] = "pipe.flow.sensor.component.gt"
