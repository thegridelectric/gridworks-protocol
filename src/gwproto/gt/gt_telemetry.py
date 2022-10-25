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


class GtTelemetry_Maker:
    type_alias = "gt.telemetry.110"

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
            raise TypeError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise TypeError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtTelemetry:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing TypeAlias")
        if "ScadaReadTimeUnixMs" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing ScadaReadTimeUnixMs")
        if "Value" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing Value")
        if "NameGtEnumSymbol" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing NameGtEnumSymbol")
        if new_d["Name"] in TelemetryNameMap.gt_to_local_dict.keys():
            new_d["Name"] = TelemetryNameMap.gt_to_local(new_d["NameGtEnumSymbol"])
        else:
            new_d["Name"] = TelemetryName.UNKNOWN
        if "Exponent" not in new_d.keys():
            raise TypeError(f"dict {new_d} missing Exponent")

        return GtTelemetry(
            TypeAlias=new_d["TypeAlias"],
            ScadaReadTimeUnixMs=new_d["ScadaReadTimeUnixMs"],
            Value=new_d["Value"],
            Name=new_d["Name"],
            Exponent=new_d["Exponent"],
            #
        )
