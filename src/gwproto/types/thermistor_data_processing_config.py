"""Type thermistor.data.processing.config, version 000"""

from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict, PositiveInt

from gwproto.enums import MakeModel, ThermistorDataMethod
from gwproto.property_format import (
    SpaceheatName,
)


class ThermistorDataProcessingConfig(BaseModel):
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

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        d["ThermistorMakeModel"] = self.ThermistorMakeModel.value
        if "DataProcessingMethod" in d:
            d["DataProcessingMethod"] = d["DataProcessingMethod"].value
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "thermistor.data.processing.config"
