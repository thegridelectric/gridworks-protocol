"""Type data.channel.gt, version 001"""

from typing import Literal, Optional

from pydantic import BaseModel, model_validator
from typing_extensions import Self

from gwproto.enums import TelemetryName
from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UTCSeconds,
    UUID4Str,
)


class DataChannelGt(BaseModel):
    """
    Data Channel.

    Core mechanism for identifying a stream of telemetry data. Everything but the DisplayName
    and StartS are meant to be immutable. The Name is meant to be unique per TerminalAssetAlias.
    """

    Name: SpaceheatName
    DisplayName: str
    AboutNodeName: SpaceheatName
    CapturedByNodeName: SpaceheatName
    TelemetryName: TelemetryName
    TerminalAssetAlias: LeftRightDotStr
    InPowerMetering: Optional[bool] = None
    StartS: Optional[UTCSeconds] = None
    Id: UUID4Str
    TypeName: Literal["data.channel.gt"] = "data.channel.gt"
    Version: Literal["001"] = "001"

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: Power Metering.
        If InPowerMetering is true then the TelemetryName must be PowerW
        """
        # Implement check for axiom 1"
        return self

    @classmethod
    def type_name_value(cls) -> str:
        return "data.channel.gt"
