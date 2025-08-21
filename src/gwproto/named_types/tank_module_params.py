"""Type tank.module.params, version 110"""

from typing import Literal, Optional

from gw.named_types import GwBase
from pydantic import PositiveInt, model_validator
from typing_extensions import Self

from gwproto.property_format import (
    SpaceheatName,
)


class TankModuleParams(GwBase):
    """ASL schema of record [tank.module.params v110](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/tank.module.params.110.yaml)"""

    hw_uid: str
    actor_node_name: SpaceheatName
    pico_a_b: Optional[str] = None
    capture_period_s: PositiveInt
    samples: PositiveInt
    num_sample_averages: PositiveInt
    async_capture_delta_micro_volts: PositiveInt
    capture_offset_s: Optional[float] = None
    type_name: Literal["tank.module.params"] = "tank.module.params"
    version: Literal["110"] = "110"

    @model_validator(mode="after")
    def check_pico_a_b(self) -> Self:
        """
        Axiom 1: "If PicoAB exists it must be a or b"
        """
        if self.pico_a_b and self.pico_a_b not in ["a", "b"]:
            raise ValueError(
                f"Axiom 1: If PicoAB exists it must be a or b, not {self.pico_a_b}"
            )

        return self
