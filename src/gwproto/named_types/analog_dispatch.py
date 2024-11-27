from typing import Literal, Optional

from pydantic import BaseModel, PositiveInt

from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UTCMilliseconds,
    UUID4Str,
)


class AnalogDispatch(BaseModel):
    FromGNodeAlias: Optional[LeftRightDotStr] = None
    FromName: SpaceheatName
    ToName: SpaceheatName
    AboutName: SpaceheatName
    Value: PositiveInt
    MessageId: UUID4Str
    UnixTimeMs: UTCMilliseconds
    TypeName: Literal["analog.dispatch"] = "analog.dispatch"
    Version: Literal["000"] = "000"
