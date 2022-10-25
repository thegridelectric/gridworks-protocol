"""gt.sh.multipurpose.telemetry.status.100 type"""
import json
from typing import Any
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gwproto.property_format as property_format
from gwproto.enums import TelemetryName
from gwproto.enums import TelemetryNameMap
from gwproto.message import as_enum
from gwproto.property_format import predicate_validator


class GtShMultipurposeTelemetryStatus(BaseModel):
    AboutNodeAlias: str  #
    TelemetryName: TelemetryName  #
    ValueList: List[int]
    ReadTimeUnixMsList: List[int]
    SensorNodeAlias: str  #
    TypeAlias: Literal["gt.sh.multipurpose.telemetry.status.100"] = "gt.sh.multipurpose.telemetry.status.100"

    _validator_about_node_alias = predicate_validator("AboutNodeAlias", property_format.is_lrd_alias_format)

    @validator("TelemetryName", pre=True)
    def _validator_telemetry_name(cls, v: Any) -> TelemetryName:
        return as_enum(v, TelemetryName, TelemetryName.UNKNOWN)

    @validator("ReadTimeUnixMsList")
    def _validator_read_time_unix_ms_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_reasonable_unix_time_ms(elt):
                raise ValueError(f"failure of predicate is_reasonable_unix_time_ms() on elt {elt} of ReadTimeUnixMsList")
        return v

    def asdict(self):
        d = self.dict()
        del d["TelemetryName"]
        d["TelemetryNameGtEnumSymbol"] = TelemetryNameMap.local_to_gt(self.TelemetryName)
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class GtShMultipurposeTelemetryStatus_Maker:
    type_alias = "gt.sh.multipurpose.telemetry.status.100"

    def __init__(self,
                    about_node_alias: str,
                    telemetry_name: TelemetryName,
                    value_list: List[int],
                    read_time_unix_ms_list: List[int],
                    sensor_node_alias: str):

        self.tuple = GtShMultipurposeTelemetryStatus(
            AboutNodeAlias=about_node_alias,
            TelemetryName=telemetry_name,
            ValueList=value_list,
            ReadTimeUnixMsList=read_time_unix_ms_list,
            SensorNodeAlias=sensor_node_alias,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShMultipurposeTelemetryStatus) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShMultipurposeTelemetryStatus:
        try:
            d = json.loads(t)
        except TypeError:
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtShMultipurposeTelemetryStatus:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "AboutNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing AboutNodeAlias")
        if "TelemetryNameGtEnumSymbol" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TelemetryNameGtEnumSymbol")
        if new_d["TelemetryName"] in TelemetryNameMap.gt_to_local_dict.keys():
            new_d["TelemetryName"] = TelemetryNameMap.gt_to_local(new_d["TelemetryNameGtEnumSymbol"])
        else:
            new_d["TelemetryName"] = TelemetryName.UNKNOWN
        if "ValueList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ValueList")
        if "ReadTimeUnixMsList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ReadTimeUnixMsList")
        if "SensorNodeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing SensorNodeAlias")

        return GtShMultipurposeTelemetryStatus(
            TypeAlias=new_d["TypeAlias"],
            AboutNodeAlias=new_d["AboutNodeAlias"],
            TelemetryName=new_d["TelemetryName"],
            ValueList=new_d["ValueList"],
            ReadTimeUnixMsList=new_d["ReadTimeUnixMsList"],
            SensorNodeAlias=new_d["SensorNodeAlias"],
            #
        )
