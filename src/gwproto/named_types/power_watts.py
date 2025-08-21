"""Type power.watts, version 000"""

from typing import Literal

from gw.named_types import GwBase
from pydantic import StrictInt


class PowerWatts(GwBase):
    """ASL schema of record [power.watts v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/power.watts.000.yaml)"""

    watts: StrictInt
    type_name: Literal["power.watts"] = "power.watts"
    version: Literal["000"] = "000"
