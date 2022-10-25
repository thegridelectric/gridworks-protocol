"""gt.dispatch.boolean type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator


class GtDispatchBoolean(BaseModel):
    AboutNodeAlias: str  #
    ToGNodeAlias: str  #
    FromGNodeAlias: str  #
    FromGNodeId: str  #
    RelayState: int  #
    SendTimeUnixMs: int  #
    TypeAlias: Literal["gt.dispatch.boolean"] = "gt.dispatch.boolean"

    _validator_about_node_alias = predicate_validator("AboutNodeAlias", property_format.is_lrd_alias_format)

    _validator_to_g_node_alias = predicate_validator("ToGNodeAlias", property_format.is_lrd_alias_format)

    _validator_from_g_node_alias = predicate_validator("FromGNodeAlias", property_format.is_lrd_alias_format)

    _validator_from_g_node_id = predicate_validator("FromGNodeId", property_format.is_uuid_canonical_textual)

    _validator_relay_state = predicate_validator("RelayState", property_format.is_bit)

    _validator_send_time_unix_ms = predicate_validator("SendTimeUnixMs", property_format.is_reasonable_unix_time_ms)

    def asdict(self):
        d = self.dict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())
