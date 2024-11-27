"""Type scada.params, version 000"""

from typing import Literal

from pydantic import BaseModel, ConfigDict

from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UTCMilliseconds,
    UUID4Str,
)


class ScadaParams(BaseModel):
    """ """

    FromGNodeAlias: LeftRightDotStr
    FromName: SpaceheatName
    ToName: SpaceheatName
    UnixTimeMs: UTCMilliseconds
    MessageId: UUID4Str
    TypeName: Literal["scada.params"] = "scada.params"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")
