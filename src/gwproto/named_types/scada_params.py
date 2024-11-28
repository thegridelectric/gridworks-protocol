"""Type scada.params, version 001"""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

from gwproto.named_types.ha1_params import Ha1Params
from gwproto.property_format import (
    LeftRightDotStr,
    SpaceheatName,
    UTCMilliseconds,
    UUID4Str,
)


class ScadaParams(BaseModel):
    FromGNodeAlias: LeftRightDotStr
    FromName: SpaceheatName
    ToName: SpaceheatName
    UnixTimeMs: UTCMilliseconds
    MessageId: UUID4Str
    NewParams: Optional[Ha1Params] = None
    OldParams: Optional[Ha1Params] = None
    TypeName: Literal["scada.params"] = "scada.params"
    Version: Literal["001"] = "001"

    model_config = ConfigDict(extra="allow")
