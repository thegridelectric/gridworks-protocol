"""Type dfr.component.gt, version 000"""

from collections.abc import Sequence
from typing import Literal

from pydantic import PositiveInt

from gwproto.named_types import ComponentGt
from gwproto.named_types.dfr_config import DfrConfig


class DfrComponentGt(ComponentGt):
    config_list: Sequence[DfrConfig]
    i2c_address_list: list[PositiveInt]
    type_name: Literal["dfr.component.gt"] = "dfr.component.gt"
    version: str = "000"
