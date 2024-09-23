"""Type telemetry.reporting.config, version 000"""

from typing import Literal, Optional, Self

from pydantic import BaseModel, PositiveInt, model_validator

from gwproto.enums import TelemetryName, Unit
from gwproto.property_format import SpaceheatName


class TelemetryReportingConfig(BaseModel):
    TelemetryName: TelemetryName
    AboutNodeName: SpaceheatName
    ReportOnChange: bool
    SamplePeriodS: int
    Exponent: int
    Unit: Unit
    AsyncReportThreshold: Optional[float] = None
    NameplateMaxValue: Optional[PositiveInt] = None
    TypeName: Literal["telemetry.reporting.config"] = "telemetry.reporting.config"
    Version: Literal["001"] = "001"

    def __hash__(self) -> int:
        return hash((type(self), *self.__dict__.values()))

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Async reporting consistency.
        If AsyncReportThreshold exists, so does NameplateMaxValue
        """
        if self.AsyncReportThreshold is not None and self.NameplateMaxValue is None:
            raise ValueError(
                "Violates Axiom 1: If AsyncReportThreshold exists, so does NameplateMaxValue"
            )
        return self
