"""Type multipurpose.sensor.component.gt, version 000"""

from typing import List, Literal

from gwproto.types import ComponentGt
from gwproto.types.telemetry_reporting_config import (
    TelemetryReportingConfig,
)


class MultipurposeSensorComponentGt(ComponentGt):
    ChannelList: list[int]
    ConfigList: List[TelemetryReportingConfig]
    TypeName: Literal["multipurpose.sensor.component.gt"] = (
        "multipurpose.sensor.component.gt"
    )
