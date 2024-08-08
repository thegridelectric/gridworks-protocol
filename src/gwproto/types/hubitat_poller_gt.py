from gw.utils import snake_to_pascal
from pydantic import BaseModel, field_validator

from gwproto.enums import TelemetryName, Unit


class MakerAPIAttributeGt(BaseModel):
    attribute_name: str
    node_name: str
    telemetry_name_gt_enum_symbol: str = "c89d0ba1"
    unit_gt_enum_symbol: str = "ec14bd47"
    exponent: int = 3
    interpret_as_number: bool = True
    enabled: bool = True
    web_poll_enabled: bool = True
    web_listen_enabled: bool = True
    report_missing: bool = True
    report_parse_error: bool = True

    @property
    def telemetry_name(self) -> TelemetryName:
        value = TelemetryName.symbol_to_value(
            self.telemetry_name_gt_enum_symbol,
        )
        return TelemetryName(value)

    @property
    def unit(self) -> Unit:
        value = Unit.symbol_to_value(
            self.unit_gt_enum_symbol,
        )
        return Unit(value)

    class Config:
        extra = "allow"
        alias_generator = snake_to_pascal
        populate_by_name = True

    @field_validator("telemetry_name_gt_enum_symbol")
    @classmethod
    def _check_telemetry_name_symbol(cls, v: str) -> str:
        if v not in TelemetryName.symbols():
            v = TelemetryName.value_to_symbol(TelemetryName.default())
        return v


class HubitatPollerGt(BaseModel):
    hubitat_component_id: str
    device_id: int
    attributes: list[MakerAPIAttributeGt] = []
    enabled: bool = True
    web_listen_enabled: bool = True
    poll_period_seconds: float = 60

    class Config:
        extra = "allow"
        alias_generator = snake_to_pascal
        populate_by_name = True
