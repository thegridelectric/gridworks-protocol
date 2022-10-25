"""gt.sh.multipurpose.telemetry.status type"""
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
    TypeAlias: Literal["gt.sh.multipurpose.telemetry.status"] = "gt.sh.multipurpose.telemetry.status"

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
