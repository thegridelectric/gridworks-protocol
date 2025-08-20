"""Type ads.channel.config, version 000"""

from typing import Literal, Optional

from pydantic import ConfigDict, PositiveInt

from gwproto.enums import MakeModel, ThermistorDataMethod
from gwproto.named_types.channel_config import ChannelConfig


class AdsChannelConfig(ChannelConfig):
    terminal_block_idx: PositiveInt
    thermistor_make_model: MakeModel
    data_processing_method: Optional[ThermistorDataMethod] = None
    data_processing_description: Optional[str] = None
    type_name: Literal["ads.channel.config"] = "ads.channel.config"
    version: str = "000"

    model_config = ConfigDict(extra="allow", use_enum_values=True)
