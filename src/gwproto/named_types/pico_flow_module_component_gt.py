"""Type pico.flow.module.component.gt, version 000"""

from typing import Literal, Optional

from pydantic import ConfigDict, PositiveInt, StrictInt, model_validator
from typing_extensions import Self

from gwproto.enums import GpmFromHzMethod, HzCalcMethod, MakeModel
from gwproto.named_types.component_gt import ComponentGt
from gwproto.property_format import (
    SpaceheatName,
)


class PicoFlowModuleComponentGt(ComponentGt):
    """ASL schema of record [pico.flow.module.component.gt v000](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/pico.flow.module.component.gt.000.yaml)"""

    enabled: bool
    serial_number: str
    flow_node_name: SpaceheatName
    flow_meter_type: MakeModel
    hz_calc_method: HzCalcMethod
    gpm_from_hz_method: GpmFromHzMethod
    constant_gallons_per_tick: float
    send_hz: bool
    send_gallons: bool
    send_tick_lists: bool
    no_flow_ms: PositiveInt
    async_capture_threshold_gpm_times100: StrictInt
    publish_empty_ticklist_after_s: Optional[PositiveInt] = None
    publish_any_ticklist_after_s: Optional[PositiveInt] = None
    publish_ticklist_period_s: Optional[PositiveInt] = None
    publish_ticklist_length: Optional[PositiveInt] = None
    exp_alpha: Optional[float] = None
    cutoff_frequency: Optional[float] = None
    type_name: Literal["pico.flow.module.component.gt"] = (
        "pico.flow.module.component.gt"
    )
    version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
                Axiom 1: Param consistency.
                - If HzCalcMethod is BasicExpWeightedAvg then ExpAlpha must exist.
        - If HzCalcMethod is BasicButterhworth then CutoffFrequency must exist


        """
        # Implement check for axiom 1""
        return self
