"""telemetry.snapshot.spaceheat type"""
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


class TelemetrySnapshotSpaceheat(BaseModel):
    AboutNodeAliasList: List[str]
    ValueList: List[int]
    TelemetryNameList: List[TelemetryName]
    ReportTimeUnixMs: int  #
    TypeAlias: Literal["telemetry.snapshot.spaceheat"] = "telemetry.snapshot.spaceheat"

    @validator("AboutNodeAliasList")
    def _validator_about_node_alias_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_lrd_alias_format(elt):
                raise ValueError(f"failure of predicate is_lrd_alias_format() on elt {elt} of AboutNodeAliasList")
        return v

    @validator("TelemetryNameList", pre=True)
    def _validator_telemetry_name_list(cls, v: Any) -> TelemetryName:
        if not isinstance(v, List):
            raise ValueError("TelemetryNameList must be a list!")
        enum_list = []
        for elt in v:
            enum_list.append(as_enum(elt, TelemetryName, TelemetryName.UNKNOWN))
        return enum_list

    _validator_report_time_unix_ms = predicate_validator("ReportTimeUnixMs", property_format.is_reasonable_unix_time_ms)

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
