"""Type electric.meter.component.gt, version 000"""

from typing import Literal, Optional, Self

from pydantic import Field, PositiveInt, model_validator

from gwproto.types import ComponentGt
from gwproto.types.egauge_io import EgaugeIo
from gwproto.types.telemetry_reporting_config import TelemetryReportingConfig


class ElectricMeterComponentGt(ComponentGt):
    ConfigList: list[TelemetryReportingConfig]
    ModbusHost: Optional[str] = None
    ModbusPort: Optional[PositiveInt] = None
    EgaugeIoList: list[EgaugeIo] = Field(
        default=[],
        title="Bijecton from EGauge4030 input to ConfigList output",
        description=(
            "This should be empty unless the MakeModel of the corresponding component attribute "
            "class is EGauge 4030. The channels that can be read from an EGauge 4030 are configurable "
            "by the person who installs the device. The information is encapsulated in a modbus "
            "map provided by eGauge as a csv from a device-specific API. The EGaugeIoList maps "
            "the data from this map to the data that the SCADA expects to see."
        ),
    )
    TypeName: Literal["electric.meter.component.gt"] = "electric.meter.component.gt"
    Version: Literal["000"] = "000"

    @model_validator(mode="after")
    def check_axioms(self) -> Self:
        if self.ModbusHost is not None and self.ModbusPort is None:
            raise ValueError("Axiom 1: ModbusHost None iff ModbusPort None! ")
        if len(self.EgaugeIoList) == 0:
            return self
        if self.ModbusHost is None:
            raise ValueError(
                "Axiom 2: If EgaugeIoList has non-zero length then ModbusHost must exist!"
            )
        if {x.OutputConfig for x in self.EgaugeIoList} != set(self.ConfigList):
            raise ValueError(
                "Axiom 2: If EgaugeIoList has non-zero length then the set of"
                "output configs must equal ConfigList as a set"
            )
        return self
