"""Type keyparam.change.log, version 000"""

from typing import Literal

from gw.named_types import GwBase
from pydantic import ConfigDict, model_validator
from typing_extensions import Self

from gwproto.enums import KindOfParam
from gwproto.property_format import (
    LeftRightDotStr,
    check_is_log_style_date_with_millis,
)


class KeyparamChangeLog(GwBase):
    """ASL schema of record [keyparam.change.log v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/keyparam.change.log.000.yaml)"""

    about_node_alias: LeftRightDotStr
    change_time_utc: str
    author: str
    param_name: str
    description: str
    kind: KindOfParam
    type_name: Literal["keyparam.change.log"] = "keyparam.change.log"
    version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def _check_change_time_utc(self) -> Self:
        try:
            check_is_log_style_date_with_millis(self.change_time_utc)
        except ValueError as e:
            raise ValueError(
                f"ChangeTimeUtc failed LogStyleDateWithMillis format validation: {e}",
            ) from e
        return self
