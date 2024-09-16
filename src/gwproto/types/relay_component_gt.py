"""Type relay.component.gt, version 000"""

from typing import Literal, Optional

from gwproto.types import ComponentGt


class RelayComponentGt(ComponentGt):
    Gpio: Optional[int] = None
    NormallyOpen: bool
    TypeName: Literal["relay.component.gt"] = "relay.component.gt"
