"""gt.sh.simple.telemetry.status type"""
import json
from typing import Any
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gwproto.property_format as property_format
from gwproto.enums import TelemetryName
from gwproto.enums import TelemetryNameMap
from gwproto.errors import SchemaError
from gwproto.message import as_enum
from gwproto.property_format import predicate_validator


class GtShSimpleTelemetryStatus(BaseModel):
    ValueList: List[int]
    ReadTimeUnixMsList: List[int]
    TelemetryName: TelemetryName  #
    ShNodeAlias: str  #
    TypeAlias: Literal["gt.sh.simple.telemetry.status"] = "gt.sh.simple.telemetry.status"

    @validator("ReadTimeUnixMsList")
    def _validator_read_time_unix_ms_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_reasonable_unix_time_ms(elt):
                raise ValueError(f"failure of predicate is_reasonable_unix_time_ms() on elt {elt} of ReadTimeUnixMsList")
        return v

    @validator("TelemetryName", pre=True)
    def _validator_telemetry_name(cls, v: Any) -> TelemetryName:
        return as_enum(v, TelemetryName, TelemetryName.UNKNOWN)

    _validator_sh_node_alias = predicate_validator("ShNodeAlias", property_format.is_lrd_alias_format)

    def asdict(self):
        d = self.dict()
        del d["TelemetryName"]
        d["TelemetryNameGtEnumSymbol"] = TelemetryNameMap.local_to_gt(self.TelemetryName)
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class GtShSimpleTelemetryStatus_Maker:
    type_alias = "gt.sh.simple.telemetry.status"

    def __init__(self,
                    value_list: List[int],
                    read_time_unix_ms_list: List[int],
                    telemetry_name: TelemetryName,
                    sh_node_alias: str):

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
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtShSimpleTelemetryStatus:
        d2 = dict(d)
        if "TypeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeAlias")
        if "TelemetryNameGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TelemetryNameGtEnumSymbol")
        if d2["TelemetryNameGtEnumSymbol"] in TelemetryNameMap.gt_to_local_dict.keys():
            d2["TelemetryName"] = TelemetryNameMap.gt_to_local(d2["TelemetryNameGtEnumSymbol"])
        else:
            d2["TelemetryName"] = TelemetryName.UNKNOWN

        return GtShSimpleTelemetryStatus(
            TypeAlias=d2["TypeAlias"],
            ValueList=d2["ValueList"],
            ReadTimeUnixMsList=d2["ReadTimeUnixMsList"],
            TelemetryName=d2["TelemetryName"],
            ShNodeAlias=d2["ShNodeAlias"],
            #
        )
