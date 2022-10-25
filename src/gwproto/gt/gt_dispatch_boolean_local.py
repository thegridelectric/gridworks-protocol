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


class GtDispatchBooleanLocal_Maker:
    type_alias = "gt.dispatch.boolean.local.100"

    def __init__(self,
                    send_time_unix_ms: int,
                    from_node_alias: str,
                    about_node_alias: str,
                    relay_state: int):

        self.tuple = GtDispatchBooleanLocal(
            SendTimeUnixMs=send_time_unix_ms,
            FromNodeAlias=from_node_alias,
            AboutNodeAlias=about_node_alias,
            RelayState=relay_state,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtDispatchBooleanLocal) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtDispatchBooleanLocal:
        try:
            d = json.loads(t)
        except TypeError:
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtDispatchBooleanLocal:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "SendTimeUnixMs" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing SendTimeUnixMs")
        if "FromNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing FromNodeAlias")
        if "AboutNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing AboutNodeAlias")
        if "RelayState" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing RelayState")

        return GtDispatchBooleanLocal(
            TypeAlias=new_d["TypeAlias"],
            SendTimeUnixMs=new_d["SendTimeUnixMs"],
            FromNodeAlias=new_d["FromNodeAlias"],
            AboutNodeAlias=new_d["AboutNodeAlias"],
            RelayState=new_d["RelayState"],
            #
        )
