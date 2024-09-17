"""Type power.watts, version 000"""

from typing import Literal

from pydantic import BaseModel

from gwproto.property_format import ReallyAnInt


class PowerWatts(BaseModel):
    """
    Real-time power of TerminalAsset in Watts.

    Used by a SCADA -> Atn or Atn -> AggregatedTNode to report real-time power of their TerminalAsset.
    Positive number means WITHDRAWAL from the grid - so generating electricity creates a negative
    number. This message is considered worse than useless to send after the first attempt, and
    does not require an ack. Shares the same purpose as gs.pwr, but is not designed to minimize
    bytes so comes in JSON format.
    """

    Watts: ReallyAnInt
    TypeName: Literal["power.watts"] = "power.watts"
    Version: Literal["000"] = "000"

    @classmethod
    def type_name_value(cls) -> str:
        return "power.watts"
