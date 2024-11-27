"""Type dfr.config, version 000"""

from typing import Literal

from pydantic import PositiveInt

from gwproto.named_types import ChannelConfig


class DfrConfig(ChannelConfig):
    OutputIdx: PositiveInt
    InitialVoltsTimes100: PositiveInt
    TypeName: Literal["dfr.config"] = "dfr.config"
    Version: Literal["000"] = "000"
