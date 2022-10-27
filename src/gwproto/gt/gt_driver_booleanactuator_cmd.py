"""gt.driver.booleanactuator.cmd type"""
import json
from typing import Literal

from pydantic import BaseModel

import gwproto.property_format as property_format
from gwproto.errors import SchemaError
from gwproto.property_format import predicate_validator


class GtDriverBooleanactuatorCmd(BaseModel):
    RelayState: int  #
    ShNodeAlias: str  #
    CommandTimeUnixMs: int  #
    TypeAlias: Literal["gt.driver.booleanactuator.cmd"] = "gt.driver.booleanactuator.cmd"

    _validator_relay_state = predicate_validator("RelayState", property_format.is_bit)

    _validator_sh_node_alias = predicate_validator("ShNodeAlias", property_format.is_lrd_alias_format)

    _validator_command_time_unix_ms = predicate_validator("CommandTimeUnixMs", property_format.is_reasonable_unix_time_ms)

    def asdict(self):
        d = self.dict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class GtDriverBooleanactuatorCmd_Maker:
    type_alias = "gt.driver.booleanactuator.cmd"

    def __init__(self,
                    relay_state: int,
                    sh_node_alias: str,
                    command_time_unix_ms: int):

        self.tuple = GtDriverBooleanactuatorCmd(
            RelayState=relay_state,
            ShNodeAlias=sh_node_alias,
            CommandTimeUnixMs=command_time_unix_ms,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtDriverBooleanactuatorCmd) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtDriverBooleanactuatorCmd:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtDriverBooleanactuatorCmd:
        d2 = dict(d)
        if "TypeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeAlias")

        return GtDriverBooleanactuatorCmd(
            TypeAlias=d2["TypeAlias"],
            RelayState=d2["RelayState"],
            ShNodeAlias=d2["ShNodeAlias"],
            CommandTimeUnixMs=d2["CommandTimeUnixMs"],
            #
        )
