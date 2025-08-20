"""Type dfr.config, version 000"""

from typing import Literal

from pydantic import PositiveInt, StrictInt

from gwproto.named_types import ChannelConfig


class DfrConfig(ChannelConfig):
    output_idx: PositiveInt
    initial_volts_times_100: StrictInt
    type_name: Literal["dfr.config"] = "dfr.config"
    version: str = "000"
