"""gt.sh.simple.telemetry.status.100 type"""
import json
from typing import Literal, List
from pydantic import BaseModel, validator

import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator
from gwproto.enums import (
    TelemetryName,
    TelemetryNameMap,
)


class GtShSimpleTelemetryStatus(BaseModel):
    ValueList: List[int]
    ReadTimeUnixMsList: List[int]
    TelemetryName: TelemetryName  #
    ShNodeAlias: str  #
    TypeAlias: Literal["gt.sh.simple.telemetry.status.100"] = "gt.sh.simple.telemetry.status.100"

    @validator("ReadTimeUnixMsList")
    def _validator_read_time_unix_ms_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_reasonable_unix_time_ms(elt):
                raise ValueError(
                    f"failure of predicate is_lrd_alias_format() on elt {elt} of ReadTimeUnixMsList"
                )
        return v

    _validator_sh_node_alias = predicate_validator(
        "ShNodeAlias", property_format.is_lrd_alias_format
    )

    def asdict(self):
        d = self.dict()
        del d["TelemetryName"]
        d["TelemetryNameGtEnumSymbol"] = TelemetryNameMap.local_to_gt(self.TelemetryName)
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class GtShSimpleTelemetryStatus_Maker:
    type_alias = "gt.sh.simple.telemetry.status.100"

    def __init__(
        self,
        value_list: List[int],
        read_time_unix_ms_list: List[int],
        telemetry_name: TelemetryName,
        sh_node_alias: str,
    ):

        self.tuple = GtShSimpleTelemetryStatus(
            ValueList=value_list,
            ReadTimeUnixMsList=read_time_unix_ms_list,
            TelemetryName=telemetry_name,
            ShNodeAlias=sh_node_alias,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShSimpleTelemetryStatus) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShSimpleTelemetryStatus:
        try:
            d = json.loads(t)
        except TypeError:
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtShSimpleTelemetryStatus:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "ValueList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ValueList")
        if "ReadTimeUnixMsList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ReadTimeUnixMsList")
        if "TelemetryNameGtEnumSymbol" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TelemetryNameGtEnumSymbol")
        if new_d["TelemetryName"] in TelemetryNameMap.gt_to_local_dict.keys():
            new_d["TelemetryName"] = TelemetryNameMap.gt_to_local(
                new_d["TelemetryNameGtEnumSymbol"]
            )
        else:
            new_d["TelemetryName"] = TelemetryName.UNKNOWN
        if "ShNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ShNodeAlias")

        return GtShSimpleTelemetryStatus(
            TypeAlias=new_d["TypeAlias"],
            ValueList=new_d["ValueList"],
            ReadTimeUnixMsList=new_d["ReadTimeUnixMsList"],
            TelemetryName=new_d["TelemetryName"],
            ShNodeAlias=new_d["ShNodeAlias"],
            #
        )
