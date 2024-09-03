"""Type electric.meter.cac.gt, version 000"""

from typing import Literal, Optional

from gwproto.enums import LocalCommInterface, TelemetryName
from gwproto.types import ComponentAttributeClassGt


class ElectricMeterCacGt(ComponentAttributeClassGt):
    TelemetryNameList: list[TelemetryName]
    PollPeriodMs: int
    Interface: LocalCommInterface
    DefaultBaud: Optional[int] = None
    TypeName: Literal["electric.meter.cac.gt"] = "electric.meter.cac.gt"
