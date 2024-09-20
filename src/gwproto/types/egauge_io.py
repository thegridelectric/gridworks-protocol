"""Type egauge.io, version 000"""

from typing import Literal

from pydantic import BaseModel, Field

from gwproto.types.egauge_register_config import EgaugeRegisterConfig
from gwproto.types.telemetry_reporting_config import TelemetryReportingConfig


class EgaugeIo(BaseModel):
    """
    Used for an eGauge meter's component information in a hardware layout.

    When the component associated to a PowerMeter ShNode has MakeModel EGAUGE__4030, there is
    a significant amount of configuration required to specify both what is read from the eGauge
    (input) and what is then sent up to the SCADA (output). This type handles that information.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/egauge-io.html)
    """

    InputConfig: EgaugeRegisterConfig = Field(
        title="Input config for one channel of data for a specific eGauge meter",
        description=(
            "This is the data available from the modbus csv map provided by eGauge for this component, "
            "for example http://egauge14875.egaug.es/6001C/settings.html for a eGauge device "
            "with ID 14875"
        ),
    )
    OutputConfig: TelemetryReportingConfig = Field(
        title="Output config for the same channel ",
        description=(
            "This is the data as the Scada proactor expects to consume it from the power meter "
            "driver proactor."
        ),
    )
    TypeName: Literal["egauge.io"] = "egauge.io"
    Version: Literal["000"] = "000"
