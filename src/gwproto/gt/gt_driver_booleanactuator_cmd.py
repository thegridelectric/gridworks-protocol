"""gt.driver.booleanactuator.cmd type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator


class GtDriverBooleanactuatorCmd(BaseModel):
    RelayState: int  #
    ShNodeAlias: str  #
    CommandTimeUnixMs: int  #
    TypeAlias: Literal["gt.driver.booleanactuator.cmd"] = "gt.driver.booleanactuator.cmd"

    _validator_relay_state = predicate_validator("RelayState", property_format.is_bit)

    _validator_sh_node_alias = predicate_validator("ShNodeAlias", property_format.is_lrd_alias_format)

    _validator_command_time_unix_ms = predicate_validator("CommandTimeUnixMs", property_format.is_reasonable_unix_time_ms)

    def asdict(self):
        d = self.dict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())
