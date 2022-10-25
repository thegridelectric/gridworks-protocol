"""gt.sh.booleanactuator.cmd.status.100 type"""
import json
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator


class GtShBooleanactuatorCmdStatus(BaseModel):
    ShNodeAlias: str  #
    RelayStateCommandList: List[int]
    CommandTimeUnixMsList: List[int]
    TypeAlias: Literal["gt.sh.booleanactuator.cmd.status.100"] = "gt.sh.booleanactuator.cmd.status.100"

    _validator_sh_node_alias = predicate_validator("ShNodeAlias", property_format.is_lrd_alias_format)

    @validator("RelayStateCommandList")
    def _validator_relay_state_command_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_bit(elt):
                raise ValueError(f"failure of predicate is_lrd_alias_format() on elt {elt} of RelayStateCommandList")
        return v

    @validator("CommandTimeUnixMsList")
    def _validator_command_time_unix_ms_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_reasonable_unix_time_ms(elt):
                raise ValueError(f"failure of predicate is_lrd_alias_format() on elt {elt} of CommandTimeUnixMsList")
        return v

    def asdict(self):
        d = self.dict()
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class GtShBooleanactuatorCmdStatus_Maker:
    type_alias = "gt.sh.booleanactuator.cmd.status.100"

    def __init__(self,
                    sh_node_alias: str,
                    relay_state_command_list: List[int],
                    command_time_unix_ms_list: List[int]):

        self.tuple = GtShBooleanactuatorCmdStatus(
            ShNodeAlias=sh_node_alias,
            RelayStateCommandList=relay_state_command_list,
            CommandTimeUnixMsList=command_time_unix_ms_list,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShBooleanactuatorCmdStatus) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShBooleanactuatorCmdStatus:
        try:
            d = json.loads(t)
        except TypeError:
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtShBooleanactuatorCmdStatus:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "ShNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ShNodeAlias")
        if "RelayStateCommandList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing RelayStateCommandList")
        if "CommandTimeUnixMsList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing CommandTimeUnixMsList")

        return GtShBooleanactuatorCmdStatus(
            TypeAlias=new_d["TypeAlias"],
            ShNodeAlias=new_d["ShNodeAlias"],
            RelayStateCommandList=new_d["RelayStateCommandList"],
            CommandTimeUnixMsList=new_d["CommandTimeUnixMsList"],
            #
        )
