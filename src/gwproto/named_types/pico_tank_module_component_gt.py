"""Type pico.tank.reader.component.gt, version 010"""

from typing import Literal, Optional

from pydantic import ConfigDict, model_validator
from typing_extensions import Self

from gwproto.enums import TempCalcMethod
from gwproto.named_types.component_gt import ComponentGt


class PicoTankModuleComponentGt(ComponentGt):
    """ASL schema of record [pico.tank.module.component.gt v010](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/schemas/pico.tank.module.component.gt.010.yaml)"""

    enabled: bool
    pico_hw_uid: Optional[str] = None
    pico_a_hw_uid: Optional[str] = None
    pico_b_hw_uid: Optional[str] = None
    temp_calc_method: TempCalcMethod
    thermistor_beta: int
    send_micro_volts: bool
    samples: int
    num_sample_averages: int
    pico_k_ohms: Optional[int] = None
    serial_number: str = "NA"
    async_capture_delta_micro_volts: int
    type_name: Literal["pico.tank.module.component.gt"] = (
        "pico.tank.module.component.gt"
    )
    version: str = "010"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: PicoHwUid exists  XOR (both PicoAHwUid and PicoBHwUid exist)
        """
        if self.pico_hw_uid is not None:
            if self.pico_a_hw_uid or self.pico_b_hw_uid:
                raise ValueError(
                    "Can't have both PicoHwUid and any of (PicoAHwUid, PicoBHwUid"
                )
        elif not (self.pico_a_hw_uid and self.pico_b_hw_uid):
            raise ValueError(
                "If PicoHwUid is not set, PicoAHwUid and PicoBHwUid must both be set!"
            )

        return self

    @model_validator(mode="after")
    def check_axiom_2(self) -> Self:
        """
        Axiom 2: PicoKOhms exists iff TempCalcMethod is TempCalcMethod.SimpleBetaForPico
        # note this is a known incorrect method, but there are a few in the field
        # that do this.
        """
        is_simple_beta = self.temp_calc_method == TempCalcMethod.SimpleBetaForPico
        has_kohms = self.pico_k_ohms is not None

        if is_simple_beta != has_kohms:
            raise ValueError(
                "PicoKOhms must be provided if and only if TempCalcMethod is SimpleBetaForPico"
            )

        return self
