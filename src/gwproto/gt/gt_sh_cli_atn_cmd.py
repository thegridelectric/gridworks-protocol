"""gt.sh.cli.atn.cmd type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.errors import SchemaError
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


class GtShCliAtnCmd_Maker:
    type_alias = "gt.sh.cli.atn.cmd"

    def __init__(self,
                    from_g_node_alias: str,
                    send_snapshot: bool,
                    from_g_node_id: str):

        self.tuple = GtShCliAtnCmd(
            FromGNodeAlias=from_g_node_alias,
            SendSnapshot=send_snapshot,
            FromGNodeId=from_g_node_id,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShCliAtnCmd) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShCliAtnCmd:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtShCliAtnCmd:
        d2 = dict(d)
        if "TypeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeAlias")

        return GtShCliAtnCmd(
            TypeAlias=d2["TypeAlias"],
            FromGNodeAlias=d2["FromGNodeAlias"],
            SendSnapshot=d2["SendSnapshot"],
            FromGNodeId=d2["FromGNodeId"],
            #
        )
