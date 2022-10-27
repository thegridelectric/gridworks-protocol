"""gt.dispatch.boolean type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.errors import SchemaError
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


class GtDispatchBoolean_Maker:
    type_alias = "gt.dispatch.boolean"

    def __init__(self,
                    about_node_alias: str,
                    to_g_node_alias: str,
                    from_g_node_alias: str,
                    from_g_node_id: str,
                    relay_state: int,
                    send_time_unix_ms: int):

        self.tuple = GtDispatchBoolean(
            AboutNodeAlias=about_node_alias,
            ToGNodeAlias=to_g_node_alias,
            FromGNodeAlias=from_g_node_alias,
            FromGNodeId=from_g_node_id,
            RelayState=relay_state,
            SendTimeUnixMs=send_time_unix_ms,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtDispatchBoolean) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtDispatchBoolean:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtDispatchBoolean:
        d2 = dict(d)
        if "TypeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeAlias")

        return GtDispatchBoolean(
            TypeAlias=d2["TypeAlias"],
            AboutNodeAlias=d2["AboutNodeAlias"],
            ToGNodeAlias=d2["ToGNodeAlias"],
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeId=d2["FromGNodeId"],
            RelayState=d2["RelayState"],
            SendTimeUnixMs=d2["SendTimeUnixMs"],
            #
        )
