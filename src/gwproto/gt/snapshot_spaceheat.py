"""snapshot.spaceheat type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.errors import SchemaError
from gwproto.gt.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat
from gwproto.gt.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat_Maker
from gwproto.property_format import predicate_validator


class SnapshotSpaceheat(BaseModel):
    FromGNodeAlias: str  #
    FromGNodeInstanceId: str  #
    Snapshot: TelemetrySnapshotSpaceheat  #
    TypeAlias: Literal["snapshot.spaceheat"] = "snapshot.spaceheat"

    _validator_from_g_node_alias = predicate_validator("FromGNodeAlias", property_format.is_lrd_alias_format)

    _validator_from_g_node_instance_id = predicate_validator("FromGNodeInstanceId", property_format.is_uuid_canonical_textual)

    def asdict(self):
        d = self.dict()
        d["Snapshot"] = self.Snapshot.asdict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class SnapshotSpaceheat_Maker:
    type_alias = "snapshot.spaceheat"

    def __init__(self,
                    from_g_node_alias: str,
                    from_g_node_instance_id: str,
                    snapshot: TelemetrySnapshotSpaceheat):

        self.tuple = SnapshotSpaceheat(
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            Snapshot=snapshot,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: SnapshotSpaceheat) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> SnapshotSpaceheat:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> SnapshotSpaceheat:
        d2 = dict(d)
        if "TypeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeAlias")
        if "Snapshot" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Snapshot")
        if not isinstance(d2["Snapshot"], dict):
            raise SchemaError(f"d['Snapshot'] {d2['Snapshot']} must be a TelemetrySnapshotSpaceheat!")
        snapshot = TelemetrySnapshotSpaceheat_Maker.dict_to_tuple(d2["Snapshot"])
        d2["Snapshot"] = snapshot

        return SnapshotSpaceheat(
            TypeAlias=d2["TypeAlias"],
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            Snapshot=d2["Snapshot"],
            #
        )
