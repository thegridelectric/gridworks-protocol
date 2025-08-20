"""Type dfr.config, version 000"""

from typing import Literal

from pydantic import PositiveInt, StrictInt

from gwproto.named_types import ChannelConfig


class DfrConfig(ChannelConfig):
    """ASL schema of record [dfr.config v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/dfr.config.000.yaml)"""

    output_idx: PositiveInt
    initial_volts_times_100: StrictInt
    type_name: Literal["dfr.config"] = "dfr.config"
    version: str = "000"
