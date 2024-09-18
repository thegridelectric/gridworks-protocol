"""Type gt.sh.cli.atn.cmd, version 110"""

from typing import Any, Literal

from pydantic import BaseModel

from gwproto.property_format import (
    LeftRightDotStr,
    UUID4Str,
)


class GtShCliAtnCmd(BaseModel):
    """
    AtomicTNode CLI Command.

    This is a generic type mechanism for a crude command line interface on a SCADA, brokered
    by the AtomicTNode.
    """

    FromGNodeAlias: LeftRightDotStr
    SendSnapshot: bool
    FromGNodeId: UUID4Str
    TypeName: Literal["gt.sh.cli.atn.cmd"] = "gt.sh.cli.atn.cmd"
    Version: Literal["110"] = "110"

    def model_dump(self, **kwargs: dict[str, Any]) -> dict:
        d = super().model_dump(**kwargs)
        return d

    @classmethod
    def type_name_value(cls) -> str:
        return "gt.sh.cli.atn.cmd"
