"""Type dfr.component.gt, version 000"""

from collections.abc import Sequence
from typing import Literal

from pydantic import PositiveInt

from gwproto.named_types import ComponentGt
from gwproto.named_types.dfr_config import DfrConfig


class DfrComponentGt(ComponentGt):
    """ASL schema of record [dfr.component.gt v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/dfr.component.gt.000.yaml)"""

    config_list: Sequence[DfrConfig]
    i2c_address_list: list[PositiveInt]
    type_name: Literal["dfr.component.gt"] = "dfr.component.gt"
    version: Literal["000"] = "000"
