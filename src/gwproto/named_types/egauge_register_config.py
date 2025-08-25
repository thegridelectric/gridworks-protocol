"""Type egauge.register.config, version 000"""

from typing import Literal

from gw.named_types import GwBase
from pydantic import StrictInt


class EgaugeRegisterConfig(GwBase):
    """ASL schema of record [egauge.register.config v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/egauge.register.config.000.yaml)"""

    address: StrictInt
    name: str
    description: str
    type: str
    denominator: StrictInt
    unit: str
    type_name: Literal["egauge.register.config"] = "egauge.register.config"
    version: Literal["000"] = "000"
