"""Type electric.meter.cac.gt, version 000"""

from typing import Any, Literal, Optional

from gwproto.enums import TelemetryName
from gwproto.types import ComponentAttributeClassGt


class ElectricMeterCacGt(ComponentAttributeClassGt):
    TelemetryNameList: list[TelemetryName]
    DefaultBaud: Optional[int] = None
    TypeName: Literal["electric.meter.cac.gt"] = "electric.meter.cac.gt"

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["MakeModel"] = self.MakeModel.value
        d["TelemetryNameList"] = [elt.value for elt in self.TelemetryNameList]
        return d
