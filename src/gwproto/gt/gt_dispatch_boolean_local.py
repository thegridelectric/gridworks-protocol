"""gt.dispatch.boolean.local.100 type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator


class GtDispatchBooleanLocal(BaseModel):
    SendTimeUnixMs: int  #
    FromNodeAlias: str  #
    AboutNodeAlias: str  #
    RelayState: int  #
    TypeAlias: Literal["gt.dispatch.boolean.local.100"] = "gt.dispatch.boolean.local.100"

    _validator_send_time_unix_ms = predicate_validator("SendTimeUnixMs", property_format.is_reasonable_unix_time_ms)

    _validator_from_node_alias = predicate_validator("FromNodeAlias", property_format.is_lrd_alias_format)

    _validator_about_node_alias = predicate_validator("AboutNodeAlias", property_format.is_lrd_alias_format)

    _validator_relay_state = predicate_validator("RelayState", property_format.is_bit)

    def asdict(self):
        d = self.dict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())
