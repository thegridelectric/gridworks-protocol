"""Type data.channel.gt, version 001"""

from typing import Any, Literal, Optional

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

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["TelemetryName"] = self.TelemetryName.value
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "data.channel.gt"
