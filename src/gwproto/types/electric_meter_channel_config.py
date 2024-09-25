"""Type electric.meter.channel.config, version 000"""

from typing import Literal, Optional

from gwproto.types.channel_config import ChannelConfig
from gwproto.types.egauge_register_config import (
    EgaugeRegisterConfig,
)


class ElectricMeterChannelConfig(ChannelConfig):
    EgaugeRegisterConfig: Optional[EgaugeRegisterConfig]
    TypeName: Literal["electric.meter.channel.config"] = "electric.meter.channel.config"
    Version: Literal["000"] = "000"
