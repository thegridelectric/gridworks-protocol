"""Type egauge.io, version 001"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import (
    SpaceheatName,
)
from gwproto.types.egauge_register_config import EgaugeRegisterConfig


class EgaugeIo(BaseModel):
    """
    Used for an eGauge meter's component information in a hardware layout.

    When the component associated to a PowerMeter ShNode has MakeModel EGAUGE__4030, there is
    a significant amount of configuration required to specify both what is read from the eGauge
    (input) and what is then sent up to the SCADA (output). This type handles that information.

    [More info](https://gridworks-protocol.readthedocs.io/en/latest/egauge-io.html)
    """

    ChannelName: SpaceheatName
    InputConfig: EgaugeRegisterConfig
    TypeName: Literal["egauge.io"] = "egauge.io"
    Version: Literal["001"] = "001"

    @classmethod
    def type_name_value(cls) -> str:
        return "egauge.io"
