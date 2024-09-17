"""Type resistive.heater.cac.gt, version 001"""

from typing import Literal

from pydantic import PositiveInt

from gwproto.property_format import (
    ReallyAnInt,
)
from gwproto.types.component_attribute_class_gt import ComponentAttributeClassGt


class ResistiveHeaterCacGt(ComponentAttributeClassGt):
    NameplateMaxPowerW: ReallyAnInt
    RatedVoltageV: PositiveInt
    TypeName: Literal["resistive.heater.cac.gt"] = "resistive.heater.cac.gt"
    Version: Literal["001"] = "001"

    @classmethod
    def type_name_value(cls) -> str:
        return "resistive.heater.cac.gt"
