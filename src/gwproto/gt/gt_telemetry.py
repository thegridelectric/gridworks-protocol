"""gt.telemetry type"""
import json
from typing import Any
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gwproto.property_format as property_format
from gwproto.enums import TelemetryName
from gwproto.enums import TelemetryNameMap
from gwproto.errors import SchemaError
from gwproto.message import as_enum
from gwproto.property_format import predicate_validator


class GtTelemetry(BaseModel):
    ScadaReadTimeUnixMs: int  #
    Value: int  #
    Name: TelemetryName  #
    Exponent: int  #
    TypeAlias: Literal["gt.telemetry"] = "gt.telemetry"

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


class GtTelemetry_Maker:
    type_alias = "gt.telemetry"

    def __init__(self,
                    scada_read_time_unix_ms: int,
                    value: int,
                    name: TelemetryName,
                    exponent: int):

        self.tuple = GtTelemetry(
            ScadaReadTimeUnixMs=scada_read_time_unix_ms,
            Value=value,
            Name=name,
            Exponent=exponent,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtTelemetry) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtTelemetry:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtTelemetry:
        d2 = dict(d)
        if "TypeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeAlias")
        if "NameGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing NameGtEnumSymbol")
        if d2["NameGtEnumSymbol"] in TelemetryNameMap.gt_to_local_dict.keys():
            d2["Name"] = TelemetryNameMap.gt_to_local(d2["NameGtEnumSymbol"])
        else:
            d2["Name"] = TelemetryName.UNKNOWN

        return GtTelemetry(
            TypeAlias=d2["TypeAlias"],
            ScadaReadTimeUnixMs=d2["ScadaReadTimeUnixMs"],
            Value=d2["Value"],
            Name=d2["Name"],
            Exponent=d2["Exponent"],
            #
        )
