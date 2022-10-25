"""gt.sh.booleanactuator.cmd.status type"""
import json
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator


class GtShBooleanactuatorCmdStatus(BaseModel):
    ShNodeAlias: str  #
    RelayStateCommandList: List[int]
    CommandTimeUnixMsList: List[int]
    TypeAlias: Literal["gt.sh.booleanactuator.cmd.status"] = "gt.sh.booleanactuator.cmd.status"

    _validator_sh_node_alias = predicate_validator("ShNodeAlias", property_format.is_lrd_alias_format)

    @validator("RelayStateCommandList")
    def _validator_relay_state_command_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_bit(elt):
                raise ValueError(f"failure of predicate is_bit() on elt {elt} of RelayStateCommandList")
        return v

    @validator("CommandTimeUnixMsList")
    def _validator_command_time_unix_ms_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_reasonable_unix_time_ms(elt):
                raise ValueError(f"failure of predicate is_reasonable_unix_time_ms() on elt {elt} of CommandTimeUnixMsList")
        return v

    def asdict(self):
        d = self.dict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())
