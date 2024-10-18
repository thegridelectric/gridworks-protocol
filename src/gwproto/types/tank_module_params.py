"""Type tank.module.params, version 100"""

from typing import Literal, Optional

from pydantic import BaseModel, PositiveInt, field_validator

from gwproto.property_format import SpaceheatName


class TankModuleParams(BaseModel):
    HwUid: str
    ActorNodeName: SpaceheatName
    PicoAB: str
    CapturePeriodS: PositiveInt
    Samples: PositiveInt
    NumSampleAverages: PositiveInt
    AsyncCaptureDeltaMicroVolts: PositiveInt
    CaptureOffsetS: Optional[float] = None
    TypeName: Literal["tank.module.params"] = "tank.module.params"
    Version: Literal["100"] = "100"

    @field_validator("PicoAB")
    @classmethod
    def check_pico_a_b(cls, v: str) -> str:
        """
        Axiom 1: "PicoAB must be a or b"
        """
        if v not in {"a", "b"}:
            raise ValueError(f"PicoAB must be lowercase a or lowercase b, not <{v}>")
        return v
