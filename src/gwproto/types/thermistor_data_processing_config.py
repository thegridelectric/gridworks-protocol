"""Type thermistor.data.processing.config, version 000"""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, PositiveInt

from gwproto.enums import MakeModel, ThermistorDataMethod
from gwproto.property_format import (
    SpaceheatName,
)


class ThermistorDataProcessingConfig(BaseModel):
    """
    How does polled raw data get turned into a captured temperature reading? This config type
    provides that information.
    """

    ChannelName: SpaceheatName
    TerminalBlockIdx: PositiveInt
    ThermistorMakeModel: MakeModel
    DataProcessingMethod: Optional[ThermistorDataMethod] = None
    DataProcessingDescription: Optional[str] = None
    TypeName: Literal["thermistor.data.processing.config"] = (
        "thermistor.data.processing.config"
    )
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @classmethod
    def type_name_value(cls) -> str:
        return "thermistor.data.processing.config"
