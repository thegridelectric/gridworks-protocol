"""snapshot.spaceheat.100 type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.gt.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat
from gwproto.property_format import predicate_validator


class SnapshotSpaceheat(BaseModel):
    FromGNodeAlias: str  #
    FromGNodeInstanceId: str  #
    Snapshot: TelemetrySnapshotSpaceheat  #
    TypeAlias: Literal["snapshot.spaceheat.100"] = "snapshot.spaceheat.100"

    _validator_from_g_node_alias = predicate_validator("FromGNodeAlias", property_format.is_lrd_alias_format)

    _validator_from_g_node_instance_id = predicate_validator("FromGNodeInstanceId", property_format.is_uuid_canonical_textual)

    def asdict(self):
        d = self.dict()
        d["Snapshot"] = self.Snapshot.asdict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())
