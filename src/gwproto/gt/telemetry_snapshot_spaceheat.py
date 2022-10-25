"""telemetry.snapshot.spaceheat.100 type"""
import json
from typing import Literal, List
from pydantic import BaseModel, validator

import gwproto.property_format as property_format
from gwproto.property_format import predicate_validator
from gwproto.enums import (
    TelemetryName,
    TelemetryNameMap,
)


class TelemetrySnapshotSpaceheat(BaseModel):
    AboutNodeAliasList: List[str]
    ValueList: List[int]
    TelemetryNameList: List[TelemetryName]
    ReportTimeUnixMs: int  #
    TypeAlias: Literal["telemetry.snapshot.spaceheat.100"] = "telemetry.snapshot.spaceheat.100"

    @validator("AboutNodeAliasList")
    def _validator_about_node_alias_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_lrd_alias_format(elt):
                raise ValueError(
                    f"failure of predicate is_lrd_alias_format() on elt {elt} of AboutNodeAliasList"
                )
        return v

    _validator_report_time_unix_ms = predicate_validator(
        "ReportTimeUnixMs", property_format.is_reasonable_unix_time_ms
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


class TelemetrySnapshotSpaceheat_Maker:
    type_alias = "telemetry.snapshot.spaceheat.100"

    def __init__(
        self,
        about_node_alias_list: List[str],
        value_list: List[int],
        telemetry_name_list: List[TelemetryName],
        report_time_unix_ms: int,
    ):

        self.tuple = TelemetrySnapshotSpaceheat(
            AboutNodeAliasList=about_node_alias_list,
            ValueList=value_list,
            TelemetryNameList=telemetry_name_list,
            ReportTimeUnixMs=report_time_unix_ms,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: TelemetrySnapshotSpaceheat) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> TelemetrySnapshotSpaceheat:
        try:
            d = json.loads(t)
        except TypeError:
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> TelemetrySnapshotSpaceheat:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "AboutNodeAliasList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing AboutNodeAliasList")
        if "ValueList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ValueList")
        if "TelemetryNameList" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TelemetryNameList")
        telemetry_name_list = []
        for elt in new_d["TelemetryNameList"]:
            telemetry_name_list.append(TelemetryNameMap.gt_to_local(elt))
        new_d["TelemetryNameList"] = telemetry_name_list
        if "ReportTimeUnixMs" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ReportTimeUnixMs")

        return TelemetrySnapshotSpaceheat(
            TypeAlias=new_d["TypeAlias"],
            AboutNodeAliasList=new_d["AboutNodeAliasList"],
            ValueList=new_d["ValueList"],
            TelemetryNameList=new_d["TelemetryNameList"],
            ReportTimeUnixMs=new_d["ReportTimeUnixMs"],
            #
        )
