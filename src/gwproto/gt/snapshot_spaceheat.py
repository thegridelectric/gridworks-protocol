"""snapshot.spaceheat.100 type"""
import json
from typing import Literal
from pydantic import BaseModel
import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator

from gwproto.gt import TelemetrySnapshotSpaceheat, TelemetrySnapshotSpaceheat_Maker


class SnapshotSpaceheat(BaseModel):
    FromGNodeAlias: str  #
    FromGNodeInstanceId: str  #
    Snapshot: TelemetrySnapshotSpaceheat  #
    TypeAlias: Literal["snapshot.spaceheat.100"] = "snapshot.spaceheat.100"

    _validator_from_g_node_alias = predicate_validator(
        "FromGNodeAlias", property_format.is_lrd_alias_format
    )
    _validator_from_g_node_instance_id = predicate_validator(
        "FromGNodeInstanceId", property_format.is_uuid_canonical_textual
    )

    def asdict(self):
        d = self.dict()
        d["Snapshot"] = self.Snapshot.asdict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class SnapshotSpaceheat_Maker:
    type_alias = "snapshot.spaceheat.100"

    def __init__(
        self,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        snapshot: TelemetrySnapshotSpaceheat,
    ):

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
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> SnapshotSpaceheat:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "FromGNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing FromGNodeInstanceId")
        if "Snapshot" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing Snapshot")
        if not isinstance(new_d["Snapshot"], dict):
            raise TypeError(
                f"d['Snapshot'] {new_d['Snapshot']} must be a TelemetrySnapshotSpaceheat!"
            )
        snapshot = TelemetrySnapshotSpaceheat_Maker.dict_to_tuple(new_d["Snapshot"])
        new_d["Snapshot"] = snapshot

        return SnapshotSpaceheat(
            TypeAlias=new_d["TypeAlias"],
            FromGNodeAlias=new_d["FromGNodeAlias"],
            FromGNodeInstanceId=new_d["FromGNodeInstanceId"],
            Snapshot=new_d["Snapshot"],
            #
        )
