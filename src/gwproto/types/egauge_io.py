"""Type egauge.io, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import (
    SpaceheatName,
)
from gwproto.types.egauge_register_config import (
    EgaugeRegisterConfig,
)


class EgaugeIo(BaseModel):
    ChannelName: SpaceheatName
    InputConfig: EgaugeRegisterConfig
    TypeName: Literal["egauge.io"] = "egauge.io"
    Version: Literal["001"] = "001"
