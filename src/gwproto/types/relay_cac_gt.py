"""Type relay.cac.gt, version 000"""

from typing import Literal

from gwproto.types import ComponentAttributeClassGt


class RelayCacGt(ComponentAttributeClassGt):
    TypicalResponseTimeMs: int
    TypeName: Literal["relay.cac.gt"] = "relay.cac.gt"
