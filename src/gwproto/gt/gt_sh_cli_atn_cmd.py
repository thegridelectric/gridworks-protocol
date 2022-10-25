"""gt.sh.cli.atn.cmd type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator


class GtShCliAtnCmd(BaseModel):
    FromGNodeAlias: str  #
    SendSnapshot: bool  #
    FromGNodeId: str  #
    TypeAlias: Literal["gt.sh.cli.atn.cmd"] = "gt.sh.cli.atn.cmd"

    _validator_from_g_node_alias = predicate_validator("FromGNodeAlias", property_format.is_lrd_alias_format)

    _validator_from_g_node_id = predicate_validator("FromGNodeId", property_format.is_uuid_canonical_textual)

    def asdict(self):
        d = self.dict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())
