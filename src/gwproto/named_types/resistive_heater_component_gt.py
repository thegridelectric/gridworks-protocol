"""Type resistive.heater.component.gt, version 000"""

from typing import Literal, Optional

from pydantic import StrictInt

from gwproto.named_types.channel_config import ChannelConfig
from gwproto.named_types.component_gt import ComponentGt


class ResistiveHeaterComponentGt(ComponentGt):
    """ASL schema of record [resistive.heater.component.gt v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/resistive.heater.component.gt.000.yaml)"""

    tested_max_hot_milli_ohms: Optional[StrictInt] = None
    tested_max_cold_milli_ohms: Optional[StrictInt] = None
    config_list: list[ChannelConfig]
    type_name: Literal["resistive.heater.component.gt"] = (
        "resistive.heater.component.gt"
    )
    version: Literal["000"] = "000"
