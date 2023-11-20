from pydantic import BaseModel
from pydantic import Extra
from pydantic import validator

from gwproto.enums import TelemetryName as EnumTelemetryName
from gwproto.enums import Unit as EnumUnit
from gwproto.types.simple_temp_sensor_cac_gt import TelemetryNameMap
from gwproto.types.simple_temp_sensor_cac_gt import UnitMap
from gwproto.utils import snake_to_camel


class MakerAPIAttributeGt(BaseModel):
    attribute_name: str
    node_name: str
    telemetry_name_gt_enum_symbol: str = "c89d0ba1"
    temp_unit_gt_enum_symbol: str = "ec14bd47"
    exponent: int = 3
    enabled: bool = True
    report_missing: bool = True
    report_parse_error: bool = True

    @property
    def telemetry_name(self) -> EnumTelemetryName:
        return TelemetryNameMap.type_to_local(
            self.telemetry_name_gt_enum_symbol,
        )

    @property
    def unit(self) -> EnumUnit:
        return UnitMap.type_to_local(
            self.temp_unit_gt_enum_symbol,
        )

    class Config:
        extra = Extra.allow
        alias_generator = snake_to_camel
        allow_population_by_field_name = True

    @validator("telemetry_name_gt_enum_symbol")
    def _check_telemetry_name_symbol(cls, v: str) -> str:
        if v not in TelemetryNameMap.type_to_versioned_enum_dict:
            v = TelemetryNameMap.local_to_type(EnumTelemetryName.default())
        return v


class HubitatPollerGt(BaseModel):
    hubitat_component_id: str
    device_id: int
    attributes: list[MakerAPIAttributeGt] = []
    enabled: bool = True

    class Config:
        extra = Extra.allow
        alias_generator = snake_to_camel
        allow_population_by_field_name = True
