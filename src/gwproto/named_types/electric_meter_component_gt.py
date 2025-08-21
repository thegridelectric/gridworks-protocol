"""Type electric.meter.component.gt, version 001"""

from typing import Literal, Optional

from pydantic import PositiveInt

from gwproto.named_types.component_gt import ComponentGt
from gwproto.named_types.electric_meter_channel_config import ElectricMeterChannelConfig


class ElectricMeterComponentGt(ComponentGt):
    """ASL schema of record [electric.meter.component.gt v001](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/electric.meter.component.gt.001.yaml)"""

    config_list: list[ElectricMeterChannelConfig]
    modbus_host: Optional[str] = None
    modbus_port: Optional[PositiveInt] = None
    type_name: Literal["electric.meter.component.gt"] = "electric.meter.component.gt"
    version: Literal["001"] = "001"
