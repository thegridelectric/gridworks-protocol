"""Type pipe.flow.sensor.cac.gt, version 000"""

from typing import Literal, Optional

from gwproto.types import ComponentAttributeClassGt


class PipeFlowSensorCacGt(ComponentAttributeClassGt):
    CommsMethod: Optional[str] = None
    TypeName: Literal["pipe.flow.sensor.cac.gt"] = "pipe.flow.sensor.cac.gt"
