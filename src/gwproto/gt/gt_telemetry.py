"""gt.telemetry.110 type"""
import json
from typing import Any
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gwproto.property_format as property_format
from gwproto.enums import TelemetryName
from gwproto.enums import TelemetryNameMap
from gwproto.message import as_enum
from gwproto.property_format import predicate_validator


class GtTelemetry(BaseModel):
    ScadaReadTimeUnixMs: int  #
    Value: int  #
    Name: TelemetryName  #
    Exponent: int  #
    TypeAlias: Literal["gt.telemetry.110"] = "gt.telemetry.110"

    _validator_scada_read_time_unix_ms = predicate_validator("ScadaReadTimeUnixMs", property_format.is_reasonable_unix_time_ms)

    @validator("Name", pre=True)
    def _validator_name(cls, v: Any) -> TelemetryName:
        return as_enum(v, TelemetryName, TelemetryName.UNKNOWN)

    def asdict(self):
        d = self.dict()
        del d["Name"]
        d["NameGtEnumSymbol"] = TelemetryNameMap.local_to_gt(self.Name)
        return d

    def as_type(self):
        return json.dumps(self.asdict())
