"""Type ads111x.based.cac.gt, version 000"""

from pydantic import ConfigDict, PositiveInt, StrictInt, model_validator
from typing_extensions import Literal, Self

from gwproto.enums import TelemetryName
from gwproto.named_types.component_attribute_class_gt import ComponentAttributeClassGt
from gwproto.property_format import (
    check_is_ads1115_i2c_address,
)


class Ads111xBasedCacGt(ComponentAttributeClassGt):
    ads_i2c_address_list: list[StrictInt]
    total_terminal_blocks: PositiveInt
    telemetry_name_list: list[TelemetryName]
    type_name: Literal["ads111x.based.cac.gt"] = "ads111x.based.cac.gt"
    version: Literal["000"] = "000"

    model_config = ConfigDict(extra="allow")

    @model_validator(mode="after")
    def _check_ads_i2c_address_list(self) -> Self:
        try:
            for elt in self.ads_i2c_address_list:
                check_is_ads1115_i2c_address(elt)
        except ValueError as e:
            raise ValueError(
                f"AdsI2cAddressList element failed Ads1115I2cAddress format validation: {e}",
            ) from e
        return self

    @model_validator(mode="after")
    def check_axiom_1(self) -> Self:
        """
        Axiom 1: TerminalBlock Ads Chip consistency.
        TotalTerminalBlocks should be greater than 4 * (len(AdsI2cAddressList) - 1 ) and less than or equal to 4*len(AdsI2cAddressList)
        """
        # Implement check for axiom 1"
        return self
