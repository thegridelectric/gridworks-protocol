"""Type electric.meter.cac.gt, version 001"""

from typing import Literal, Optional

from gwproto.enums import TelemetryName
from gwproto.named_types import ComponentAttributeClassGt


class ElectricMeterCacGt(ComponentAttributeClassGt):
    """ASL schema of record [electric.meter.cac.gt v001](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/electric.meter.cac.001.yaml)"""

    telemetry_name_list: list[TelemetryName]
    default_baud: Optional[int] = None
    type_name: Literal["electric.meter.cac.gt"] = "electric.meter.cac.gt"
    version: Literal["001"] = "001"
