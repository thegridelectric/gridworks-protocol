"""Type electric.meter.channel.config, version 000"""

from typing import Literal, Optional

from gwproto.named_types.channel_config import ChannelConfig
from gwproto.named_types.egauge_register_config import (
    EgaugeRegisterConfig as EgaugeConfig,
)


class ElectricMeterChannelConfig(ChannelConfig):
    """ASL schema of record [electric.meter.channel.config v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/electric.meter.channel.config.000.yaml)"""

    egauge_register_config: Optional[EgaugeConfig] = None
    type_name: Literal["electric.meter.channel.config"] = (
        "electric.meter.channel.config"
    )
    version: str = "000"
