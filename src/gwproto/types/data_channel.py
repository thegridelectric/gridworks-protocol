"""Type data.channel, version 000"""

from typing import Literal

from pydantic import BaseModel, Field

from gwproto.enums import TelemetryName
from gwproto.property_format import LeftRightDotStr


class DataChannel(BaseModel):
    """
    Data Channel.

    A data channel is a concept of some collection of readings that share all characteristics
    other than time.
    """

    DisplayName: str = Field(
        title="Display Name",
        description=(
            "This display name is the handle for the data channel. It is meant to be set by the "
            "person/people who will be analyzing time series data. It is only expected to be "
            "unique within the data channels associated to a specific Terminal Asset."
        ),
    )
    AboutName: LeftRightDotStr
    CapturedByName: LeftRightDotStr
    TelemetryName: TelemetryName
    TypeName: Literal["data.channel"] = "data.channel"
    Version: Literal["000"] = "000"
