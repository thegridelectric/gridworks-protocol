"""Type i2c.multichannel.dt.relay.component.gt, version 000"""

from typing import Literal

from pydantic import ConfigDict, StrictInt, model_validator
from typing_extensions import Self

from gwproto.named_types.component_gt import ComponentGt
from gwproto.named_types.relay_actor_config import RelayActorConfig


class I2cMultichannelDtRelayComponentGt(ComponentGt):
    """ASL schema of record [i2c.multichannel.dt.relay.component.gt v002](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/i2c.multichannel.dt.relay.component.gt.002.yaml)"""

    i2c_address_list: list[StrictInt]
    config_list: list[RelayActorConfig]
    type_name: Literal["i2c.multichannel.dt.relay.component.gt"] = (
        "i2c.multichannel.dt.relay.component.gt"
    )
    version: Literal["002"] = "002"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_3(self) -> Self:
        """g
        Axiom 2: Actor and Idx Consistency.
        There are no duplicates of ActorName or RelayIdx in the RelayConfigList
        """
        # Implement Axiom(s)
        return self
