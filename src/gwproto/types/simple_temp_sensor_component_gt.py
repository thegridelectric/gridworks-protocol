"""Type simple.temp.sensor.component.gt, version 000"""

from typing import Literal, Optional

from gwproto.types import ComponentGt


class SimpleTempSensorComponentGt(ComponentGt):
    Channel: Optional[int] = None
    TypeName: Literal["simple.temp.sensor.component.gt"] = (
        "simple.temp.sensor.component.gt"
    )
