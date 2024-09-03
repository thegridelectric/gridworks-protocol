"""Type multipurpose.sensor.cac.gt, version 000"""

from typing import Literal, Optional

from gwproto.enums import TelemetryName, Unit
from gwproto.types import ComponentAttributeClassGt


class MultipurposeSensorCacGt(ComponentAttributeClassGt):
    PollPeriodMs: int
    Exponent: int
    TempUnit: Unit
    TelemetryNameList: list[TelemetryName]
    MaxThermistors: Optional[int] = None
    DisplayName: Optional[str] = None
    CommsMethod: Optional[str] = None
    TypeName: Literal["multipurpose.sensor.cac.gt"] = "multipurpose.sensor.cac.gt"
