"""gt.dispatch.boolean.local type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.errors import SchemaError
from gwproto.property_format import predicate_validator


class GtDispatchBooleanLocal(BaseModel):
    SendTimeUnixMs: int  #
    FromNodeAlias: str  #
    AboutNodeAlias: str  #
    RelayState: int  #
    TypeAlias: Literal["gt.dispatch.boolean.local"] = "gt.dispatch.boolean.local"

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
    type_alias = "gt.dispatch.boolean.local"

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
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtDispatchBooleanLocal:
        d2 = dict(d)
        if "TypeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeAlias")

        return GtDispatchBooleanLocal(
            TypeAlias=d2["TypeAlias"],
            SendTimeUnixMs=d2["SendTimeUnixMs"],
            FromNodeAlias=d2["FromNodeAlias"],
            AboutNodeAlias=d2["AboutNodeAlias"],
            RelayState=d2["RelayState"],
            #
        )
