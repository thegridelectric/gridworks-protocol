"""Type ads111x.based.cac.gt, version 000"""

from typing import List, Literal

from pydantic import (
    ConfigDict,
    PositiveInt,
    field_validator,
    model_validator,
)
from typing_extensions import Self

from gwproto.enums import TelemetryName
from gwproto.property_format import (
    check_is_ads1115_i2c_address,
)
from gwproto.types.component_attribute_class_gt import ComponentAttributeClassGt


class Ads111xBasedCacGt(ComponentAttributeClassGt):
    AdsI2cAddressList: List[str]
    TotalTerminalBlocks: PositiveInt
    TelemetryNameList: List[TelemetryName]
    TypeName: Literal["ads111x.based.cac.gt"] = "ads111x.based.cac.gt"
    Version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow", use_enum_values=True)

    @field_validator("AdsI2cAddressList")
    @classmethod
    def _check_ads_i2c_address_list(cls, v: List[str]) -> List[str]:
        try:
            for elt in v:
                check_is_ads1115_i2c_address(elt)
        except ValueError as e:
            raise ValueError(
                f"AdsI2cAddressList element failed Ads1115I2cAddress format validation: {e}",
            ) from e
        return v

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: TerminalBlock Ads Chip consistency.
        TotalTerminalBlocks should be greater than 4 * (len(AdsI2cAddressList) - 1 ) and less than or equal to 4*len(AdsI2cAddressList)
        """
        # Implement check for axiom 1"
        return self
