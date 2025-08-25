"""Type data.channel.gt, version 001"""

from typing import Literal, Optional

from gw.named_types import GwBase
from pydantic import model_validator
from typing_extensions import Self

from gwproto.enums import TelemetryName
from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UTCSeconds,
    UUID4Str,
)


class DataChannelGt(GwBase):
    """ASL schema of record [data.channel.gt v001](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/data.channel.gt.001.yaml)"""

    name: SpaceheatName
    display_name: str
    about_node_name: SpaceheatName
    captured_by_node_name: SpaceheatName
    telemetry_name: TelemetryName
    terminal_asset_alias: LeftRightDotStr
    in_power_metering: Optional[bool] = None
    start_s: Optional[UTCSeconds] = None
    id: UUID4Str
    type_name: Literal["data.channel.gt"] = "data.channel.gt"
    version: Literal["001"] = "001"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Power Metering.
        If InPowerMetering is true then the TelemetryName must be PowerW
        """

        if self.in_power_metering and self.telemetry_name != TelemetryName.PowerW:
            raise ValueError(
                "Axiom 1 violated! If InPowerMetering is true then"
                f"the TelemetryName must be PowerW. Got  {self.telemetry_name}"
            )
        return self
