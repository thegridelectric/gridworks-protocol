"""gt.dispatch.boolean.100 type"""
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
    TypeAlias: Literal["gt.dispatch.boolean.100"] = "gt.dispatch.boolean.100"

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
    type_alias = "gt.dispatch.boolean.100"

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
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtDispatchBoolean:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "AboutNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing AboutNodeAlias")
        if "ToGNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ToGNodeAlias")
        if "FromGNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing FromGNodeAlias")
        if "FromGNodeId" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing FromGNodeId")
        if "RelayState" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing RelayState")
        if "SendTimeUnixMs" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing SendTimeUnixMs")

        return GtDispatchBoolean(
            TypeAlias=new_d["TypeAlias"],
            AboutNodeAlias=new_d["AboutNodeAlias"],
            ToGNodeAlias=new_d["ToGNodeAlias"],
            FromGNodeAlias=new_d["FromGNodeAlias"],
            FromGNodeId=new_d["FromGNodeId"],
            RelayState=new_d["RelayState"],
            SendTimeUnixMs=new_d["SendTimeUnixMs"],
            #
        )
