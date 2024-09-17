"""Type gt.sh.cli.atn.cmd, version 110"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import (
    LeftRightDotStr,
    UUID4Str,
)


class GtShCliAtnCmd(BaseModel):
    FromGNodeAlias: LeftRightDotStr
    SendSnapshot: bool
    FromGNodeId: UUID4Str
    TypeName: Literal["gt.sh.cli.atn.cmd"] = "gt.sh.cli.atn.cmd"
    Version: Literal["110"] = "110"

    @classmethod
    def type_name_value(cls) -> str:
        return "gt.sh.cli.atn.cmd"
