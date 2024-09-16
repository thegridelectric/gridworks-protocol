"""Type simple.temp.sensor.cac.gt, version 000"""

from typing import Literal, Optional

from gwproto.enums import TelemetryName, Unit
from gwproto.types import ComponentAttributeClassGt


class SimpleTempSensorCacGt(ComponentAttributeClassGt):
    TypicalResponseTimeMs: int
    Exponent: int
    TempUnit: Unit
    TelemetryName: TelemetryName
    CommsMethod: Optional[str] = None
    TypeName: Literal["simple.temp.sensor.cac.gt"] = "simple.temp.sensor.cac.gt"
