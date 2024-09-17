"""Type i2c.multichannel.dt.relay.component.gt, version 000"""

from typing import List, Literal

from pydantic import field_validator

from gwproto.property_format import (
    ReallyAnInt,
)
from gwproto.types.component_gt import ComponentGt
from gwproto.types.relay_actor_config import RelayActorConfig


class I2cMultichannelDtRelayComponentGt(ComponentGt):
    """
    I2c Multichannel Double Throw Relay Component.

    A specific instance of a board with multiple double-throw electromechanical relays. The
    board is expected to be addressable over i2c, with that address being configurable to a
    finite number of choices via dipswitches.
    """

    I2cAddressList: List[ReallyAnInt]
    RelayConfigList: List[RelayActorConfig]
    TypeName: Literal["i2c.multichannel.dt.relay.component.gt"] = (
        "i2c.multichannel.dt.relay.component.gt"
    )
    Version: Literal["000"] = "000"

    @field_validator("RelayConfigList")
    @classmethod
    def check_relay_config_list(
        cls, v: List[RelayActorConfig]
    ) -> List[RelayActorConfig]:
        """g
        Axiom 2: Actor and Idx Consistency.
        There are no duplicates of ActorName or RelayIdx in the RelayConfigList
        """
        # Implement Axiom(s)
        return v

    @classmethod
    def type_name_value(cls) -> str:
        return "i2c.multichannel.dt.relay.component.gt"
