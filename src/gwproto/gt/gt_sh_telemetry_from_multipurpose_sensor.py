"""gt.sh.telemetry.from.multipurpose.sensor.100 type"""
import json
from typing import Literal, List
from pydantic import BaseModel, validator
from gwproto.property_format import predicate_validator
import gwproto.property_format as property_format

from gwproto.enums import (
    TelemetryName,
    TelemetryNameMap,
)


class GtShTelemetryFromMultipurposeSensor(BaseModel):
    AboutNodeAliasList: List[str]
    ValueList: List[int]
    ScadaReadTimeUnixMs: int  #
    TelemetryNameList: List[TelemetryName]
    TypeAlias: Literal[
        "gt.sh.telemetry.from.multipurpose.sensor.100"
    ] = "gt.sh.telemetry.from.multipurpose.sensor.100"

    @validator("AboutNodeAliasList")
    def _validator_about_node_alias_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_lrd_alias_format(elt):
                raise ValueError(
                    f"failure of predicate is_lrd_alias_format() on elt {elt} of AboutNodeAliasList"
                )
        return v

    _validator_scada_read_time_unix_ms = predicate_validator(
        "ScadaReadTimeUnixMs", property_format.is_reasonable_unix_time_ms
    )

    def asdict(self):
        d = self.dict()
        del d["TelemetryNameList"]
        telemetry_name_list = []
        for elt in self.TelemetryNameList:
            telemetry_name_list.append(TelemetryNameMap.local_to_gt(elt))
        d["TelemetryNameList"] = telemetry_name_list
        return d

    def as_type(self):
        return json.dumps(self.asdict())


class GtShTelemetryFromMultipurposeSensor_Maker:
    type_alias = "gt.sh.telemetry.from.multipurpose.sensor.100"

    def __init__(
        self,
        about_node_alias_list: List[str],
        value_list: List[int],
        scada_read_time_unix_ms: int,
        telemetry_name_list: List[TelemetryName],
    ):

        self.tuple = GtShTelemetryFromMultipurposeSensor(
            AboutNodeAliasList=about_node_alias_list,
            ValueList=value_list,
            ScadaReadTimeUnixMs=scada_read_time_unix_ms,
            TelemetryNameList=telemetry_name_list,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtShTelemetryFromMultipurposeSensor) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShTelemetryFromMultipurposeSensor:
        try:
            d = json.loads(t)
        except TypeError:
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtShTelemetryFromMultipurposeSensor:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "AboutNodeAliasList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing AboutNodeAliasList")
        if "ValueList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ValueList")
        if "ScadaReadTimeUnixMs" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ScadaReadTimeUnixMs")
        if "TelemetryNameList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TelemetryNameList")
        telemetry_name_list = []
        for elt in new_d["TelemetryNameList"]:
            telemetry_name_list.append(TelemetryNameMap.gt_to_local(elt))
        new_d["TelemetryNameList"] = telemetry_name_list

        return GtShTelemetryFromMultipurposeSensor(
            TypeAlias=new_d["TypeAlias"],
            AboutNodeAliasList=new_d["AboutNodeAliasList"],
            ValueList=new_d["ValueList"],
            ScadaReadTimeUnixMs=new_d["ScadaReadTimeUnixMs"],
            TelemetryNameList=new_d["TelemetryNameList"],
            #
        )
